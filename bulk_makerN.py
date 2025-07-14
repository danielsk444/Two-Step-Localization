from calc_ra_dec import calc_ra_dec
import numpy as np
import healpy as hp

def bulk_makerN(hpx,nside,percentile,credible_levels):
    bulk = []
    bulkra = []
    bulkdec = []
    bulkpix = []
    #A = np.sum(credible_levels <= percentile) * hp.nside2pixarea(nside, degrees=True)
    for i in range(len(hpx)):
        if credible_levels[i] <= percentile:
            ra, dec = calc_ra_dec(i, nside)
            bulk.append(hpx[i])
            bulkra.append(ra)
            bulkdec.append(dec)
            bulkpix.append(i)
    return bulkra, bulkdec, bulk,bulkpix
