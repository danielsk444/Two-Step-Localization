import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.colors as mcolors
from Type1Mat import Type1Mat
from scan_mat import scan_mat

n = 500


def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=-1):
    if n == -1:
        n = cmap.N
    new_cmap = mcolors.LinearSegmentedColormap.from_list(
        'trunc({name},{a:.2f},{b:.2f})'.format(name=cmap.name, a=minval, b=maxval),
        cmap(np.linspace(minval, maxval, n)))
    return new_cmap


def ploti():
    r = 1
    u = np.linspace(0, 2 * np.pi, 2 * n)
    v = np.linspace(0, np.pi, 2 * n)
    x = r * np.outer(np.cos(u), np.sin(v))
    y = r * np.outer(np.sin(u), np.sin(v))
    z = r * np.outer(np.ones(np.size(u)), np.cos(v))
    # z[z < 0] = 0
    return x, y, z

def fig_plot(phis1, thetas1,phis2, thetas2,  bulkra, bulkdec, bulk, timearrs1,timearrs2,scanned_ra, scanned_dec,scanned_time):
    print('fig plot')
    #plt.plot(2,2)
    #plt.show()
    fig = plt.figure()
    [x, y, z] = ploti()
    time_matN = Type1Mat(phis1, thetas1,phis2, thetas2,  bulkra, bulkdec, bulk, timearrs1,timearrs2,scanned_ra, scanned_dec,scanned_time)
    #time_matN2 = scan_mat(scanned_ra, scanned_dec,scanned_time)

    minColor = 0.00
    maxColor = 0.3
    BrBG_t = truncate_colormap(plt.get_cmap("BrBG"), minColor, maxColor)
    minColor = 0.5
    maxColor = 1
    BrBG_tt = truncate_colormap(plt.get_cmap("BrBG"), minColor, maxColor)

    # parameterToColorBy = np.linspace(5, 10, 6, dtype=float)
    # colors = [BrBG_t(i) for i in np.linspace(0, 1, parameterToColorBy.shape[0])]
    # norm = mpl.colors.Normalize(parameterToColorBy[0],parameterToColorBy[-1])
    scamap = plt.cm.ScalarMappable(cmap='BrBG')
    scamap1 = plt.cm.ScalarMappable(cmap=BrBG_t)
    scamap2 = plt.cm.ScalarMappable(cmap=BrBG_tt)
    #scamap3 = plt.cm.ScalarMappable(cmap=Oranges)

    fcolors = scamap.to_rgba(time_matN)
    #fcolors2 = scamap3.to_rgba(time_matN2)
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    # ax.set_title(
    # f"{tele.get_name()} ||time: {timearr[-1]} ||phiI: {phiI} ||thetaI: {thetaI} ||phiF: {evra} ||thetaF: {evdec} ||phiF1: {ramax} ||thetaF1: {decmax}\nstretch: {stretch} ||tchange: {tchange} ||rachange: {rachange} ||decchange: {decchange} ||FOV: {FOV}||A:{A}\n||ramove: {ramove}||decmove: {decmove}||ramax1:{ramax1}||decmax1:{decmax1} ||minra:{minra}||mindec:{mindec}")
    ax.axis('off')
    #ax.plot_surface(x, y, z, facecolors=fcolors2, rstride=1, cstride=1, alpha=None, antialiased=True)

    ax.plot_surface(x, y, z, facecolors=fcolors, rstride=1, cstride=1, alpha=None, antialiased=True)

    # s = f"time-{timearr[-1]} \n,phiI-{phiI}\n,thetaI -{thetaI}\n,phiF-{evra}\n,thetaF-{evdec}\n,stretch-{stretch}\n,tchange-{tchange}\n,rachange-{rachange} \n,decchange-{decchange}\n,FOV-{FOV}"
    # ax.text(1, 1,2, s, ha="left", va="top")
    cmap = BrBG_t
    norm = mpl.colors.Normalize(vmin=0, vmax=max(timearrs1[-1],timearrs2[-1]))
    fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap), shrink=0.2, ax=ax, location="right", label="Time")
    cmap = BrBG_tt
    norm = mpl.colors.Normalize(vmin=0, vmax=max(bulk))
    fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap), shrink=0.2, ax=ax, location="left", label="Event prob.")
    print('min', np.amin(time_matN), 'max', np.amax(time_matN))
    # sm = plt.cm.ScalarMappable(cmap=BrBG_t)
    # sm.norm = mpl.colors.Normalize(1, max(timearr))
    # sm.cmap=mpl.colors.Colormap(BrBG_t)
    # cb = fig.colorbar(sm, shrink=0.2 ,ax=ax, location="left")plt.show()
    # plt.ion()
    # plt.draw()
    #plt.show()
