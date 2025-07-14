import matplotlib.pyplot as plt
import numpy as np


def path(tele, raI, decI, ra, dec, tchange, rachange, decchange, ii, timearr, theta, phi, tottime, j,turn_points_ra,turn_points_dec):
    br=False
    #print('1,',tele, raI, decI, ra, dec, tchange, rachange, decchange, ii, timearr, theta, phi, tottime, j)
    #plt.plot(2, 2)
    #plt.show()
        #if isinstance(tele, tele_deg):
            #time, flag = tele.time(ra, dec, raI, decI)
            #print('ttttttt1', time)
        #if isinstance(tele, tele_acc):
        #print('ti4', ra, dec, tchange, rachange, decchange)

       # plt.plot(2, 2)
        #plt.show()
    j=0
    time, flag, flago,flago2,flag2,timetheta, timephi,sign,time2 = tele.time(ra, dec, raI, decI)
           # print('ttttttt2', time)
        #print('ti4', ra, dec, tchange, rachange, decchange)

    if tchange[0]<time:
        time, flag, flago, flago2, flag2, timetheta, timephi, sign, time2 = tele.time(ra, dec, raI, decI)
        n = 20

        for i in range(n):
            timearr[i] = (i / n) * time
            if timearr[i]>0.95*tchange[0]:
                br=True
                break
            # for j in range (0,len(tchange)):
            # if isinstance(tele,tele_deg):
            # phi[i], theta[i] = tele.place(timearr[i], raI, decI, flag, ra, dec)
            # if isinstance(tele, tele_acc):
            print('1', timearr[i])
            # print('time', time, time2)
            # plt.plot(2, 2)
            # plt.show()
            phi[i], theta[i] = tele.place(timearr[i], raI, decI, flag, flago, flag2, flago2, ra, dec, timetheta, timephi, sign, time2)
            timearr[i] = tottime + ((i - ii) / n) * time

    while br:
        time, flag, flago, flago2, flag2, timetheta, timephi, sign, time2 = tele.time(ra, dec,rachange[j], decchange[j])
        for i in range(n):
            timearr[i] = (i / n) * time
            if timearr[i] > 0.95 * tchange[0]:
                br = True
                break
            # for j in range (0,len(tchange)):
            # if isinstance(tele,tele_deg):
            # phi[i], theta[i] = tele.place(timearr[i], raI, decI, flag, ra, dec)
            # if isinstance(tele, tele_acc):
            print('1', timearr[i])
            # print('time', time, time2)
            # plt.plot(2, 2)
            # plt.show()
            phi[i], theta[i] = tele.place(timearr[i],rachange[i], decchange[i], flag, flago, flag2, flago2, ra, dec, timetheta, timephi, sign, time2)
            timearr[i] = tottime + ((i - ii) / n) * time
        j += 1
    #print('arrrrrrr', timearr,phi,theta )
#plt.plot(2,2)
#plt.show()


    return phi, theta, timearr, i,turn_points_ra,turn_points_dec
