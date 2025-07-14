import matplotlib.pyplot as plt
import numpy as np
import healpy as hp
from calc_sky_area_per_pix import calc_sky_area_per_pix
from calc_nside import calc_nside
from calc_credible_levels import calc_credible_levels
from read_map import read_map
from calc_ipix import calc_ipix
from bulk_makerN import bulk_makerN
import time



def event_update(area, hpx):
    #start = time.time()  # Capture start time

    print('event_update')

    npix, sky_area = calc_sky_area_per_pix(hpx)
    nside = calc_nside(npix)
    c=1
    probrob = 0.9
    A = 41252.96  # Total sky area in degrees^2
    percentile = 0.99999

    # Precompute credible levels and initialize bulk
    credible_levels, _ = calc_credible_levels(hpx, nside, percentile)
    pixel_area_deg2 = hp.nside2pixarea(nside, degrees=True)  # Precompute pixel area

    # Optimize the area adjustment logic
    max_iterations = 2000
    adjustment_factor = 0.00001
    good_area = True
    count_tot = 0
    while not (0.99 * area <= A <= 1.01 * area):
        count_tot += 1
        adjustment = 0  # Tracks cumulative percentile adjustment
        iteration_count = 0

        if A > 1.01 * area:  # Area is too large
            while A > 1.01 * area and iteration_count < max_iterations:
                #print('A',A)
                c=abs(area-A)
                #print('c1',c)
                adjustment -= adjustment_factor*c
                if abs(adjustment)>0.5*percentile:
                    adjustment==0.5*percentile
                A = np.sum(credible_levels <= percentile + adjustment) * pixel_area_deg2
                iteration_count += 1
                #print('1eu',A,area,percentile , adjustment)
        elif A < 0.99 * area:  # Area is too small
            while A < 0.99 * area and iteration_count < max_iterations:
                c=100*(area-A)/area
                #print('c2',c)
                adjustment += adjustment_factor*c
                A = np.sum(credible_levels <= percentile + adjustment) * pixel_area_deg2
                iteration_count += 1
                #print('2eu',A,area,percentile , adjustment)

        percentile += adjustment
        if count_tot > 5:  # Exit if adjustments take too long
            good_area = False
            break

    # Generate bulk data
    bulkra, bulkdec, bulk, bulkpix = bulk_makerN(hpx, nside, percentile, credible_levels)

    # Create the new map efficiently
    nmap = np.zeros(len(hpx))
    pixel_indices = [calc_ipix(bulkra[i], bulkdec[i], nside) for i in range(len(bulk))]
    for idx, pix in enumerate(pixel_indices):
        nmap[pix] = bulk[idx]

    hpx1 = nmap
    #print('lenhpx',len(hpx1),len(hpx))
    #end = time.time()  # Capture end time
    #elapsed_time = end - start
    #print(f"Elapsed time: {elapsed_time:.2f} seconds")
    #plt.plot(2,2)
    #plt.show()
    return hpx1, bulk, bulkra, bulkdec, bulkpix, probrob, A, good_area
