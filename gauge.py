import matplotlib.pyplot as plt
def gauge(ra, dec):
    is_set=False
    while not is_set:
        is_set = True
        if type(dec) == list:
            for i in range(len(ra)):
                if dec[i] > 90:
                    is_set = False
                    dec[i] = 180 - dec[i]
                    if ra[i] > 180:
                        ra[i] = ra[i] - 180
                    if ra[i] < 180:
                        ra[i] = ra[i] + 180

                if dec[i] < - 90:
                    is_set = False
                    dec[i] = -180 - dec[i]
                    if ra[i] > 180:
                        ra[i] = ra[i] - 180
                    if ra[i] < 180:
                        ra[i] = ra[i] + 180
                if ra[i] > 360:
                    is_set = False
                    ra[i] = ra[i] - 360

                if ra[i] < 0:
                    is_set = False
                    ra[i] = ra[i] + 360

        elif type(dec) == int or type(dec) == float:
            if dec > 90:
                dec = -180 + dec
                is_set = False

            if dec < - 90:
                is_set = False

                dec = 180 + dec
            if ra > 360:
                print(ra)
                is_set = False
                ra = ra - 360

            if ra < 0:
                is_set = False
                ra = ra + 360



    return ra, dec
