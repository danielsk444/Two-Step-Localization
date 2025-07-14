from is_it_here import is_it_here
from calc_ipix import calc_ipix

def timearrs_trunc(timearrs1,timearrs2,phis1,thetas1,passedra1,passeddec1 , nside,scanned_ra,scanned_dec,scanned_time):

    # Mask logic based on timearrs1 and timearrs2
    if timearrs1[-1] > timearrs2[-1]:
        mask = timearrs1 <= timearrs2[-1]

        # Apply the mask to timearrs1, phis1, and thetas1
        print("sadhhjk", len(timearrs1), len(passedra1))

        # Only apply mask to passedra1 and passeddec1 if lengths match
            # Get the removed values
        print("a")
        for j in reversed(range(len(scanned_time))):
            if scanned_time[j] > timearrs2[-1]:
                # Iterate over the passed lists in reverse.
                for i in reversed(range(len(passedra1))):
                    ipix = calc_ipix(passedra1[i], passeddec1[i], nside)
                    pixs = calc_ipix(scanned_ra[j], scanned_dec[j], nside)
                    if ipix in pixs:
                        # Remove the matched elements from both sets of lists.
                        del passedra1[i]
                        del passeddec1[i]
                        del scanned_ra[j]
                        del scanned_dec[j]
                        del scanned_time[j]  # remove scanned_time if needed
                        # Once we remove the scanned index j, we break out of the inner loop.
                        print('Bashar')
                        break
                    # iterate backwards over the indices of scanned_ra

        timearrs1 = timearrs1[mask]
        phis1 = phis1[mask]
        thetas1 = thetas1[mask]

        return scanned_ra,scanned_dec,passedra1,passeddec1,timearrs1,phis1,thetas1,scanned_time

