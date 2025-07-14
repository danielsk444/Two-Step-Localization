import healpy as hp

def prob_in_poly(hpx, xyz, nside):
    ipix_poly = hp.query_polygon(nside, xyz)
    prob_poly = hpx[ipix_poly].sum()
    print('Integrated Probability in Circle for the given xyz set is - ', prob_poly)
    return prob_poly