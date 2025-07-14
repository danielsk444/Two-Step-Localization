import healpy as hp
from random import random
from Updates import Updates
from timearrs_trunc import timearrs_trunc
from calc_ra_dec import calc_ra_dec
import cartopy.crs as ccrs
from datetime import datetime
from matplotlib.ticker import  FuncFormatter
import numpy as np
from matplotlib import cm, colors
from matplotlib import gridspec
from scan2telN import scan2telN
import matplotlib.pyplot as plt
from kmeans import kmeans
from plant_event import plant_event
from randy import randy
from calc_ipix_max import calc_ipix_max
from where_to import where_to
from calc_nside import calc_nside
from calc_sky_area_per_pix import calc_sky_area_per_pix
from read_map import read_map
from labelmax_maker import labelmax_maker
from recordings import recordings
from recordingsXL import recordingsXL
from update_generator import update_generator

from fixarrays00 import fixarrays00
def scopes100(k):
    fits_files = ['S230520ae.fits.gz,0', 'S230520ae.fits.gz,1','S230529ay.fits.gz,0','S230529ay.fits.gz,1', 'S230601bf.fits.gz,0', 'S230601bf.fits.gz,1','S230605o.fits.gz,0','S230605o.fits.gz,1', 'S230606d.fits.gz,0', 'S230606d.fits.gz,1','S230608as.fits.gz,1', 'S230609u.fits.gz,1','S230708t.gz,0','S230708t.gz,1','S230708t.gz,2', 'S230708z.gz,0', 'S230708z.gz,1','S230709bi.gz,0','S230709bi.gz,1', 'S230723ac.gz,0', 'S230723ac.gz,1','S230726a.gz,0','S230726a.gz,1', 'S230729z.gz,0', 'S230729z.gz,1','S230731an.gz,0','S230731an.gz,1','S230731an.gz,2', 'S230802aq.gz,0', 'S230802aq.gz,1','S230805x.gz,0','S230805x.gz,1','S230806ak.gz,0', 'S230806ak.gz,1','S230807f.gz,0','S230807f.gz,1','S230807f.gz,2', 'S230814ah.gz,0', 'S230814ah.gz,1', 'S230814ah.gz,2','S230814r.gz,0','S230814r.gz,1', 'S230819ax.gz,0', 'S230819ax.gz,1', 'S230819ax.gz,2','S230820bq.gz,0','S230820bq.gz,1', 'S230822bm.gz,0', 'S230822bm.gz,1','S230824r.gz,0','S230824r.gz,1','S230824r.gz,2', 'S230825k.gz,0', 'S230825k.gz,1','S230831e.gz,0','S230831e.gz,1','S230831e.gz,2', 'S230904n.gz,0', 'S230904n.gz,1', 'S230904n.gz,2']


    timesarr1 = []
    timesarr2 = []
    file_name = fits_files[int(59*random())]
    print(file_name)
    hpx = hp.fitsfunc.read_map(file_name)
    npix = 1
    sky_area = 1
    nside = 1
    ipix = 1
    theta, phi = 1, 1
    ra, dec = 1, 1
    i = np.flipud(np.argsort(hpx))
    sorted_credible_levels = np.cumsum(hpx[i])
    credible_levels = np.empty_like(sorted_credible_levels)
    credible_levels_ipix = 1
    prob_dens_ipix_max = 1
    credible_levels_ipix_09 = 1
    r = 1
    xyz = 1
    ipix_disc = 1
    prob_circ = 0.1
    ipix_poly = 1
    prob_poly = 0.1
    cum_prob_dens = 0
    color_mapa = 'BrBG'
    cb_label = 'Time(sec)'
    ii = 0
    gg = 0
    n = 20
    timearr = np.zeros(n)
    theta = np.zeros(n)
    phi = np.zeros(n)
    tottime = 0
    j = -1
    jg=-1
    a= 50+3*random()
    b=40+3*random()
    c=20+3*random()
    d=5+3*random()
    t_pre_merge=[a, b, c, d]
    a = random()

    if a < 0.33:
        run=3
    elif 0.333 < a < 0.67:
        run=4
    else:
        run=5

    event_ipix=0

    # Defining telescopes' Classes
    # type 1
    class tele_deg:
        # Setting initial values
        def __init__(self, name=" ", az_rate=-1, az_c=1, lat_rate=-1, lat_c=1, FOV=1):
            # Here we define the parameters of type 1 telescope
            self.name = name
            self.az_rate = az_rate
            self.az_c = az_c
            self.lat_rate = lat_rate
            self.lat_c = lat_c
            self.FOV = FOV

        # Creating Getting and Setting Methods
        def get_name(self):
            return self.name

        def set_name(self, name):
            self.name = name

        def get_az_rate(self):
            return self.az_rate

        def set_az_rate(self, az_rate):
            self.az_rate = az_rate

        def get_az_c(self):
            return self.az_c

        def set_az_c(self, az_c):
            self.az_c = az_c

        def get_lat_rate(self):
            return self.lat_rate

        def set_lat_rate(self, lat_rate):
            self.lat_rate = lat_rate

        def get_lat_c(self):
            return self.lat_c

        def set_lat_c(self, lat_c):
            self.lat_c = lat_c

        def get_FOV(self):
            return self.FOV

        def set_FOV(self, FOV):
            self.FOV = FOV

        # Defining a calculation method for the motion time
        def time(self, phi, theta, phiI, thetaI):
            if phi == phiI and theta == thetaI:
                flag = 0
                time = 0
            if phi == phiI and theta != thetaI:
                flag = 1
                time = self.lat_rate * abs(theta - thetaI) + self.lat_c
            if (phi != phiI and theta == thetaI):
                flag = 2
                time = self.az_rate * abs(phi - phiI) + self.az_c
            if (phi != phiI and theta != thetaI and abs(phi - phiI) != 180):
                flag = 3
                time = max(self.az_rate * abs(phi - phiI) + self.az_c, self.lat_rate * abs(theta - thetaI) + self.lat_c)

            return time, flag

        def place(self, time, phiI, thetaI, flag, phiF, thetaF):
            bt = 1
            bp = 1
            theta = 0
            phi = 0
            if thetaF < thetaI:
                bt = -1
            if phiF < phiI:
                bp = -1
            if flag == 0:
                theta = thetaI
                phi = phiI
            if flag == 1:
                theta = thetaI + bt * ((time - self.lat_c) / self.lat_rate)
                phi = phiI
            if flag == 2:
                theta = thetaI
                phi = phiI + bp * ((time - self.az_c) / self.az_rate)
            if flag == 3:
                if time < min(self.az_rate * abs(phiF - phiI) + self.az_c, self.lat_rate * abs(thetaF - thetaI) + self.lat_c):
                    theta = thetaI + bt * ((time - self.lat_c) / self.lat_rate)
                    phi = phiI + bp * ((time - self.az_c) / self.az_rate)
                elif self.az_rate * abs(phiF - phiI) + self.az_c > self.lat_rate * abs(thetaF - thetaI) + self.lat_c:
                    theta = thetaF
                    phi = phiI + bp * ((time - self.az_c) / self.az_rate)
                else:
                    theta = thetaI + bt * ((time - self.lat_c) / self.lat_rate)
                    phi = phiF

            return phi, theta

        # type 2


    class tele_acc:  # type 2: acceleration + maximum velocity
        # Setting initial values
        def __init__(self, name="", acc=-1, max_vel=-1, FOV=2):
            # Here we define the parameters of type 2 telescope
            self.name = name
            self.acc = acc
            self.max_vel = max_vel
            self.FOV = FOV

        # Setting and Getting Methods
        def get_name(self):
            return self.name

        def set_name(self, name):
            self.name = name

        def get_acc(self):
            return self.acc

        def set_acc(self, acc):
            self.acc = acc

        def get_max_vel(self):
            return self.max_vel

        def set_max_vel(self, max_vel):
            self.max_vel = max_vel

        def get_FOV(self):
            return self.FOV

        def set_FOV(self, FOV):
            self.FOV = FOV

        # Calculation Method for the motion time
        def time(self, phi, theta, phiI, thetaI):
            flago = 0
            timetheta, timephi = 0, 0
            sign = 1
            time2 = [0, 0]
            flag2 = False
            flago2=[0, 0]
            thetas = [thetaI, theta]
            t_acc = self.max_vel / self.acc
            xc = 2 * self.acc * t_acc ** 2
            if phi == phiI and theta == thetaI:
                flag = 0
                time = 0
            if phi == phiI and theta != thetaI:
                if abs(theta - thetaI) <= xc:
                    flag = 1
                    time = 2 * np.sqrt(abs(theta - thetaI) / (2 * self.acc))
                else:
                    flag = 2
                    time = 2 * t_acc + (abs(theta - thetaI) - xc) / self.max_vel

            if phi != phiI and theta == thetaI:
                if abs(phi - phiI) < 180:
                    if abs(phi - phiI) <= xc:
                        flag = 3
                        time1 = 2 * np.sqrt(abs(phi - phiI) / (2 * self.acc))
                    else:
                        flag = 4
                        time1 = 2 * t_acc + (abs(phi - phiI) - xc) / self.max_vel
                else:
                    if 360 - abs(phi - phiI) <= xc:
                        flag = 3
                        time1 = 2 * np.sqrt((360 - abs(phi - phiI)) / (2 * self.acc))
                    else:
                        flag = 4
                        time1 = 2 * t_acc + ((360 - abs(phi - phiI)) - xc) / self.max_vel
            if phi != phiI and theta != thetaI:
                if abs(theta - thetaI) <= xc:
                    flag = 5
                    timetheta = 2 * np.sqrt(abs(theta - thetaI) / (2 * self.acc))
                else:
                    flag = 6
                    timetheta = 2 * t_acc + (abs(theta - thetaI) - xc) / self.max_vel
                if abs(phi - phiI) < 180:
                    if abs(phi - phiI) <= xc:
                        flago = 1
                        timephi = 2 * np.sqrt(abs(phi - phiI) / (2 * self.acc))
                    else:
                        flago = 2
                        timephi = 2 * t_acc + (abs(phi - phiI) - xc) / self.max_vel
                else:
                    if (360 - abs(phi - phiI)) <= xc:
                        flago = 1
                        timephi = 2 * np.sqrt((360 - abs(phi - phiI)) / (2 * self.acc))
                    else:
                        flago = 2
                        timephi = 2 * t_acc + ((360 - abs(phi - phiI)) - xc) / self.max_vel
                time1 = max(timetheta, timephi)
            if phi != phiI:
                if (thetaI + theta) < 0:
                    sign = -1
                for i in range(2):
                    if abs(thetas[i] - sign * 90) <= xc:
                        time2[i] = 2 * np.sqrt(abs(thetas[i] - sign * 90) / (2 * self.acc))
                        flago2[i]=False
                    else:
                        time2[i] = 2 * t_acc + (abs(thetas[i] - sign * 90) - xc) / self.max_vel
                        flago2[i]=True
                if sum(time2) < time1:
                    flag2 = True
                    time = sum(time2)
                else:
                    time = time1

            return time, flag, flago,flago2, flag2, timetheta, timephi, sign, time2

        def place(self, time, phiI, thetaI, flag, flago, flag2,flago2, phiF, thetaF, timetheta, timephi, sign, time2):
            t_acc = self.max_vel / self.acc
            xc = 2 * self.acc * t_acc ** 2
            bt = 1
            bp = 1
            theta = 0
            phi = 0
            if thetaF < thetaI:
                bt = -1
            if phiF < phiI:
                bp = -1
            if flag == 0:
                theta = thetaI
                phi = phiI
            elif flag == 1:
                theta = thetaI + bt * (self.acc * time ** 2) / 2
                phi = phiI
            elif flag == 2:
                theta = thetaI + bt * ((time - 2 * t_acc) * self.max_vel + xc)
                phi = phiI
            if flag2:
                if time < time2[0]:

                    if flago2[0]:
                        theta = thetaI + sign * ((time - 2 * t_acc) * self.max_vel + xc)
                        phi = phiI
                    else:
                        theta = thetaI + sign * (self.acc * time ** 2) / 2
                        phi = phiI
                    if abs(theta) > 90:
                        theta = sign * 90

                else:
                    if flago2[1]:
                        theta = sign * 90 - sign * (((time-time2[0] )- 2 * t_acc) * self.max_vel + xc)
                        phi = phiF
                    else:
                        theta = sign * 90 - sign * (self.acc * (time-time2[0] ) ** 2) / 2
                        phi = phiF

            else:
                if flag == 3:
                    if abs(phiF - phiI) < 180:
                        phi = phiI + bp * ((self.acc * time ** 2) / 2)
                        theta = thetaI
                    else:
                        if (0 < phiI - bp * ((self.acc * time ** 2) / 2) < 360):
                            phi = phiI - bp * ((self.acc * time ** 2) / 2)
                            theta = thetaI
                        elif (0 > phiI - bp * ((self.acc * time ** 2) / 2)):
                            phi = 360 + (phiI - bp * ((self.acc * time ** 2) / 2))
                            theta = thetaI
                        else:
                            phi = phiI - bp * ((self.acc * time ** 2) / 2) - 360
                            theta = thetaI
                if flag == 4:
                    if abs(phiF - phiI) < 180:
                        phi = phiI + bp * ((time - 2 * t_acc) * self.max_vel + xc)
                        theta = thetaI
                    else:
                        if (0 < phiI - bp * ((time - 2 * t_acc) * self.max_vel + xc) < 360):
                            phi = phiI - bp * ((time - 2 * t_acc) * self.max_vel + xc)
                            theta = thetaI
                        elif (0 > phiI - bp * ((time - 2 * t_acc) * self.max_vel + xc)):
                            phi = 360 + (phiI - bp * ((time - 2 * t_acc) * self.max_vel + xc))
                        else:
                            phi = phiI - bp * ((time - 2 * t_acc) * self.max_vel + xc) - 360
                if flag == 5 and flago == 1:
                    if time < min(timetheta, timephi):
                        if abs(phiF - phiI) < 180:
                            phi = phiI + bp * ((self.acc * time ** 2) / 2)
                            theta = thetaI + bt * (self.acc * time ** 2) / 2
                        else:
                            if (0 < phiI - bp * ((self.acc * time ** 2) / 2) < 360):
                                phi = phiI - bp * ((self.acc * time ** 2) / 2)
                                theta = thetaI + bt * (self.acc * time ** 2) / 2
                            elif (0 > phiI - bp * ((self.acc * time ** 2) / 2)):
                                phi = 360 + (phiI - bp * ((self.acc * time ** 2) / 2))
                                theta = thetaI + bt * (self.acc * time ** 2) / 2
                            else:
                                phi = phiI - bp * ((self.acc * time ** 2) / 2) - 360
                                theta = thetaI + bt * (self.acc * time ** 2) / 2
                    elif timetheta > timephi:
                        phi = phiF
                        theta = thetaI + bt * (self.acc * time ** 2) / 2
                    else:
                        if abs(phiF - phiI) < 180:
                            theta = thetaF
                            phi = phiI + bp * ((self.acc * time ** 2) / 2)
                        else:
                            if (0 < phiI - bp * ((self.acc * time ** 2) / 2) < 360):
                                theta = thetaF
                                phi = phiI - bp * ((self.acc * time ** 2) / 2)
                            elif (0 > phiI - bp * ((self.acc * time ** 2) / 2)):
                                theta = thetaF
                                phi = 360 + (phiI - bp * ((self.acc * time ** 2) / 2))
                            else:
                                theta = thetaF
                                phi = phiI - bp * ((self.acc * time ** 2) / 2) - 360
                if flag == 5 and flago == 2:
                    if time < timetheta:
                        if abs(phiF - phiI) < 180:
                            phi = phiI + bp * ((self.acc * time ** 2) / 2)
                            theta = thetaI + bt * (self.acc * time ** 2) / 2
                        else:
                            if (0 < phiI - bp * ((self.acc * time ** 2) / 2) < 360):
                                phi = phiI - bp * ((self.acc * time ** 2) / 2)
                                theta = thetaI + bt * (self.acc * time ** 2) / 2
                            elif (0 > phiI - bp * ((self.acc * time ** 2) / 2)):
                                phi = 360 + (phiI - bp * ((self.acc * time ** 2) / 2))
                                theta = thetaI + bt * (self.acc * time ** 2) / 2
                            else:
                                phi = phiI - bp * ((self.acc * time ** 2) / 2) - 360
                                theta = thetaI + bt * (self.acc * time ** 2) / 2
                    elif timetheta < time < 2 * t_acc:
                        if abs(phiF - phiI) < 180:
                            phi = phiI + bp * ((self.acc * time ** 2) / 2)
                            theta = thetaF
                        else:
                            if (0 < phiI - bp * ((self.acc * time ** 2) / 2) < 360):
                                phi = phiI - bp * ((self.acc * time ** 2) / 2)
                                theta = thetaF
                            elif (0 > phiI - bp * ((self.acc * time ** 2) / 2)):
                                phi = 360 + (phiI - bp * ((self.acc * time ** 2) / 2))
                                theta = thetaF
                            else:
                                phi = phiI - bp * ((self.acc * time ** 2) / 2) - 360
                                theta = thetaF
                    else:
                        if abs(phiF - phiI) < 180:
                            phi = phiI + bp * ((time - 2 * t_acc) * self.max_vel + xc)
                            theta = thetaF
                        else:
                            if (0 < phiI - bp * ((time - 2 * t_acc) * self.max_vel + xc) < 360):
                                phi = phiI - bp * ((time - 2 * t_acc) * self.max_vel + xc)
                                theta = thetaF
                            elif (0 > phiI - bp * ((time - 2 * t_acc) * self.max_vel + xc)):
                                phi = 360 + (phiI - bp * ((time - 2 * t_acc) * self.max_vel + xc))
                                theta = thetaF
                            else:
                                phi = phiI - bp * ((time - 2 * t_acc) * self.max_vel + xc) - 360
                                theta = thetaF
                if flag == 6 and flago == 1:
                    if time < timephi:
                        if abs(phiF - phiI) < 180:
                            phi = phiI + bp * ((self.acc * time ** 2) / 2)
                            theta = thetaI + bt * (self.acc * time ** 2) / 2
                        else:
                            if (0 < phiI + bp * ((self.acc * time ** 2) / 2) < 360):
                                phi = phiI - bp * ((self.acc * time ** 2) / 2)
                                theta = thetaI + bt * (self.acc * time ** 2) / 2
                            elif (0 > phiI + bp * ((self.acc * time ** 2) / 2)):
                                phi = 360 + (phiI - bp * ((self.acc * time ** 2) / 2))
                                theta = thetaI + bt * (self.acc * time ** 2) / 2
                            else:
                                phi = phiI - bp * ((self.acc * time ** 2) / 2) - 360
                                theta = thetaI + bt * (self.acc * time ** 2) / 2
                    elif timephi < time < 2 * t_acc:
                        theta = thetaI + bt * (self.acc * time ** 2) / 2
                        phi = phiF
                    else:
                        theta = thetaI + bt * ((time - 2 * t_acc) * self.max_vel + xc)
                        phi = phiF
                if flag == 6 and flago == 2:

                    if time < min(timetheta, timephi):
                        if abs(phiF - phiI) < 180:
                            phi = phiI + bp * ((time - 2 * t_acc) * self.max_vel + xc)
                            theta = thetaI + bt * ((time - 2 * t_acc) * self.max_vel + xc)
                        else:
                            if (0 < phiI - bp * ((time - 2 * t_acc) * self.max_vel + xc) < 360):
                                phi = phiI - bp * ((time - 2 * t_acc) * self.max_vel + xc)
                                theta = thetaI + bt * ((time - 2 * t_acc) * self.max_vel + xc)
                            elif (0 > phiI - bp * ((time - 2 * t_acc) * self.max_vel + xc)):
                                phi = 360 + (phiI - bp * ((time - 2 * t_acc) * self.max_vel + xc))
                                theta = thetaI + bt * ((time - 2 * t_acc) * self.max_vel + xc)
                            else:
                                phi = phiI - bp * ((time - 2 * t_acc) * self.max_vel + xc) - 360
                                theta = thetaI + bt * ((time - 2 * t_acc) * self.max_vel + xc)
                    elif timetheta > timephi:
                        phi = phiF
                        theta = thetaI + bt * ((time - 2 * t_acc) * self.max_vel + xc)

                    else:
                        if abs(phiF - phiI) < 180:
                            phi = phiI + bp * ((time - 2 * t_acc) * self.max_vel + xc)
                            theta = thetaF
                        else:
                            if (0 < phiI - bp * ((time - 2 * t_acc) * self.max_vel + xc) < 360):
                                phi = phiI - bp * ((time - 2 * t_acc) * self.max_vel + xc)
                                theta = thetaF
                            elif (0 > phiI - bp * ((time - 2 * t_acc) * self.max_vel + xc)):
                                phi = 360 + (phiI - bp * ((time - 2 * t_acc) * self.max_vel + xc))
                                theta = thetaF
                            else:
                                phi = phiI - bp * ((time - 2 * t_acc) * self.max_vel + xc) - 360
                                theta = thetaF
            return phi, theta


    # Defining Default Telescopes
    def lsst():
        tele_lsst = tele_deg()
        tele_lsst.set_name("LSST")
        tele_lsst.set_az_rate(0.66)
        tele_lsst.set_az_c(-2)
        tele_lsst.set_lat_rate(0.57)
        tele_lsst.set_lat_c(3)
        tele_lsst.set_FOV(9.6)
        return tele_lsst


    def  ztf():
        tele_ztf = tele_acc()
        tele_ztf.set_name("ZTF")
        tele_ztf.set_acc(0.5)
        tele_ztf.set_max_vel(3)
        tele_ztf.set_FOV(47)
        return tele_ztf


    def sw():
        tele_sw = tele_acc()
        tele_sw.set_name("Swope")
        tele_sw.set_acc(5)
        tele_sw.set_max_vel(2)
        tele_sw.set_FOV(7)
        return tele_sw


    def ULTRASAT():
        tele_US = tele_acc()
        tele_US.set_name("ULTRASAT")
        tele_US.set_acc(5)
        tele_US.set_max_vel(0.5)
        tele_US.set_FOV(204)
        return tele_US


    def BIG():
        tele_BIG = tele_acc()
        tele_BIG.set_name("BIG")
        tele_BIG.set_acc(0.5)
        tele_BIG.set_max_vel(3)
        tele_BIG.set_FOV(1000)

        return tele_BIG


    hpx = read_map(file_name)

    npix, sky_area = calc_sky_area_per_pix(hpx)
    nside = calc_nside(npix)

    phiI, thetaI, stretch, tchange,  phiI2, thetaI2 = randy()

    t_update, area_update, hpx, bulk, bulkra, bulkdec,bulkpix,A90,thetaLVK,phiLVK,psiLVK,ILVK,SNRs,dis,D,good_area,SNRs_filtered,t_pre_merge_filtered,A90_filtered =update_generator(run, t_pre_merge,hpx)
    if not good_area:

        return

    labels, labels1, nkmeans, centroids = kmeans(bulkra, bulkdec)

    ipix_max, prob_dens_ipix_max = calc_ipix_max(hpx)
    rachange, decchange = calc_ra_dec(ipix_max, nside)

    for z in range(5):

        if z == 0:
            tele1 = ULTRASAT()
        else:
           
            tele1 = BIG()
            tele1.set_FOV([100, 200, 400, 1000][z - 1])

        tele2 = sw()
        tele_times=[]
        track_times=[]

        who_found_arr = []
        pointsra, pointsdec, pointsra1, pointsdec1, nra, ndec, pointslabels = where_to(hpx, bulkra, bulkdec, min(tele1.FOV, tele2.FOV), nside, labels, centroids, bulkpix)

        labelmax1, bulkramax1, bulkdecmax1, labelmax2, bulkramax2, bulkdecmax2, minra1, minra2, mindec1, mindec2=labelmax_maker(bulk,pointsra,pointsdec, pointslabels ,labels,nkmeans, tele1,tele2, phiI, thetaI, phiI2, thetaI2)
        starting_t=t_pre_merge[0]-t_pre_merge_filtered[0]

        hpxs, bulks, bulkras, bulkdecs, pointsras, pointsdecs, pointslabelss,labelss=Updates(nside,np.sqrt(tele2.FOV / np.pi), area_update, hpx, labels, bulk, bulkra, bulkdec, pointsra, pointsdec, pointslabels)
        if z == 0:
            event_idx, event_ipix = plant_event(bulks[-1], bulkras[-1], bulkdecs[-1], nside)

        for met in range(3):

            phis1, thetas1, timearrs1, phis2, thetas2, timearrs2, scanned_ra, scanned_dec,scanned_pix,scanned_ra1, scanned_dec1,scanned_pix1,scanned_ra2, scanned_dec2,scanned_pix2,scanned_time,scanned_time1,scanned_time2, passedra1, passeddec1, passedra2, passeddec2, minrap1, mindecp1, minrap2, mindecp2,hpxs,bulks,bulkras,bulkdecs,labelss,event_ipix,turn_points_ra,turn_points_dec,who_found,t_scan,scanned_pix_s, scanned_ra_s, scanned_dec_s,flag0,call=scan2telN(pointsras, pointsdecs, tele1, tele2, phiI, thetaI, phiI2, thetaI2, minra1, mindec1, minra2, mindec2, rachange, decchange, ii, gg, timearr, theta, phi, tottime, j, jg, labelss, nkmeans,event_ipix,bulks,bulkras,bulkdecs,hpxs,nside,pointslabelss,labelmax1,labelmax2,t_update,area_update,file_name,met,starting_t,z,t_pre_merge[0])
            if timearrs1[-1] == 100000:
                timearrs1 = timearrs1[:-1]
            rax, decx = calc_ra_dec(event_ipix, nside)
            phis1, thetas1, timearrs1=fixarrays00(phis1, thetas1, timearrs1)
            phis2, thetas2, timearrs2=fixarrays00(phis2, thetas2, timearrs2)

            if flag0 :
                who_found=tele1.name
                if met!=0 and timearrs2[-1]<timearrs1[-1]:
                    who_found = tele2.name

                if met==0 and not call:
                    who_found = tele2.name

                if met==0 or met==1:

                    scanned_time.append(t_scan)
                    if isinstance(scanned_pix_s, int):
                        scanned_pix_s = [scanned_pix_s]  # Wrap the integer in a list

                    scanned_pix.extend(scanned_pix_s)
                    scanned_ra.append(scanned_ra_s)
                    scanned_dec.append(scanned_dec_s)
                else:

                    scanned_time1.append(t_scan)
                    if isinstance(scanned_pix_s, int):
                        scanned_pix_s = [scanned_pix_s]  # Wrap the integer in a list

                    scanned_pix1.extend(scanned_pix_s)
                    scanned_ra1.append(scanned_ra_s)
                    scanned_dec1.append(scanned_dec_s)


            if who_found=='Swope' and  timearrs1[-1]>timearrs2[-1]:
                if met!=2:
                    scanned_ra, scanned_dec, passedra1, passeddec1, timearrs1, phis1, thetas1,scanned_time=timearrs_trunc(timearrs1,timearrs2,phis1,thetas1,passedra1,passeddec1 , nside,scanned_ra,scanned_dec,scanned_time)
                else:
                    scanned_ra1, scanned_dec1, passedra1, passeddec1, timearrs1, phis1, thetas1,scanned_time1=timearrs_trunc(timearrs1,timearrs2,phis1,thetas1,passedra1,passeddec1 , nside,scanned_ra1,scanned_dec1,scanned_time1)

            cmaps = ["Greens", "Blues" , "Purples","pink"]

            # Generate modified colormaps that start at the midpoint
            half_cmaps = {name: cm.colors.ListedColormap(cm.get_cmap(name)(np.linspace(0.5, 1, 128))) for name in cmaps}

            # Create main figure with GridSpec for arranging sub-elements
            fig = plt.figure(figsize=(10, 8))
            gs = gridspec.GridSpec(4, 1, height_ratios=[20, 0.5, 0.5, 1], figure=fig)  # Main plot + colorbars

            # Choose projection type here (e.g., Robinson, PlateCarree, etc.)
            projection = ccrs.Robinson()  # Change projection as needed
            ax_main = fig.add_subplot(gs[0], projection=projection)
            ax_main.set_global()  # Set to global view

            # Remove all features like land, ocean, coastline, borders
            # Just showing the map's shape
            ax_main.set_facecolor('lightgrey')  # Background color for the map
            ax_main.gridlines(draw_labels=True)  # Optional: add gridlines for better reference

            # Normalize time data for consistent colormap scaling
            norm = colors.Normalize(vmin=min(min(timearrs1), min(timearrs2)), vmax=max(max(timearrs1), max(timearrs2)))
            if len(set(labelss[0]))>1:
                for i in range(len(set(labelss[0]))):
                    for j in range(len(labelss[0])):
                        if labelss[0][j] == i:

                            # Add text with coordinate transformation
                            ax_main.text(
                                bulkras[0][j], bulkdecs[0][j], f"Seach area {i + 1}",
                                fontsize=6.5, color='black', transform=ccrs.PlateCarree()
                            )
                            break

            scatter_plots = []
            for i in range(len(labelss)):
                cmap = half_cmaps[cmaps[i % len(cmaps)]]  # Use modified colormap
                scatter = ax_main.scatter(
                    bulkras[i], bulkdecs[i],
                    c=bulks[i],
                    cmap=cmap,
                    transform=ccrs.PlateCarree(),  # Use PlateCarree projection for latitude/longitude
                    label=f'90% prob. area Update-{i + 1}',
                )
                scatter_plots.append(scatter)

            # Plot scanned areas
            if scanned_ra:
                for i in range(len(scanned_ra)):
                    ax_main.plot(
                        scanned_ra[i], scanned_dec[i], ',',
                        color=(scanned_time[i] / max(scanned_time), 0.05, 0.05),
                        alpha=0.65,
                        transform=ccrs.PlateCarree()
                    )

            if scanned_ra1:
                for i in range(len(scanned_ra1)):
                    ax_main.plot(
                        scanned_ra1[i], scanned_dec1[i], ',',
                        color=(scanned_time1[i] / max(scanned_time1), 0.05, 0.05),
                        alpha=0.65,
                        transform=ccrs.PlateCarree()
                    )

            if scanned_ra2:
                for i in range(len(scanned_ra2)):
                    ax_main.plot(
                        scanned_ra2[i], scanned_dec2[i], ',',
                        color=(scanned_time2[i] / max(scanned_time2), 0.05, 0.05),
                        alpha=0.65,
                        transform=ccrs.PlateCarree()
                    )

            # Event markers
            ax_main.plot(rax, decx, 'X', color=  'yellow', markersize=11,label='Event', transform=ccrs.PlateCarree())
            ax_main.plot(phiI, thetaI, 'rH', markersize=10, label='Starting point Aux. tel.', transform=ccrs.PlateCarree())
            ax_main.plot(phiI2, thetaI2, 'H', color='orange', markersize=10, label='Starting point Main tel.', transform=ccrs.PlateCarree())

            # Various plotted elements
            if len(turn_points_ra) > 0:
                ax_main.plot(turn_points_ra, turn_points_dec, 'r*', markersize=4.5, label='Update redirection points', transform=ccrs.PlateCarree())

            ax_main.plot(pointsra, pointsdec, 'c*', markersize=1.5,  alpha=0.5,label='Stopping points', transform=ccrs.PlateCarree())
            ax_main.plot(passedra1, passeddec1, 'mo', markersize=1.5,  alpha=0.5, label='Passed checkpoints  Aux. tel.', transform=ccrs.PlateCarree())
            ax_main.plot(passedra2, passeddec2, 'bo', markersize=1.5,  alpha=0.5, label='Passed checkpoints Main tel.', transform=ccrs.PlateCarree())

            # Time-based scatter plots
            scatter1 = ax_main.scatter(phis1, thetas1, c=timearrs1, cmap="copper", norm=norm, label='Aux. tel. course', transform=ccrs.PlateCarree())
            scatter2 = ax_main.scatter(phis2, thetas2, c=timearrs2, marker='x', cmap="copper", norm=norm, label='Main tel. course', transform=ccrs.PlateCarree())

            # Main colorbar for time data
            cbar_main = fig.colorbar(scatter1, ax=ax_main, label="Time (sec)", shrink=0.8)

            # Closest starting points
            ax_main.plot(minrap1, mindecp1, 'r^', label='Closest to  Aux. tel starting point ', transform=ccrs.PlateCarree())
            ax_main.plot(minrap2, mindecp2, '^', color='orange', label='Closest to   Main tel. starting point ', transform=ccrs.PlateCarree())

            # Course change markers (if needed)
            if met==0:
                ax_main.set_title(f'Telescope movement - Two Step method. time={max(timearrs1[-1], timearrs2[-1]):.2f} sec',y=1.15 )
            elif met==1:
                ax_main.set_title(f'Telescope movement - Partial communication method. time={max(timearrs1[-1], timearrs2[-1]):.2f} sec',y=1.15  )

            else:
                ax_main.set_title(f'Telescope movement. No communication method. time={max(timearrs1[-1], timearrs2[-1]):.2f} sec',y=1.15  )


            ax_main.legend(loc='upper left', bbox_to_anchor=(-0.2, 1), prop={'size': 8},framealpha=0.6 )  # Adjust size as needed

            # === Small Colorbar Matrix ===
            n_cols = min(len(labelss), 5)  # Max 5 columns to keep them inside the figure

            # Calculate starting position for small colorbars
            left_margin = 0.05
            right_margin = 0.9
            spacing_x = (right_margin - left_margin) / n_cols
            spacing_y = 0.08  # Adjust vertical spacing to keep them inside

            def scientific_1e5(x, pos):
                return f"{x * 1e5:.1f}"  # Convert to fixed 1e-5 notation

            for i, scatter in enumerate(scatter_plots):
                row = i // n_cols
                col = i % n_cols

                # Adjust positions dynamically so all colorbars stay inside
                x_pos = left_margin + col * spacing_x
                y_pos = 0.22 - row * spacing_y

                ax_cbar = fig.add_axes([x_pos, y_pos, 0.12, 0.02])  # Small horizontal colorbars

                # Normalize with a fixed range
                norm = colors.Normalize(vmin=min(bulks[i]), vmax=max(bulks[i]))
                sm = plt.cm.ScalarMappable(cmap=scatter.cmap, norm=norm)

                cbar = fig.colorbar(sm, cax=ax_cbar, orientation="horizontal")
                cbar.set_label(f'Update-{i + 1} prob.', fontsize=9)
                cbar.ax.xaxis.set_label_position('top')  # Moves the label above the colorbar

                # Apply formatter to force 1e-5 display
                formatter = FuncFormatter(scientific_1e5)
                cbar.ax.xaxis.set_major_formatter(formatter)

                # Set proper ticks
                ticks = np.linspace(min(bulks[i]), max(bulks[i]), num=2)
                cbar.set_ticks(ticks)

                # Increase tick density
                cbar.update_ticks()
                cbar.ax.tick_params(labelsize=6)

            if who_found:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

                #plt.savefig(f"figure_{z}_{met}_{timestamp}_{rax}_{decx}.jpg",dpi=300)
                plt.show()
                tele_times.append([timearrs1[-1], timearrs2[-1]])
                who_found_arr.append(who_found)
                print(who_found == tele1.name, who_found == tele2.name)

                track_times.append(timearrs2[-1])

            if tele_times == []:
                break


        if len(tele_times) == 3:
            recordings(tele_times, who_found_arr, phiI, thetaI, phiI2, thetaI2, rax, decx, A90, tele1, tele2, t_pre_merge, file_name, run, thetaLVK, phiLVK, psiLVK, ILVK, SNRs, track_times, dis, D, SNRs_filtered, t_pre_merge_filtered,
                       A90_filtered)
            recordingsXL(tele_times, who_found_arr, phiI, thetaI, phiI2, thetaI2, rax, decx, A90, tele1, tele2, t_pre_merge, file_name, run, thetaLVK, phiLVK, psiLVK, ILVK, SNRs, track_times, dis, D, SNRs_filtered, t_pre_merge_filtered,
                         A90_filtered)

