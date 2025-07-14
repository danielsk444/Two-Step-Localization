from calc_ipix_max import calc_ipix_max
from calc_ra_dec import calc_ra_dec
def bulk_maker(hpx,nside):
    bulk = []
    bulkra = []
    bulkdec = []
    ipix_max, prob_dens_ipix_max = calc_ipix_max(hpx)
    for i in range(len(hpx)):
        if hpx[i] > 0.1 * hpx[ipix_max]:
            ra, dec = calc_ra_dec(i, nside)
            bulk.append(hpx[i])
            bulkra.append(ra)
            bulkdec.append(dec)
    return bulkra, bulkdec, bulk
