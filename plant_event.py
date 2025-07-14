import numpy as np
from random import choices
from calc_ipix import calc_ipix
import matplotlib.pyplot as plt

def plant_event(bulk, bulkra, bulkdec,nside):
    idxs = np.linspace(0, len(bulk) - 1, len(bulk))
    event_idx = choices(idxs, weights=(bulk))
    print('event_idx', event_idx)
    event_ipix = calc_ipix(bulkra[int(event_idx[0])], bulkdec[int(event_idx[0])],nside)
    print('event_ipix', event_ipix)
    #plt.plot(2,2)
    #plt.show()
    return event_idx, event_ipix
