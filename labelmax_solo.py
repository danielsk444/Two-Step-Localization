import matplotlib.pyplot as plt
from prob_in_blob import prob_in_blob
from closest_point import closest_point
def labelmax_solo(bulk,labels,tele,  phiI, thetaI,pointsra,pointsdec, pointslabels):
    labelmax1= 0
    bulkramax1 = []
    bulkdecmax1 = []
    ts1=[]
    minras1=[]
    mindecs1=[]


    probs,blobras,blobdecs=prob_in_blob(bulk,labels,len(set(labels)),pointsra,pointsdec, pointslabels)
    print('blobras',blobras)
    for i in range(len(blobras)):
        minra, mindec,mintime = closest_point(blobras[i], blobdecs[i], tele, phiI, thetaI)
        ts1.append(mintime)
        minras1.append(minra)
        mindecs1.append(mindec)

    scores1=[]
    for i in range(len(ts1)):
        scores1.append(0.75*probs[i]/max(probs)+0.25*(1-ts1[i]/max(ts1)))
    labelmax1=scores1.index(max(scores1))
    print('labels',labels)
    #plt.plot(1, 1)
    #plt.show()
    bulkramax1=blobras[labelmax1]
    bulkdecmax1=blobras[labelmax1]
    minra1=minras1[labelmax1]
    mindec1 = mindecs1[labelmax1]

    print('labelmax1',labelmax1,labels,scores1)
    if ((1 not in labels) and labelmax1==1) or  ((0 not in labels) and labelmax1==0 ):
        plt.plot(1,1)
        plt.show()

    return labelmax1,bulkramax1,bulkdecmax1,minra1,mindec1
