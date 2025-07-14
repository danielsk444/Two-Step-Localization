import random
import matplotlib.pyplot as plt

def custom_distribution(rmax):
    # Calculate probabilities for each number from 1 to rmax
    probabilities = [3 * (i**2) / rmax for i in range(1, rmax + 1)]
    # Normalize probabilities to sum up to 1
    total_prob = sum(probabilities)
    probabilities = [prob / total_prob for prob in probabilities]
    return probabilities

def choose_number(rmax):
    probabilities = custom_distribution(rmax)
    numbers = list(range(1, rmax + 1))
    chosen_number = random.choices(numbers, probabilities)[0]
    return chosen_number


def size_lotto(run):
    if  run == 3:
        rmax=140
    elif run == 4:
        rmax=160.
    elif run == 5:
        rmax=325
    dis= choose_number(int(rmax))
    #GW170817
    #snr_dis=32.4/40
    #snr=dis*snr_dis

    return dis