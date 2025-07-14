import numpy as np


def path(tele, raI, decI, ra, dec,  timearr, theta, phi, tottime, turn_points_ra,turn_points_dec):

    time, flag, flago,flago2,flag2,timetheta, timephi,sign,time2 = tele.time(ra, dec, raI, decI)
    n = 20
    for i in range( n ):
        timearr[i] = ((i) / n) * time
        phi[i], theta[i] = tele.place(timearr[i], raI, decI, flag, flago,flag2,flago2,  ra, dec, timetheta, timephi,sign,time2)
        timearr[i] = tottime + ((i) / n) * time
    return phi, theta, timearr, i,turn_points_ra,turn_points_dec
