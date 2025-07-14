import numpy as np
import healpy as hp

def area_calc(bulk,hpx,nside):
    i = np.flipud(np.argsort(hpx))
    sorted_credible_levels = np.cumsum(hpx[i])
    credible_levels = np.empty_like(sorted_credible_levels)
    credible_levels[i] = sorted_credible_levels
    print('credible_levels=', credible_levels)

    A = np.sum(bulk) * hp.nside2pixarea(nside, degrees=True)

    return A
