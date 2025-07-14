import healpy as hp
import matplotlib.pyplot as plt

def plot_fits(hpx):
    hp.mollview(hpx)
    hp.graticule()
    plt.show()