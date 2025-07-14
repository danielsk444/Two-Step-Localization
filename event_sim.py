from gauge import gauge
from is_globe import is_globe
import numpy as np
from calc_ra_dec import calc_ra_dec
from calc_ipix_max import calc_ipix_max
from calc_ipix import calc_ipix
from prob_in_circ import prob_in_circ
import matplotlib.pyplot as plt

def event_sim(hpx, bulk, bulkra, bulkdec, ra, dec, stretch, labels, labelsc, nkmeans,nside):
    norm = 1
    probrob = 0
    bulkn = []
    bulkran = []
    bulkdecn = []
    ipix_max, prob_dens_ipix_max = calc_ipix_max(hpx)
    ramax, decmax = calc_ra_dec(ipix_max, nside)
    ramove = ramax - ra
    decmove = decmax - dec
    print(labels)
    print('nkmeans',nkmeans)

    for i in range(nkmeans):
        bulkraa = []
        bulkdeca = []
        bulka = []
        labels1 = []
        maxra = -10000
        maxdec = -10000
        minra = 10000
        mindec = 10000
        for j in range(len(labels)):
            if labels[j] == i:
                bulkraa.append(bulkra[j])
                bulkdeca.append(bulkdec[j])
                bulka.append(bulk[j])
                labels1.append(labelsc[j])
                if bulkra[j] < minra:
                    minra = bulkra[j]
                if bulkra[j] > maxra:
                    maxra = bulkra[j]
                if bulkdec[j] < mindec:
                    mindec = bulkdec[j]
                    mindeclabel = labelsc[j]
                if bulkdec[j] > maxdec:
                    maxdec = bulkra[j]
                    maxdeclabel = labelsc[j]
        print('labelsc',len(labelsc))
        print('labels1',len(labels1))
        labels1c = []
        for i in range(len(labels1)):
            labels1c.append(labels1[i])
        # print('labels1c',labels1c)
        labels1, globe, globe1, globe2, globemin, globemax = is_globe(bulkraa, bulkdeca, labels1)
        # print('labelss',len(labels))

        if globe:
            middec = mindec + (maxdec - mindec) / 2
            midra = globemin + (360 - globemin + globemax) / 2
            if midra > 360:
                midra = midra - 360

            for j in range(len(bulka)):
                #print('gg', j)
                if labels1c[j] != labels1[j]:

                    if midra > 180:
                        bulkraa[j] = 360 - max(midra, bulkraa[j]) + min(midra, bulkraa[j])
                    else:
                        bulkraa[j] = -360 + max(midra, bulkraa[j]) - min(midra, bulkraa[j])
                else:
                    bulkraa[j] = bulkraa[j] - midra
                bulkdeca[j] = bulkdeca[j] - middec

        elif globe1:
            maxdec = 10000
            for j in range(len(bulka)):
                if labels1c[j] != mindeclabel:
                    if bulkdeca[j] < maxdec:
                        maxdec = bulkdeca[j]
            middec = mindec + (180 - maxdec - mindec) / 2
            midra = minra + (maxra - minra) / 2
            for j in range(len(bulka)):
                if labels1c[j] != mindeclabel:
                    bulkdeca[j] = 180 - bulkdeca[j] - middec
                else:
                    bulkdeca[j] = bulkdeca[j] - middec
                bulkraa[j] = bulkraa[j] - midra

        elif globe2:
            mindec = -10000
            for j in range(len(bulka)):
                if labels1c[j] != maxdeclabel:
                    if bulkdeca[j] > mindec:
                        mindec = bulkdeca[j]
            middec = maxdec - (180 + maxdec + mindec) / 2
            midra = minra + (maxra - minra) / 2
            for j in range(len(bulka)):
                if labels1c[j] != mindeclabel:
                    bulkdeca[j] = -180 + bulkdeca[j] + bulkdeca
                else:
                    bulkdeca[j] = bulkdeca[j] - middec
        else:
            midra = minra + (maxra - minra) / 2
            middec = mindec + (maxdec - mindec) / 2

            for j in range(len(bulka)):
                bulkraa[j] = bulkraa[j] - midra
                bulkdeca[j] = bulkdeca[j] - middec

        for j in range(len(bulka)):
            bulkran.append( midra  + stretch * (bulkraa[j]))
            bulkdecn.append( middec + stretch * (bulkdeca[j]))
            bulkn.append(bulka[j])




    bulkran, bulkdecn = gauge(bulkran, bulkdecn)
    bulkra = []
    bulkdec = []
    for j in range(len(bulkran)):
        bulkra.append(bulkran[j])
        bulkdec.append(bulkdecn[j])
    print('l', len(bulk), len(bulkra))

    while probrob < 0.99:
        bulk = []
        for i in range(0, len(bulkn)):
            bulk.append(bulkn[i] * norm)

        print('ramove', ramove, ramax, decmove, decmax)
        nmap = np.zeros(len(hpx))
        for i in range(len(bulk)):
            p = calc_ipix(bulkra[i], bulkdec[i],nside)
            print('norm', norm, 'probrob', probrob)
            nmap[p] = bulk[i]
            print('ddd', len(bulk), len(bulkra), len(bulkdec))

        probrob = prob_in_circ(nmap, ramax, decmax, 100000, nside)
        if stretch < 0.1:
            norm = norm + 10
        elif stretch < 0.3:
            norm = norm + 3
        else:
            norm = norm + 2
        print('norm', norm, 'probrob', probrob)

    # hp.fitsfunc.write_map('nnmap39.fits', nmap)
    # hpx1 = read_map('nnmap39.fits')
    hpx1 = nmap
    return hpx1,bulk, bulkra, bulkdec


