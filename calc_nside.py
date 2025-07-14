import healpy as hp

def calc_nside(npix):
    nside = hp.npix2nside(npix)
    print('nside=', nside)
    return nside