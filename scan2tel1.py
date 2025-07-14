import numpy as np
from path import path
from is_it_here import is_it_here
import matplotlib.pyplot as plt

#from scopes100 import labels
from kmeans import kmeans
from closest_point import closest_point
from labelmax_solo import labelmax_solo
from plant_event import plant_event
from prob_in_blob import prob_in_blob
def scan2tel1(phiI, thetaI, pointsras, pointsdecs, tele,t_update, minrap, mindecp, ramax, decmax,  ii, timearr, theta, phi, tottime, j,event_ipix,hpxs,nside,kks,phis,thetas,timearrs,r,passedra,passeddec,scanned_ra,scanned_dec,scanned_pix,scanned_time,kk,pointslabelss,labelss,labelmax,delay,file_name,area_update,r2, kk1, kk2,turn_points_ra,turn_points_dec,met,bulks, bulkras, bulkdecs,scanned_pix_s,z,t0):
    is_here = False
    rachange = []
    decchange = []
    tchange = []
    uflag=0
    merge=False

    hpx = hpxs[0]
    pointslabels = pointslabelss[0]
    bulk = bulks[0]
    bulkra = bulkras[0]
    bulkdec = bulkdecs[0]
    pointsra1=pointsras[0]
    pointsdec1=pointsdecs[0]
    pointsra=pointsra1
    pointsdec=pointsdec1

    time, flag, flago,flago2,flag2,timetheta, timephi,sign,time2 = tele.time(minrap, mindecp,phiI, thetaI)

    if t_update!=[]:
        while (time >= t_update[uflag] ):

            uflag = uflag + 1
            hpx, bulk, bulkra, bulkdec, pointsra, pointsdec, pointslabels,labels= hpxs[uflag],bulks[uflag],bulkras[uflag],bulkdecs[uflag],pointsras[uflag],pointsdecs[uflag],pointslabelss[uflag],labelss[uflag]

            ra, dec = tele.place(t_update[uflag-1]-timearrs[-1],phiI, thetaI, flag, flago, flag2, flago2,minrap, mindecp, timetheta, timephi, sign, time2)
            turn_points_ra=np.append(turn_points_ra,ra)
            turn_points_dec=np.append(turn_points_dec,dec)
            phi, theta, timearr,i, turn_points_ra, turn_points_dec = path(tele, phiI, thetaI,ra, dec , timearr, theta, phi, tottime, turn_points_ra, turn_points_dec)
            phis = np.append(phis, phi)
            thetas = np.append(thetas, theta)
            timearr = np.add(timearr, timearrs[-1])
            timearrs = np.append(timearrs, timearr)

            labelmax, bulkramax, bulkdecmax, minrap, mindecp=labelmax_solo(bulk,labels,tele, ra, dec,pointsra,pointsdec, pointslabels)

            time, flag, flago, flago2, flag2, timetheta, timephi, sign, time2 = tele.time( minrap, mindecp,ra, dec)
            phiI,thetaI=ra, dec
            if uflag == len(t_update):
                break


    if not merge:
        delay=0

    phi, theta, timearr, i,turn_points_ra,turn_points_dec = path(tele, phiI, thetaI, minrap, mindecp, timearr, theta, phi, tottime, turn_points_ra,turn_points_dec)
    phis = np.append(phis, phi)
    thetas = np.append(thetas, theta)
    timearr = np.add(timearr, timearrs[-1])
    timearr[-1]=timearr[-1]+delay
    timearrs = np.append(timearrs, timearr)
    if timearrs[-1]>=t0 and timearrs[-1]!=100000:
        merge= True
        if met == 0 and event_ipix == 0 and z == 0:
            event_idx, event_ipix = plant_event(bulk, bulkra, bulkdec, nside)
    else:
        merge= False
    if merge:
        passedra.append(minrap)
        passeddec.append(mindecp)
        is_here, scanned_ra1, scanned_dec1,ipix_disc = is_it_here(minrap, mindecp, r, nside, event_ipix)
        scanned_time.append(timearrs[-1])
        scanned_ra.append(scanned_ra1)
        scanned_dec.append(scanned_dec1)
        if (tele.name == 'BIG' or tele.name == 'ULTRASAT') and is_here:
            scanned_pix_s = ipix_disc

        else:
            scanned_pix.extend(ipix_disc)

    return phis, thetas, timearrs,  scanned_ra, scanned_dec,scanned_pix, scanned_time,passedra, passeddec,is_here,minrap,mindecp,event_ipix,turn_points_ra,turn_points_dec,scanned_pix_s,labelmax
