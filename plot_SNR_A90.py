from snr_buildN import snr_buildN
from localization_generator import localization_generator
import matplotlib.pyplot as plt

snr1=[]
snr2=[]
snr3=[]
snr4=[]
A901=[]
A902=[]
A903=[]
A904=[]
distances=[]
for i in range (100):
    A90,theta,phi,psi,I,SNRs,dis,D=localization_generator(5,[50,29,15,2])
    snr1.append(SNRs[0])
    snr2.append(SNRs[1])
    snr3.append(SNRs[2])
    snr4.append(SNRs[3])
    A901.append(A90[0])
    A902.append(A90[1])
    A903.append(A90[2])
    A904.append(A90[3])
    distances.append(dis)



# Check the lengths of the data lists
print(f"Lengths of data lists:")
print(f"SNR1: {len(snr1)}")
print(f"SNR2: {len(snr2)}")
print(f"SNR3: {len(snr3)}")
print(f"SNR4: {len(snr4)}")
print(f"A901: {len(A901)}")
print(f"A902: {len(A902)}")
print(f"A903: {len(A903)}")
print(f"A904: {len(A904)}")
print(f"Distances: {len(distances)}")

# Create a figure and a set of subplots (2 rows, 5 columns)
fig, axs = plt.subplots(2, 5, figsize=(25, 10), sharey=True)

# Titles for each subplot
titles = ['SNR 1', 'SNR 2', 'SNR 3', 'SNR 4', 'A1', 'A2', 'A3', 'A4', 'Distances']

# Data for each subplot
data = [snr1, snr2, snr3, snr4, A901, A902, A903, A904, distances]

# Check if there are more datasets than subplots
if len(data) > len(axs.flat):
    print(f"Warning: There are more datasets ({len(data)}) than subplots ({len(axs.flat)})")

# Plot each histogram in the correct subplot
for i, ax in enumerate(axs.flat):
    if i < len(data):  # Check if index is within the range of the data
        ax.hist(data[i], bins=100, alpha=0.7, edgecolor='black')
        ax.set_title(titles[i])
        ax.set_xlabel('Value')
        ax.set_ylabel('Frequency')
    else:
        ax.set_visible(False)  # Hide extra subplots if there are more than necessary

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()
