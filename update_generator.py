import pylab as pl

from localization_generator import localization_generator
from event_update import event_update
import matplotlib.pyplot as plt
def update_generator(run, t_pre_merge,hpx):
    A90,theta,phi,psi,I,SNRs,dis,D = localization_generator(run, t_pre_merge)
    #A90=[1000,500,400,300]
    #4pi sreradians=  41252.96 deg^2
    full_sphere=41252.96
    filtered_data = [(a, s, t) for a, s, t in zip(A90, SNRs, t_pre_merge) if a <= full_sphere]

    # Unzip the filtered result
    A90_filtered, SNRs_filtered, t_pre_merge_filtered = zip(*filtered_data) if filtered_data else ([], [], [])

    # Convert tuples back to lists
    A90_filtered = list(A90_filtered)
    SNRs_filtered = list(SNRs_filtered)
    t_pre_merge_filtered = list(t_pre_merge_filtered)
    #print(t_pre_merge_filtered)

    if t_pre_merge_filtered!=[]:

        hpx, bulk, bulkra, bulkdec,bulkpix, probrob, A,good_area = event_update(A90_filtered[0], hpx)
        t_update = []
        area_update = []
        for i in range(1,len(t_pre_merge_filtered)):
            t_update.append(t_pre_merge[0] - t_pre_merge_filtered[ i])
            area_update.append(A90_filtered[i])

        print('t_update,area_update',t_update,area_update,len(t_pre_merge),A90,SNRs,A)
    else:
        good_area=False
        t_update, area_update, hpx, bulk, bulkra, bulkdec,bulkpix, A90, theta, phi, psi, I, SNRs, dis, D,  SNRs_filtered, t_pre_merge_filtered, A90_filtered=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
    #plt.plot(bulkra, bulkdec,',')
    #plt.show()
    return t_update,area_update,hpx, bulk,bulkra, bulkdec,bulkpix,A90,theta,phi,psi,I,SNRs,dis,D,good_area,SNRs_filtered,t_pre_merge_filtered,A90_filtered