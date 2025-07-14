import healpy as hp

def read_map(file_name):
    hpx = hp.fitsfunc.read_map(file_name)
    print('hpx=', hpx)
    return hpx