import numpy as np
import matplotlib.pyplot as plt

def closest_point(bulkramax, bulkdecmax, tele, raI, decI):
    mintime = 100000
    ra=0
    dec=0
    temptime = 0

    print('3',bulkdecmax,raI,decI)
    for i in range(len(bulkdecmax)):
        temptime, flag, flago,flago2,flag2, timetheta, timephi, sign, time2 = tele.time(bulkramax[i], bulkdecmax[i], raI, decI)
        if temptime < mintime:
            mintime = temptime
            ra = bulkramax[i]
            dec = bulkdecmax[i]



    return ra, dec,mintime