import numpy as np
n = 150

def Type1Mat(phis1, thetas1,phis2, thetas2,  bulkra, bulkdec, bulk, timearrs1,timearrs2,scanned_ra, scanned_dec,scanned_time):
    time_mat = np.zeros((2 * n, 2 * n))
    time_mat1 = np.zeros((2 * n, 2 * n))

    for i in range(len(scanned_ra)):
        for j in range(len(scanned_ra[i])):
            time_mat[int(n * scanned_ra[i][j] / 180) - 1, int(n * (scanned_dec[i][j]) / 90) - 1] = -max(bulk) + 0.8 *(scanned_time[i]* max(bulk) / max(scanned_time))


    for i in range(len(bulk)):
        # print('LL', bulkra[i], bulkdec[i])
        if time_mat[int(n * bulkra[i] / 180 - 1), int(n * (bulkdec[i]) / 90 - 1)]==0:
            time_mat[int(n * bulkra[i] / 180 - 1), int(n * (bulkdec[i]) / 90 - 1)] = bulk[i]

    # print('n',n)
    for i in range(len(timearrs1)):
        time_mat[int(n * phis1[i] / 180) - 1, int(n * (thetas1[i]) / 90) - 1] = -max(bulk) +0.6 * (timearrs1[i] * max(bulk) / max(timearrs1))
    for i in range(len(timearrs2)):
        time_mat[int(n * phis2[i] / 180) - 1, int(n * (thetas2[i]) / 90) - 1] = -max(bulk) + 0.6 * (timearrs2[i] * max(bulk) / max(timearrs2))



    for j in range(0, 18):
        time_mat[int(n * j * 10 / 180), :] = max(bulk) / 2
    for j in range(18, 36):
        time_mat[int(n * j * 10 / 180), :] = max(bulk) / 5
    for j in range(0, 9):
        time_mat[:, int(n * j * 10 / 90)] = max(bulk) / 1.2
    for j in range(10, 18):
        time_mat[:, int(n * j * 10 / 90)] = max(bulk) / 1.6
    for i in range(2 * n):
        for j in range(2 * n):
            time_mat1[i, j] = time_mat[i, n - 1 - j];

    # k = np.zeros((2 * n, n))
    # time_matN = np.hstack((time_mat1, k))
    time_matN = time_mat1
    return time_matN




