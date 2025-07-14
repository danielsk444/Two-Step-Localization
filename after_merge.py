from is_it_here import is_it_here
import numpy as np
import matplotlib.pyplot as plt

def after_merge(hpx, pointsra, pointsdec, r, nside, event_ipix,kk,scanned_time,scanned_pix,timearrs,scanned_ra,scanned_dec,passedra,passeddec):
    is_here, scanned_ra1, scanned_dec1, ipix_disc = is_it_here(hpx, pointsra[kk], pointsdec[kk], r, nside, event_ipix)
    # scanned_pix.append(ipix_disc)
    scanned_time = np.append(scanned_time, timearrs[-1])
    scanned_pix = np.append(scanned_pix, ipix_disc)
    scanned_ra.append(scanned_ra1)
    scanned_dec.append(scanned_dec1)
    passedra.append(pointsra[kk])
    passeddec.append(pointsdec[kk])
    return scanned_time,scanned_pix,scanned_ra,scanned_dec,passedra,passeddec,is_here