def calc_ipix_credible_level(ipix, credible_levels):
    credible_levels_ipix = credible_levels[ipix]
    credible_levels_ipix_09 = credible_levels[ipix] <= 0.9
    #print('credible_levels of pix no. ', ipix, 'is', credible_levels_ipix)
    #print('Is pix no.', ipix, ' credible level <= 0.9 - ', credible_levels_ipix_09)
    return credible_levels_ipix, credible_levels_ipix_09

