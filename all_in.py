from is_it_here import is_it_here
from calc_ipix import calc_ipix
from plant_event import plant_event
from updateN import updateN
from after_merge import after_merge

def all_in(hpx, pointsra, pointsdec, r1,r2,timearrs1,timearrs2,kk1,kk2,nside,t_update,uflag,area_update,file_name,labels, labelsc, nkmeans,labelss,hpxs,bulks,bulkras,bulkdecs, bulk, bulkra, bulkdec,kks,  pointslabels):
    count1=0
    count2=0
    merge=False
    print('pointsra,pointsdec',pointsra,pointsdec)
    for i in range(len(pointsra)):
        is_here, scanned_ra1, scanned_dec1,ipix_disc = is_it_here(hpx, pointsra[kk1], pointsdec[kk1], r1, nside, calc_ipix(pointsra[i], pointsdec[i],nside))
        if is_here:
            count1 = count1+1
        is_here, scanned_ra1, scanned_dec1,ipix_disc = is_it_here(hpx, pointsra[kk2], pointsdec[kk2], r2, nside, calc_ipix(pointsra[i], pointsdec[i],nside))
        if is_here:
            count2 = count2+1
    print('count1', count1,count2,len(pointsra))

    if count1==len(pointsra)or count2==len(pointsra):
        t_add= t_update[-1]-max(timearrs1[-1],timearrs2[-1])
        timearrs1[-1]=timearrs1[-1]+t_add
        timearrs2[-1]=timearrs2[-1]+t_add
        merge=True
        print('merge', merge)

        if uflag < len(t_update):
            while (timearrs1[-1] >= t_update[uflag] or timearrs2[-1] >= t_update[uflag]):
                print('whileall')
                if timearrs1[-1] >= t_update[uflag] or timearrs2[-1] >= t_update[uflag]:
                    # aa = [pointsra[kk1], pointsdec[kk1], pointsra[kk2], pointsdec[kk2]]
                    hpx, bulk, bulkra, bulkdec, pointsra, pointsdec, pointslabels, kk1, kk2, labels, labelsc, nkmeans, labelss, hpxs1, bulks1, bulkras1, bulkdecs1 = updateN(labels, nside, pointsra, pointsdec, r2, kk1, kk2, kks, pointslabels,
                                                                                                                                                                         area_update[uflag], file_name, labelss, hpxs, bulks, bulkras, bulkdecs)
                    kks = [kk1, kk2]
                    # print('re', aa,pointsra[kk1], pointsdec[kk1], pointsra[kk2], pointsdec[kk2])
                    uflag = uflag + 1
                    if uflag == len(t_update):
                        merge = True


    return timearrs1,timearrs2,merge,uflag,hpx, bulk, bulkra, bulkdec, pointsra, pointsdec, pointslabels, kk1, kk2,labels, labelsc, nkmeans,labelss,hpxs,bulks,bulkras,bulkdecs, bulk, bulkra, bulkdec,