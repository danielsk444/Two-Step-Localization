import numpy as np
import healpy as hp

def calc_ipix(ra, dec,nside):
    theta = 0.5 * np.pi - np.deg2rad(dec)
    phi = np.deg2rad(ra)
    #print(nside, theta, phi)
    ipix = hp.ang2pix(nside, theta, phi)
    #print('for ra - ', ra, ' and dec- ', dec, 'pix no.=', ipix)
    return ipix