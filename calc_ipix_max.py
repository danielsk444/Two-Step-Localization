import numpy as np
def calc_ipix_max(hpx):
    ipix_max = np.argmax(hpx)
    #print('The highest probability pixel - pix no.', ipix_max)
    prob_dens_ipix_max = hpx[ipix_max]  # / hp.nside2pixarea(nside, degrees=True)
    #print('The probability density per square degree at that position -', prob_dens_ipix_max)
    return ipix_max, prob_dens_ipix_max
