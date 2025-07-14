import numpy as np
from scan2tel1 import scan2tel1
from scan2tel2 import scan2tel2
from calc_ipix import calc_ipix
from path import path
from is_kmean_scanned import is_kmean_scanned
from calc_ra_dec import calc_ra_dec
from timearrs_fix import timearrs_fix
from is_it_here import is_it_here
def scan2telN(pointsras, pointsdecs, tele1, tele2, phiI, thetaI, phiI2, thetaI2, minra1, mindec1, minra2, mindec2,  rachange, decchange, ii, gg, timearr, theta, phi, tottime, j, jg, labelss,nkmeans,
             event_ipix,bulks,bulkras,bulkdecs,hpxs,nside,pointslabelss,labelmax1,labelmax2,t_update,area_update,file_name,met,starting_t,z,t0):
    pointsra1=pointsras[0]
    pointsra2=pointsras[0]
    pointsdec1=pointsdecs[0]
    pointsdec2=pointsdecs[0]
    hpx1=hpxs[0]
    labels1=labelss[0]
    pointslabels1=pointslabelss[0]
    bulk1=bulks[0]
    bulkra1=bulkras[0]
    bulkdec1=bulkdecs[0]
    hpx2=hpxs[0]
    labels2=labelss[0]
    pointslabels2=pointslabelss[0]
    bulk2=bulks[0]
    bulkra2=bulkras[0]
    bulkdec2=bulkdecs[0]
    tchange = [10000]
    phis1 = [phiI]
    thetas1 = [thetaI]
    timearrs1 = [starting_t]
    phis2 = [phiI2]
    thetas2 = [thetaI2]
    timearrs2 = [starting_t]
    scanned_ra = []
    scanned_dec = []
    scanned_ra1 = []
    scanned_dec1 = []
    scanned_ra2 = []
    scanned_dec2 = []
    scanned_pix = []
    scanned_pix1 = []
    scanned_pix2 = []
    scanned_time = []
    scanned_time1 = []
    scanned_time2 = []
    rax=0
    decx=0
    passedra1 = []
    passeddec1 = []
    turn_points_ra=[]
    turn_points_dec =[]
    passedra2 = []
    passeddec2 = []
    who_found = 0
    change_is_here=False
    kk1 = 0
    kk2 = 0
    call = False
    kks=[]
    F1 = np.sqrt(tele1.FOV)
    r1 = np.sqrt(tele1.FOV / np.pi)
    F2 = np.sqrt(tele2.FOV)
    r2 = np.sqrt(tele2.FOV / np.pi)
    t_scan=0
    scanned_pix_s=0
    scanned_ra_s = 0
    scanned_dec_s = 0
    uflag1=0
    uflag2=0
    flag0=False
    flag1=False
    flag2 = False
    c1 = 1.5
    c2 = 1.5
    countwhile1 = 0
    countwhile2 = 0
    y1=labelmax1
    y2=labelmax2
    delay=15
    changepix=calc_ipix(rachange,decchange,nside)
    merge=False
    if met!=2:
        phis1, thetas1, timearrs1, scanned_ra, scanned_dec, scanned_pix, scanned_time, passedra1, passeddec1, is_here,  minrap1, mindecp1,event_ipix,turn_points_ra,turn_points_dec,scanned_pix_s,y1=scan2tel1( phiI, thetaI, pointsras, pointsdecs, tele1,t_update, minra1, mindec1, rachange, decchange,  ii, timearr, theta, phi, tottime, j,event_ipix,hpxs,nside,kks,phis1,thetas1,timearrs1,r1,passedra1,passeddec1,scanned_ra,scanned_dec,scanned_pix,scanned_time,kk1,pointslabelss,labelss,labelmax1,delay,file_name,area_update,r2, kk1, kk2,turn_points_ra,turn_points_dec,met,bulks, bulkras, bulkdecs,scanned_pix_s,z,t0)
    else:
        phis1, thetas1, timearrs1, scanned_ra1, scanned_dec1, scanned_pix1, scanned_time1, passedra1, passeddec1, is_here,  minrap1, mindecp1,event_ipix,turn_points_ra,turn_points_dec,scanned_pix_s,y1=scan2tel1( phiI, thetaI, pointsras, pointsdecs, tele1,t_update, minra1, mindec1, rachange, decchange,  ii, timearr, theta, phi, tottime, j,event_ipix,hpxs,nside,kks,phis1,thetas1,timearrs1,r1,passedra1,passeddec1,scanned_ra1,scanned_dec1,scanned_pix1,scanned_time1,kk1,pointslabelss,labelss,labelmax1,delay,file_name,area_update,r2, kk1, kk2,turn_points_ra,turn_points_dec,met,bulks, bulkras, bulkdecs,scanned_pix_s,z,t0)

    if is_here:
        if met == 0 or met==1 :
            flag0 = True
            scanned_ra_s=scanned_ra[-1]
            scanned_ra = scanned_ra[:-1]
            scanned_dec_s = scanned_dec[-1]
            scanned_dec = scanned_dec[:-1]
            t_scan = scanned_time[-1]
            scanned_time = scanned_time[:-1]
            timearrs1 = np.append(timearrs1, 100000)

        else:
            flag0 = True
            scanned_ra_s = scanned_ra1[-1]
            scanned_ra1 = scanned_ra1[:-1]
            scanned_dec_s = scanned_dec1[-1]
            scanned_dec1 = scanned_dec1[:-1]
            t_scan = scanned_time1[-1]
            scanned_time1 = scanned_time1[:-1]
            timearrs1 = np.append(timearrs1, 100000)

    if met!=2:
        phis2, thetas2, timearrs2, scanned_ra, scanned_dec, scanned_pix, scanned_time, passedra2, passeddec2, is_here,  minrap2, mindecp2,event_ipix,turn_points_ra,turn_points_dec,scanned_pix_s,y2=scan2tel1( phiI2, thetaI2, pointsras, pointsdecs, tele2,t_update, minra2, mindec2, rachange, decchange,  ii, timearr, theta, phi, tottime, j,event_ipix,hpxs,nside,kks,phis2,thetas2,timearrs2,r2,passedra2,passeddec2,scanned_ra,scanned_dec,scanned_pix,scanned_time,kk2,pointslabelss,labelss,labelmax2,delay,file_name,area_update,r2, kk1, kk2,turn_points_ra,turn_points_dec,met,bulks, bulkras, bulkdecs,scanned_pix_s,z,t0)
    else:
        phis2, thetas2, timearrs2, scanned_ra2, scanned_dec2, scanned_pix2, scanned_time2, passedra2, passeddec2, is_here, minrap2, mindecp2,event_ipix,turn_points_ra,turn_points_dec,scanned_pix_s,y2=scan2tel1( phiI2, thetaI2, pointsras, pointsdecs, tele2,t_update, minra2, mindec2, rachange, decchange,  ii, timearr, theta, phi, tottime, j,event_ipix,hpxs,nside,kks,phis2,thetas2,timearrs2,r2,passedra2,passeddec2,scanned_ra2,scanned_dec2,scanned_pix2,scanned_time2,kk2,pointslabelss,labelss,labelmax2,delay,file_name,area_update,r2, kk1, kk2,turn_points_ra,turn_points_dec,met,bulks, bulkras, bulkdecs,scanned_pix_s,z,t0)

    if is_here:

        who_found=tele2.name



        return phis1, thetas1, timearrs1, phis2, thetas2, timearrs2, scanned_ra, scanned_dec,scanned_pix,scanned_ra1, scanned_dec1,scanned_pix1,scanned_ra2, scanned_dec2,scanned_pix2,scanned_time, scanned_time1,scanned_time2,passedra1, passeddec1, passedra2, passeddec2,  minrap1, mindecp1, minrap2, mindecp2,hpxs,bulks,bulkras,bulkdecs,labelss,event_ipix,turn_points_ra,turn_points_dec,who_found,t_scan,scanned_pix_s, scanned_ra_s, scanned_dec_s,flag0,call

    phis1, thetas1, timearrs1=timearrs_fix(phis1, thetas1, timearrs1)
    phis2, thetas2, timearrs2 = timearrs_fix(phis2, thetas2, timearrs2)

    tempdis1=10000
    tempdis2=10000
    while not is_here:
        if timearrs1[-1]==100000 and timearrs2[-1]>timearrs1[-2] and  met == 0:
            rax, decx = calc_ra_dec(event_ipix, nside)

            phi1, theta1, timearr1, i, turn_points_ra, turn_points_dec = path(tele2, phis2[-1], thetas2[-1], rax, decx, timearr, theta, phi, tottime, turn_points_ra, turn_points_dec)
            phis2 = np.append(phis2, phi1)
            thetas2 = np.append(thetas2, theta1)
            timearr1 = np.add(timearr1, timearrs2[-1])
            timearrs2 = np.append(timearrs2, timearr1)
            who_found = tele1.name
            call=True
            is_here, scanned_ra11, scanned_dec11, ipix_disc = is_it_here(rax, decx, r2, nside, event_ipix)
            scanned_pix.extend(ipix_disc)

            return phis1, thetas1, timearrs1, phis2, thetas2, timearrs2, scanned_ra, scanned_dec, scanned_pix, scanned_ra1, scanned_dec1, scanned_pix1, scanned_ra2, scanned_dec2, scanned_pix2, scanned_time, scanned_time1, scanned_time2, passedra1, passeddec1, passedra2, passeddec2, minrap1, mindecp1, minrap2, mindecp2, hpxs, bulks, bulkras, bulkdecs, labelss, event_ipix, turn_points_ra, turn_points_dec, who_found, t_scan, scanned_pix_s, scanned_ra_s, scanned_dec_s,flag0,call
        if timearrs1[-1]<timearrs2[-1]:
            if  timearrs1[-1]!=100000  and t_update!=[] and uflag1<len(t_update):
                while (timearrs1[-1] >= t_update[uflag1])  :
                    uflag1 = uflag1 + 1
                    hpx1, bulk1, bulkra1, bulkdec1, pointsra1, pointsdec1, pointslabels1,labels1 = hpxs[uflag1], bulks[uflag1], bulkras[uflag1], bulkdecs[uflag1], pointsras[uflag1], pointsdecs[uflag1], pointslabelss[uflag1],labelss[uflag1]
                    if uflag1 == len(t_update):
                        break

            if met!=2:
                phis1, thetas1, timearrs1, kks, scanned_ra, scanned_dec,scanned_pix, scanned_time,passedra1, passeddec1,is_here,countwhile1,kk1,tempdis1,c1,y,change_is_here,scanned_pix_s,event_ipix =scan2tel2(pointsra1, pointsdec1, tele1, tchange, rachange, decchange, ii, timearr, theta, phi, tottime, j, event_ipix, hpx1, nside, minrap1, mindecp1, kks, phis1, thetas1, timearrs1, F1, r1, passedra1, passeddec1, scanned_ra, scanned_dec,scanned_pix,scanned_time,countwhile1,kk1,tempdis1,c1,y1,pointslabels1,delay,merge,t_update,met, changepix,change_is_here,scanned_pix_s,z,t0,bulk1, bulkra1, bulkdec1)
            else:
                phis1, thetas1, timearrs1, kks, scanned_ra1, scanned_dec1,scanned_pix1, scanned_time1,passedra1, passeddec1,is_here,countwhile1,kk1,tempdis1,c1,y,change_is_here,scanned_pix_s,event_ipix =scan2tel2(pointsra1, pointsdec1, tele1, tchange, rachange, decchange, ii, timearr, theta, phi, tottime, j, event_ipix, hpx1, nside, minrap1, mindecp1, kks, phis1, thetas1, timearrs1, F1, r1, passedra1, passeddec1, scanned_ra1, scanned_dec1,scanned_pix1,scanned_time1,countwhile1,kk1,tempdis1,c1,y1,pointslabels1,delay,merge,t_update,met, changepix,change_is_here,scanned_pix_s,z,t0,bulk1, bulkra1, bulkdec1)



            if met==2:
                scanned_pix = []
                scanned_pix.extend(scanned_pix1)
                scanned_pix.extend(scanned_pix2)
            if is_kmean_scanned(pointsra1, pointsdec1, y1, pointslabels1, scanned_pix, nside):
                if timearrs1[-1]>t0:
                    if len(set(labels1)) > 1:
                        c1=360
                        y1 = y1 + 1
                        if y1 > len(set(labels1)) - 1:
                            y1 = 0
                else:
                    timearrs1 = np.append(timearrs1, t_update[-1])
                    phis1 = np.append(phis1, phis1[-1])
                    thetas1 = np.append(thetas1, thetas1[-1])
            if is_here:
                is_here = False
                if met ==0 or met==1 :
                    flag0 = True
                    scanned_ra_s = scanned_ra[-1]
                    scanned_ra = scanned_ra[:-1]
                    scanned_dec_s = scanned_dec[-1]
                    scanned_dec = scanned_dec[:-1]
                    t_scan = scanned_time[-1]
                    scanned_time = scanned_time[:-1]
                    timearrs1 = np.append(timearrs1, 100000)

                else:
                    flag0=True
                    scanned_ra_s = scanned_ra1[-1]
                    scanned_ra1 = scanned_ra1[:-1]
                    scanned_dec_s = scanned_dec1[-1]
                    scanned_dec1 = scanned_dec1[:-1]
                    t_scan = scanned_time1[-1]
                    scanned_time1 = scanned_time1[:-1]
                    timearrs1 = np.append(timearrs1, 100000)

        else:
            if t_update != [] and uflag2<len(t_update):
                while (timearrs2[-1] >= t_update[uflag2]) :
                    uflag2 = uflag2 + 1
                    hpx2, bulk2, bulkra2, bulkdec2, pointsra2, pointsdec2, pointslabels2,labels2 = hpxs[uflag2], bulks[uflag2], bulkras[uflag2], bulkdecs[uflag2], pointsras[uflag2], pointsdecs[uflag2], pointslabelss[uflag2],labelss[uflag2]
                    if uflag2 == len(t_update):
                        break


            if met!=2:
                phis2, thetas2, timearrs2, kks, scanned_ra, scanned_dec, scanned_pix, scanned_time, passedra2, passeddec2, is_here, countwhile2, kk2, tempdis2, c2, y,change_is_here,scanned_pix_s,event_ipix = scan2tel2(pointsra2, pointsdec2, tele2, tchange, rachange,
                                                                                                                                                                                                     decchange, gg, timearr, theta, phi, tottime, jg,
                                                                                                                                                                                                     event_ipix, hpx2, nside, minrap2, mindecp2, kks,
                                                                                                                                                                                                     phis2, thetas2, timearrs2, F2, r2, passedra2,
                                                                                                                                                                                                     passeddec2, scanned_ra, scanned_dec, scanned_pix,
                                                                                                                                                                                                     scanned_time, countwhile2, kk2, tempdis2, c2,
                                                                                                                                                                                                     y2,pointslabels2,delay, merge,
                                                                                                                                                                                                     t_update,met, changepix,change_is_here,scanned_pix_s,z,t0,bulk2, bulkra2, bulkdec2)
            else:
                phis2, thetas2, timearrs2, kks, scanned_ra2, scanned_dec2, scanned_pix2, scanned_time2, passedra2, passeddec2, is_here, countwhile2, kk2, tempdis2, c2, y,change_is_here,scanned_pix_s,event_ipix = scan2tel2(pointsra2, pointsdec2, tele2, tchange, rachange,
                                                                                                                                                                                                        decchange, gg, timearr, theta, phi, tottime, jg,
                                                                                                                                                                                                        event_ipix, hpx2, nside, minrap2, mindecp2, kks,
                                                                                                                                                                                                        phis2, thetas2, timearrs2, F2, r2, passedra2,
                                                                                                                                                                                                        passeddec2, scanned_ra2, scanned_dec2,
                                                                                                                                                                                                        scanned_pix2, scanned_time2, countwhile2, kk2,
                                                                                                                                                                                                        tempdis2, c2,  y2,  pointslabels2,
                                                                                                                                                                                                        delay, merge, t_update,met, changepix,change_is_here,scanned_pix_s,z,t0,bulk2, bulkra2, bulkdec2)


            if met == 2:

                scanned_pix = []
                scanned_pix.extend(scanned_pix1)
                scanned_pix.extend(scanned_pix2)
            if is_kmean_scanned(pointsra2, pointsdec2, y2, pointslabels2, scanned_pix, nside):
                if timearrs2[-1] > t0:
                    if len(set(labels2)) > 1:
                        c2 = 360
                        y2 = y2 + 1
                        if y2 > len(set(labels2)) - 1:
                            y2 = 0
                else:
                    timearrs2 = np.append(timearrs2, t_update[-1])
                    phis2 = np.append(phis2, phis2[-1])
                    thetas2 = np.append(thetas2, thetas2[-1])

            if is_here:

                who_found = tele2.name


                return phis1, thetas1, timearrs1, phis2, thetas2, timearrs2, scanned_ra, scanned_dec,scanned_pix,scanned_ra1, scanned_dec1,scanned_pix1,scanned_ra2, scanned_dec2,scanned_pix2,scanned_time,scanned_time1,scanned_time2, passedra1, passeddec1, passedra2, passeddec2, minrap1, mindecp1, minrap2, mindecp2,hpxs,bulks,bulkras,bulkdecs,labelss,event_ipix,turn_points_ra,turn_points_dec,who_found,t_scan,scanned_pix_s, scanned_ra_s, scanned_dec_s,flag0,call
        if countwhile1+countwhile2>100:
            who_found=0
            flag0=False

            return phis1, thetas1, timearrs1, phis2, thetas2, timearrs2,scanned_ra, scanned_dec,scanned_pix,scanned_ra1, scanned_dec1,scanned_pix1,scanned_ra2, scanned_dec2,scanned_pix2,scanned_time,scanned_time1,scanned_time2, passedra1, passeddec1, passedra2, passeddec2,minrap1, mindecp1, minrap2, mindecp2,hpxs,bulks,bulkras,bulkdecs,labelss,event_ipix,turn_points_ra,turn_points_dec,who_found,t_scan,scanned_pix_s, scanned_ra_s, scanned_dec_s,flag0,call