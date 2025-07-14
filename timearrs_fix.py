import numpy as np

def timearrs_fix(phis,thetas,timearrs):
    i=-1
    f=False
    if timearrs[-1]==15:
        f=True
        timearrs = np.delete(timearrs, i)
        phis = np.delete(phis, i)
        thetas = np.delete(thetas, i)
        i=i-1

    while(timearrs[i]==0):
        timearrs = np.delete(timearrs, i)
        phis = np.delete(phis, i)
        thetas = np.delete(thetas, i)
        i=i-1
    if f:
        timearrs[-1]=timearrs[-1]+15
    return phis,thetas,timearrs