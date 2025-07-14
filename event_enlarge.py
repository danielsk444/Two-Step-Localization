from gauge import gauge
from is_globe import is_globe
import numpy as np
from calc_ra_dec import calc_ra_dec
from calc_ipix_max import calc_ipix_max
from calc_ipix import calc_ipix
from prob_in_circ import prob_in_circ
import matplotlib.pyplot as plt

def event_enlarge(hpx, bulk, bulkra, bulkdec, stretch, labels, nkmeans, nside):
    probrob = 0
    ipix_max, prob_dens_ipix_max = calc_ipix_max(hpx)
    ramax, decmax = calc_ra_dec(ipix_max, nside)

    print(labels)
    print('nkmeans', nkmeans)

    print('len bulkra',len(bulkra))
    # Example of enlarging areas by adding more points around existing high-density points
    '''
    enlarged_bulkra = []
    enlarged_bulkdec = []
    enlarged_bulk = []
    
    for ra, dec,b in zip(bulkra, bulkdec,bulk):
        # Example: add 4 additional points (adjust the number as needed)
        for _ in range(4):
            # Generate new points around (ra, dec), example: slight random perturbation
            new_ra = ra + np.random.uniform(-5, 5)  # adjust range as needed
            new_dec = dec + np.random.uniform(-5, 5)  # adjust range as needed
            new_b = np.random.uniform(0.1, 0.9)*b   # adjust range as needed

            enlarged_bulkra.append(new_ra)
            enlarged_bulkdec.append(new_dec)
            enlarged_bulk.append(new_b)
   
    # Combine existing and enlarged points
    for i in range(len(enlarged_bulkra)):
        if enlarged_bulkra[i] not in bulkra and enlarged_bulkdec [i] not in bulkdec:
            bulkra.append(enlarged_bulkra[i])
            bulkdec.append(enlarged_bulkdec[i])
            bulk.append(enlarged_bulk[i])

    
    # Combine existing and enlarged points

    bulkra.extend(enlarged_bulkra)
    bulkdec.extend(enlarged_bulkdec)
    bulk.extend(enlarged_bulk)

    '''
    for i in range(len(bulkra)):
        # Example: adjust existing points by adding slight random perturbation
        bulkra[i] += np.random.uniform(-15, 15)  # adjust range as needed
        bulkdec[i] += np.random.uniform(-15, 15)  # adjust range as needed
        bulk[i] = np.random.uniform(0.1, 0.9) * bulk[i]  # adjust range as need
    bulkn=bulk
    bulkra, bulkdec = gauge(bulkra, bulkdec)
    print('len bulkra',len(bulkra))
    plt.plot(bulkra, bulkdec, '.')
    plt.show()
    norm = 1
    while probrob < 0.89:
        bulk = []
        for i in range(0, len(bulkn)):
            bulk.append(bulkn[i] * norm)

        nmap = np.zeros(len(hpx))
        for i in range(len(bulk)):
            p = calc_ipix(bulkra[i], bulkdec[i], nside)
            #print('norm', norm, 'probrob', probrob)
            nmap[p] = bulk[i]
            print('ddd', len(bulk), len(bulkra), len(bulkdec))

        probrob = prob_in_circ(nmap, ramax, decmax, 100000, nside)
        norm = norm + 0.05
        print('norm', norm, 'probrob', probrob)
    while probrob >0.91:
        bulk = []
        for i in range(0, len(bulkn)):
            bulk.append(bulkn[i] * norm)

        nmap = np.zeros(len(hpx))
        for i in range(len(bulk)):
            p = calc_ipix(bulkra[i], bulkdec[i], nside)
            print('norm', norm, 'probrob', probrob)
            nmap[p] = bulk[i]
            print('ddd', len(bulk), len(bulkra), len(bulkdec))

        probrob = prob_in_circ(nmap, ramax, decmax, 100000, nside)
        norm = norm - 0.02

        print('norm', norm, 'probrob', probrob)
    # hp.fitsfunc.write_map('nnmap39.fits', nmap)
    # hpx1 = read_map('nnmap39.fits')
    hpx1 = nmap
    return hpx1, bulk, bulkra, bulkdec,probrob
