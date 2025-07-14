import matplotlib.pyplot as plt
from prob_in_blob import prob_in_blob
from closest_point import closest_point
def labelmax_maker(bulk,pointsra,pointsdec, pointslabels ,labels,nkmeans, tele1,tele2, phiI, thetaI, phiI2, thetaI2):
    labelmax1= 0
    labelmax2= 0
    bulkramax1 = []
    bulkdecmax1 = []
    bulkramax2 = []
    bulkdecmax2 = []
    ts1=[]
    minras1=[]
    mindecs1=[]
    ts2=[]
    minras2=[]
    mindecs2=[]

    print('labels',len(labels))
    print('bulk',len(bulk))
    print('nkmeans',nkmeans)

    probs,blobras,blobdecs=prob_in_blob(bulk,labels,nkmeans,pointsra,pointsdec, pointslabels)
    print('blobras',blobras)
    for i in range(len(blobras)):
        minra, mindec,mintime = closest_point(blobras[i], blobdecs[i], tele1, phiI, thetaI)
        ts1.append(mintime)
        minras1.append(minra)
        mindecs1.append(mindec)
        minra, mindec, mintime = closest_point(blobras[i], blobdecs[i], tele2, phiI2, thetaI2)
        ts2.append(mintime)
        minras2.append(minra)
        mindecs2.append(mindec)

        print('ts', ts1, ts2)

    scores1=[]
    scores2=[]
    for i in range(len(ts2)):
        scores1.append(0.75*probs[i]/max(probs)+0.25*(1-ts1[i]/max(ts1)))
        scores2.append(0.75*probs[i]/max(probs)+0.25*(1-ts2[i]/max(ts2)))
    labelmax1=scores1.index(max(scores1))
    labelmax2=scores2.index(max(scores2))
    print('labels',labels)
    print('labelmax12',labelmax1,labelmax2,labels,scores1,scores2,ts1,ts2)


    bulkramax1=blobras[labelmax1]
    bulkramax2 = blobras[labelmax2]
    bulkdecmax1=blobras[labelmax1]
    bulkdecmax2 = blobdecs[labelmax2]
    minra1=minras1[labelmax1]
    minra2=minras2[labelmax2]
    mindec1 = mindecs1[labelmax1]
    mindec2 = mindecs2[labelmax2]
    print('labelmax1',labelmax1,labelmax2,labels,scores1)
    print('labelmax1',blobras,blobdecs)
    '''
    #if ((1 not in labels) and labelmax1==1) or  ((0 not in labels) and labelmax1==0 ):
    plt.plot(pointsra, pointsdec, 'o', label="Main Points")  # Circle markers

    for i in range(len(blobras)):
        plt.plot(blobras[i], blobdecs[i], 's', label=f"Blob {i + 1}")  # Square markers

    plt.plot(phiI, thetaI, 'd', label="PhiI-ThetaI")  # Diamond markers
    plt.plot(phiI2, thetaI2, '^', label="PhiI2-ThetaI2")  # Triangle markers
    plt.plot(minra1, mindec1, 'x', label="Min 1")  # X markers
    plt.plot(minra2, mindec2, '+', label="Min 2")  # Plus markers

    plt.legend()
    plt.show()
    '''
    return labelmax1,bulkramax1,bulkdecmax1,labelmax2,bulkramax2,bulkdecmax2,minra1,minra2,mindec1,mindec2
