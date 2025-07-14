import numpy as np
from prob_in_circ import prob_in_circ
import matplotlib.pyplot as plt
from calc_ipix import calc_ipix
def where_to(hpx, bulkra, bulkdec, FOV,nside,labels, centroids,bulkpix ):
    ra_arr = []
    dec_arr = []
    r = np.sqrt(FOV / np.pi)
    prob_arr = []
    pointsra1 = []
    pointsdec1 = []
    ra_l, ra_r = min(bulkra), max(bulkra)
    dec_l, dec_u = min(bulkdec), max(bulkdec)
    # print('radecradec', ra_l, ra_r, dec_l, dec_u)
    nra = int((ra_r - ra_l) /r)
    ndec = int((dec_u - dec_l) / r)
    # print('nra ndec',nra,ndec)
    # print('sqrtFOV',(ra_r - ra_l) / nra, (dec_u - dec_l) / ndec)
    for i in range(0, ndec + 1):
        dec_arr.append(dec_l + i * (dec_u - dec_l) / ndec)
    dec_arr.append(dec_u)

    for j in range(0, ndec + 1):
        # nra = int((1-np.sin(np.deg2rad(abs(dec_arr[j]))))*(ra_r - ra_l) / np.sqrt(2*FOV / np.pi))
        nra = int((ra_r - ra_l) / (1 / np.sin(np.deg2rad(90 + dec_arr[j])) * np.sqrt(2 * FOV / np.pi)))
        if nra == 0:
            nra = 1
        for i in range(0, nra + 1):
            print('nra', nra)
            ra_arr.append(ra_l + i * (ra_r - ra_l) / nra)
            print('dec_arr[jj],ra_arr[i]nra', dec_arr[j], ra_arr[i], nra)
            # print('dec_l + i * (dec_u - dec_l) / ndec)',dec_l + i * (dec_u - dec_l) / ndec)
    # print('arr', ra_arr, dec_arr, n, N)
    # print(ra_l, ra_r, dec_l, dec_u)
    ra_arr.append(ra_r)
    jj = 0
    for i in range(len(ra_arr)):
        pointsdec1.append(dec_arr[jj])
        pointsra1.append(ra_arr[i])
        print('dec_arr[jj],ra_arr[i]', dec_arr[jj], ra_arr[i])
        if i < len(ra_arr) - 1 and ra_arr[i + 1] < ra_arr[i]:
            jj = jj + 1


    pointsra = []
    pointsdec = []
    pointslabels=[]
    print('centroids',centroids)
    #plt.plot(1, 1)
    #plt.show()
    if len(centroids)>1:
        for i in range(len(pointsdec1)):
            print('where to', i, len(pointsdec1))

            temp_len = 100000
            temp_label=0
            # if (0.96 * bulkra[j] <= pointsra1[i] <= 1.04 * bulkra[j] and (0.96 * bulkdec[j] <= pointsdec1[i] <= 1.04 * bulkdec[j] or 1.04 * bulkdec[j] <= pointsdec1[i] <= 0.96 * bulkdec[j])) and i not in iis:
            # if abs(bulkra[j] - pointsra1[i])  +abs( bulkdec[j] - pointsdec1[i]) < 0.5  and i not in iis:
            if prob_in_circ(hpx, pointsra1[i], pointsdec1[i], r, nside) > 0.000001 :
            #if calc_ipix(pointsra1[i], pointsdec1[i],nside) in bulkpix  :

                for j in range(len(centroids)):
                    print('j',j,abs(centroids[j][0] - pointsra1[i])  + abs(centroids[j][1] - pointsdec1[i]),temp_len)
                    if abs(centroids[j][0] - pointsra1[i])  + abs(centroids[j][1] - pointsdec1[i]) <temp_len:
                        temp_len=abs(centroids[j][0] - pointsra1[i]) + abs(centroids[j][1] - pointsdec1[i])
                        temp_label=j
                pointsra.append(pointsra1[i])
                pointsdec.append(pointsdec1[i])
                pointslabels.append(temp_label)

    else:
        for i in range(len(pointsdec1)):
            if prob_in_circ(hpx, pointsra1[i], pointsdec1[i], r, nside) > 0.000001 :
                pointsra.append(pointsra1[i])
                pointsdec.append(pointsdec1[i])
                pointslabels.append(0)
    print('pointslabels',len(pointslabels),len(labels))
    print('pointslabels',pointslabels,labels)
    print('pointslabels1',1 in labels,1 in pointslabels,0 in labels,0 in pointslabels)

    #plt.plot(2,2)
    #plt.show()
    return  pointsra, pointsdec, pointsra1, pointsdec1, nra, ndec, pointslabels

