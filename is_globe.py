import numpy as np
from find_missing_number import find_missing_number


def is_globe(bulkra, bulkdec, labels):
    bulkra = np.array(bulkra)
    bulkdec = np.array(bulkdec)
    labels = np.array(labels)

    globe = False
    globe1 = False
    globe2 = False
    globemin1 = 360
    globemin2 = 360
    globemax1 = 0
    globemax2 = 0

    # Check for globe wraparound
    for i in range(len(bulkra)):
        if bulkra[i] > 359:
            close_indices = (bulkra < 1) & ((0.98 * bulkdec < bulkdec[i]) & (bulkdec[i] < 1.02 * bulkdec))
            if np.any(close_indices & (labels != labels[i])):
                globe = True
                ii, jj = i, np.where(close_indices)[0][0]
                break

    if globe:
        temp = max(labels[ii], labels[jj])
        temp1 = min(labels[ii], labels[jj])
        labels[labels == temp] = temp1

        temp_labels = labels == temp1
        other_labels = labels != temp1

        if np.any(temp_labels):
            globemax1 = np.max(bulkra[temp_labels])
            globemin1 = np.min(bulkra[temp_labels])
        if np.any(other_labels):
            globemax2 = np.max(bulkra[other_labels])
            globemin2 = np.min(bulkra[other_labels])

    globemax = min(globemax1, globemax2)
    globemin = max(globemin1, globemin2)

    # Check for North Pole
    north_indices = (bulkdec > 89)
    for i in range(len(bulkra)):
        if north_indices[i]:
            close_indices = (0.98 * bulkra[i] < bulkra + 180) & (bulkra + 180 < 1.02 * bulkra[i])
            if np.any(close_indices):
                globe1 = True
                ii, jj = i, np.where(close_indices)[0][0]
                break

    if globe1:
        temp = max(labels[ii], labels[jj])
        temp1 = min(labels[ii], labels[jj])
        labels[labels == temp] = temp1

    # Check for South Pole
    south_indices = (bulkdec < -89)
    for i in range(len(bulkra)):
        if south_indices[i]:
            close_indices = (0.98 * bulkra[i] < bulkra + 180) & (bulkra + 180 < 1.02 * bulkra[i])
            if np.any(close_indices):
                globe2 = True
                ii, jj = i, np.where(close_indices)[0][0]
                break

    if globe2:
        temp = max(labels[ii], labels[jj])
        temp1 = min(labels[ii], labels[jj])
        labels[labels == temp] = temp1

    # Resolve missing numbers in labels
    count = 0
    b = 1
    while count < 15 and len(set(labels)) > 1:
        missing = find_missing_number(labels)
        if not missing:
            break
        labels[labels == (missing + b)] = missing
        count += 1
        if count == 3:
            labels.fill(0)

    return labels.tolist(), globe, globe1, globe2, globemin, globemax
