import numpy as np
n = 150
def scan_mat( scanned_ra, scanned_dec,scanned_time):
    time_mat = np.NAN((2 * n, 2 * n))
    time_mat1 = np.NAN((2 * n, 2 * n))

    for i in range(len(scanned_ra)):
        for j in range(len(scanned_ra[i])):
            time_mat[int(n * scanned_ra[i][j] / 180) - 1, int(n * (scanned_dec[i][j]) / 90) - 1] =  (scanned_time[i] / max(scanned_time))

    for i in range(2 * n):
        for j in range(2 * n):
            time_mat1[i, j] = time_mat[i, n - 1 - j];

    # k = np.zeros((2 * n, n))
    # time_matN = np.hstack((time_mat1, k))
    time_matN = time_mat1
    return time_matN
