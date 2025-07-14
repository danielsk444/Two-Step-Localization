import numpy as np

def calc_sky_area_per_pix(hpx):
    npix = len(hpx)
    sky_area = 4 * 180 ** 2 / np.pi
    print('sky_area / npix=', sky_area / npix)
    return npix, sky_area
