from gauge import gauge
def after_sim( ramove, decmove, rachange, decchange):
    ramove, decmove = gauge(ramove, decmove)
    rachange, decchange = gauge(rachange, decchange)
    return ramove, decmove, rachange, decchange

