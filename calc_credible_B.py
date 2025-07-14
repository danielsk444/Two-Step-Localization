import numpy as np
import healpy as hp

def calc_credible_B(hpx, nside,probrob):
    i = np.flipud(np.argsort(hpx))
    sorted_credible_levels = np.cumsum(hpx[i])
    credible_levels = np.empty_like(sorted_credible_levels)
    credible_levels[i] = sorted_credible_levels
    #print('credible_levels=', credible_levels)
    A = np.sum(credible_levels <= probrob-0.00001) * hp.nside2pixarea(nside, degrees=True)
    return credible_levels, A

