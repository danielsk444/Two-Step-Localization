
def build_rest_kmeans(nkmeans,pointsra,pointsdec,kk,kks,labels,points2bulk):
    kkns = []
    red_labels = []
    red_pointsra = []
    red_pointsdec = []
    for j in range(nkmeans):
        for i in range(len(pointsra)):
            print('build', i, kks, j, labels[points2bulk[i]])
            if i not in kks and j == labels[points2bulk[i]]:
                print('build')
                red_labels.append(labels[points2bulk[i]])
                red_pointsra.append(pointsra[i])
                red_pointsdec.append(pointsdec[i])
    ll = 0

    for i in range(len(red_labels)):
        if red_labels[i] == labels[points2bulk[kk]] and ll == 0:
            ll = i
    return kkns,red_labels,red_pointsra,red_pointsdec,ll