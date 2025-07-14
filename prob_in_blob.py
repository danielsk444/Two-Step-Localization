import matplotlib.pyplot as plt
def prob_in_blob(bulk,labels,nkmeans,pointsra,pointsdec, pointslabels ):
    probs=[]
    blobras = []
    blobdecs = []
    for i in range(nkmeans):
        prob=0
        blobra=[]
        blobdec=[]

        for j in range(len(labels)):
            if labels[j]==i:
                prob=prob+bulk[i]
        probs.append(prob)
        for j in range(len(pointslabels)):
            if pointslabels[j] == i:
                blobra.append(pointsra[j])
                blobdec.append(pointsdec[j])
        blobras.append(blobra)
        blobdecs.append(blobdec)
    return probs,blobras,blobdecs