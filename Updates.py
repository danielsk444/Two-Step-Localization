from kmeans import kmeans
from updateN import updateN

def Updates(nside, r2, area_update, hpx, labels, bulk, bulkra, bulkdec, pointsra, pointsdec, pointslabels):
    hpxs = []
    bulks = []
    bulkras = []
    bulkdecs = []
    labelss = []
    pointsras = []
    pointsdecs = []
    pointslabelss = []


    hpxs.append(hpx)
    bulks.append(bulk)
    bulkras.append(bulkra)
    bulkdecs.append(bulkdec)
    labelss.append(labels)
    pointsras.append(pointsra)
    pointsdecs.append(pointsdec)
    pointslabelss.append(pointslabels)


    for uflag in range(len(area_update)):
        hpx, bulk, bulkra, bulkdec, pointsra, pointsdec, pointslabels, labels, labelsc, nkmeans = updateN(nside, pointsra, pointsdec, r2, area_update[uflag], hpx)
        labels, labelsc, nkmeans, centroids = kmeans(bulkra, bulkdec)
        pointsras.append(pointsra)
        pointsdecs.append(pointsdec)
        pointslabelss.append(pointslabels)
        labelss.append(labels)
        bulks.append(bulk)
        bulkras.append(bulkra)
        bulkdecs.append(bulkdec)
        hpxs.append(hpx)
    return  hpxs,bulks,bulkras,bulkdecs,pointsras,pointsdecs,pointslabelss,labelss
