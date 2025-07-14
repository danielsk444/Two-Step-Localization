import numpy as np
from calc_ipix import calc_ipix


def is_kmean_scanned(pointsra, pointsdec, y, pointslabels, scanned_pix, nside):
    # Convert inputs to NumPy arrays
    pointsra = np.array(pointsra)
    pointsdec = np.array(pointsdec)
    pointslabels = np.array(pointslabels)

    # Create a boolean mask for points with the label `y`
    mask = pointslabels == y

    # Filter RA and Dec values for the relevant points
    filtered_ra = pointsra[mask]
    filtered_dec = pointsdec[mask]

    # Calculate the pixel indices for the filtered points
    pix = np.array([calc_ipix(ra, dec, nside) for ra, dec in zip(filtered_ra, filtered_dec)])

    # Convert scanned_pix to a set for faster membership checks
    scanned_pix_set = set(scanned_pix)

    # Count the number of pixels that are in the scanned_pix set
    scanned_count = sum(p in scanned_pix_set for p in pix)

    # Check if all points with label `y` have been scanned
    return scanned_count >= len(filtered_ra)
