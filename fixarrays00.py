import numpy as np

def fixarrays00(phis, thetas, timearrs):
    # Convert input lists to numpy arrays
    print('fixarrays001',phis, thetas, timearrs)
    phis = np.array(phis)
    thetas = np.array(thetas)
    timearrs = np.array(timearrs)

    # Find the minimum length among the three arrays
    min_length = min(len(phis), len(thetas), len(timearrs))

    # Trim all arrays to the minimum length
    #phis = phis[:min_length]
    #thetas = thetas[:min_length]
    #timearrs = timearrs[:min_length]

    # Identify indices where both phis[i] and thetas[i] are zero
    indices_to_remove = np.where((phis == 0) & (thetas == 0))[0]

    # Create masks to filter out the unwanted indices
    mask = np.ones(len(phis), dtype=bool)
    mask[indices_to_remove] = False

    # Apply the mask to all three arrays
    phis = phis[mask]
    thetas = thetas[mask]
    timearrs = timearrs[mask]
    print('fixarrays002',phis, thetas, timearrs)

    return phis, thetas, timearrs
