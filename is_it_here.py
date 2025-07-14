import numpy as np
import healpy as hp
from calc_ra_dec import calc_ra_dec
import matplotlib.pyplot as plt

def is_it_here(ra, dec, r, nside, event_ipix):
    is_here = False
    #ipix_disc=np.array([])
    scanned_ra1 = []
    scanned_dec1 = []
    s_ra = 0
    s_dec = 0
    theta = 0.5 * np.pi - np.deg2rad(dec)

    phi = np.deg2rad(ra)
    radius = np.deg2rad(r)
    #print('xyz = hp.ang2vec(theta, phi)', theta, phi, dec, ra)
    xyz = hp.ang2vec(theta, phi)
    ipix_disc = hp.query_disc(nside, xyz, radius)
    for i in range(len(ipix_disc)):
        s_ra, s_dec = calc_ra_dec(ipix_disc[i], nside)
        scanned_ra1.append(s_ra)
        scanned_dec1.append(s_dec)

    if event_ipix in ipix_disc:
        is_here = True

    return is_here, scanned_ra1, scanned_dec1,ipix_disc
