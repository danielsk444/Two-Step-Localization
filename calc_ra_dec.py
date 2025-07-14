import numpy as np
import healpy as hp

def calc_ra_dec(ipix, nside):
    theta, phi = hp.pix2ang(nside, ipix)
    ra = np.rad2deg(phi)
    dec = np.rad2deg(0.5 * np.pi - theta)
    # print('for pix no. ', ipix, 'ra=', ra, 'dec=', dec)
    return ra, dec