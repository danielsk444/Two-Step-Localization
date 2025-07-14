import numpy as np
import healpy as hp
def prob_in_circ(hpx, ra, dec, r, nside):
    theta = 0.5 * np.pi - np.deg2rad(dec)
    phi = np.deg2rad(ra)
    radius = np.deg2rad(r)
    xyz = hp.ang2vec(theta, phi)
    ipix_disc = hp.query_disc(nside, xyz, radius)
    prob_circ = hpx[ipix_disc].sum()
    # print('Integrated Probability in Circle for ra - ', ra, 'dec- ', dec , ' and radius ', r,'is', prob_circ)
    return prob_circ
