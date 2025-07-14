import numpy as np
from path import path
from is_it_here import is_it_here
from prob_in_circ import prob_in_circ
from calc_ipix import calc_ipix
import matplotlib.pyplot as plt
from is_in_nested_list import is_in_nested_list
from plant_event import plant_event

def scan2tel2(pointsra, pointsdec, tele, tchange, rachange, decchange, ii, timearr, theta, phi, tottime, j, event_ipix, hpx, nside, minrap, mindecp, kks, phis, thetas, timearrs, F, r, passedra, passeddec, scanned_ra, scanned_dec, scanned_pix, scanned_time, countwhile, kk, tempdis, c, y, pointslabels, delay, merge, t_update, met, changepix, change_is_here, scanned_pix_s,z,t0,bulk, bulkra, bulkdec):
    is_here = False
    turn_points_ra = []
    turn_points_dec = []
    candidx = []
    candprob = []
    countwhile += 1

    if not merge:
        delay = 0

    # Convert pointsra, pointsdec to NumPy arrays for faster calculations (only once)
    pointsra = np.array(pointsra)
    pointsdec = np.array(pointsdec)

    # Precompute the differences in ra and dec for efficiency
    ra_diffs = np.abs(phis[-1] - pointsra)
    ra_diffs = np.where(ra_diffs > 180, 360 - ra_diffs, ra_diffs)
    dec_diffs = np.abs(thetas[-1]- pointsdec)

    # Loop over points in a more optimized way
    for i in range(len(pointsra)):
        radis = ra_diffs[i]
        dec_diff = dec_diffs[i]

        # Efficient condition check using NumPy

        if pointslabels[i] == y and radis + dec_diff < c * r  and radis + dec_diff > 0 and not calc_ipix(pointsra[i], pointsdec[i], nside) in scanned_pix :
            candidx.append(i)

            # Calculate the probability only for valid candidates
            candprob.append(prob_in_circ(hpx, pointsra[i], pointsdec[i], r, nside))

    if candprob:
        # Find the index of the max probability efficiently
        max_prob_idx = np.argmax(candprob)

        # Reset countwhile when a new candidate is found
        countwhile = 1
        c = 1.5

        # Path calculation with the new candidate
        phi1, theta1, timearr1, tt, turn_points_ra, turn_points_dec = path(
            tele, phis[-1], thetas[-1], pointsra[candidx[max_prob_idx]], pointsdec[candidx[max_prob_idx]],
            timearr, theta, phi, tottime, turn_points_ra, turn_points_dec
        )

        # Update the arrays with the new values
        phis = np.append(phis, phi1)
        thetas = np.append(thetas, theta1)
        timearr1 = np.add(timearr1, timearrs[-1])
        timearr1[-1] = timearr1[-1] + delay
        timearrs = np.append(timearrs, timearr1)

        # Update kk to the index of the chosen candidate
        kk = candidx[max_prob_idx]
        if timearrs[-1] >= t0 and timearrs[-1]!=100000 :
            merge = True
            if met == 0 and event_ipix == 0 and z == 0:
                event_idx, event_ipix = plant_event(bulk, bulkra, bulkdec, nside)
        else:
            merge = False
        if merge:
            kks.append(kk)
            is_here, scanned_ra1, scanned_dec1, ipix_disc = is_it_here(pointsra[kk], pointsdec[kk], r, nside, event_ipix)

            scanned_time.append(timearrs[-1])
            scanned_ra.append(scanned_ra1)
            scanned_dec.append(scanned_dec1)
            passedra.append(pointsra[kk])
            passeddec.append(pointsdec[kk])

            # Check the satellite condition and update scanned_pix_s or scanned_pix accordingly
            if tele.name in ['BIG', 'ULTRASAT'] and is_here:
                scanned_pix_s = ipix_disc
            else:
                scanned_pix.extend(ipix_disc)

    # Dynamically adjust the value of 'c' based on countwhile
    if countwhile > 20:
        c += 10
    elif countwhile > 10:
        c += 5
    elif countwhile > 5:
        c += 2
    else:
        c += 0.5

    return phis, thetas, timearrs, kks, scanned_ra, scanned_dec, scanned_pix, scanned_time, passedra, passeddec, is_here, countwhile, kk, tempdis, c, y, change_is_here, scanned_pix_s,event_ipix
