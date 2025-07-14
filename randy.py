from random import random
import numpy as np

def randy():
    phiI = 360 * random()
    cos_thetaI = -1 + 2 * random()
    thetaI = np.rad2deg(np.arccos(cos_thetaI))-90
    #thetaI = 90 + 180 * random()
    phiI2 = 360 * random()
    cos_thetaI2 = -1 + 2 * random()
    thetaI2 = np.rad2deg(np.arccos(cos_thetaI2))-90
    #thetaI2 = 90 + 180 * random()
    stretch = 0.15 + 0.85 * random()
    #stretch = 4

    # stretch = 10
    tchange = [200 * random()]

    return phiI, thetaI, stretch, tchange, phiI2, thetaI2
