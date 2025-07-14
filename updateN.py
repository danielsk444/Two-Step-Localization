from gauge import gauge
from is_globe import is_globe
import numpy as np
from calc_ipix import calc_ipix
from prob_in_circ import prob_in_circ
import matplotlib.pyplot as plt
from event_update import event_update
from kmeans import kmeans

def updateN(nside,pointsra1,pointsdec1,r,area,hpx):
    print('updateN')
    hpx1, bulk, bulkra, bulkdec,bulkpix, probrob, A,good_area =event_update(area,hpx)
    #('area,A',area,A,good_area)
    labels, labelsc, nkmeans,centroids = kmeans(bulkra, bulkdec)

    pointsra = []
    pointsdec = []
    pointslabels=[]
    if len(centroids) > 1:
        for i in range(len(pointsdec1)):
            temp_len = 100000
            temp_label = 0
            # if (0.96 * bulkra[j] <= pointsra1[i] <= 1.04 * bulkra[j] and (0.96 * bulkdec[j] <= pointsdec1[i] <= 1.04 * bulkdec[j] or 1.04 * bulkdec[j] <= pointsdec1[i] <= 0.96 * bulkdec[j])) and i not in iis:
            # if abs(bulkra[j] - pointsra1[i])  +abs( bulkdec[j] - pointsdec1[i]) < 0.5  and i not in iis:
            if prob_in_circ(hpx1, pointsra1[i], pointsdec1[i], r, nside) > 0.000001:
            #if calc_ipix(pointsra1[i], pointsdec1[i], nside) in bulkpix:

                for j in range(len(centroids)):
                    if abs(centroids[j][0] - pointsra1[i]) + abs(centroids[j][1] - pointsdec1[i]) < temp_len:
                        temp_len = abs(centroids[j][0] - pointsra1[i]) + abs(centroids[j][1] - pointsdec1[i])
                        temp_label = j
                pointsra.append(pointsra1[i])
                pointsdec.append(pointsdec1[i])
                pointslabels.append(labels[temp_label])
    else:
        for i in range(len(pointsdec1)):
            #print('updateN2',i,len(pointsdec1))
            if prob_in_circ(hpx1, pointsra1[i], pointsdec1[i], r, nside) > 0.000001:
            #if calc_ipix(pointsra1[i], pointsdec1[i], nside) in bulkpix:
                pointsra.append(pointsra1[i])
                pointsdec.append(pointsdec1[i])
                pointslabels.append(0)

    return hpx1,bulk, bulkra, bulkdec,pointsra,pointsdec,pointslabels,labels, labelsc, nkmeans


