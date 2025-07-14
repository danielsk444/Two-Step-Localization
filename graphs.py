from plot_BIG_arrival import plot_BIG_arrival
from plot_time_difs import plot_time_dif
from plot_times_runs import plot_time_runs
from plot_time_A90 import plot_time_A90
from plot_time_start_end_points import plot_time_start_end_points
from plot_time_update_times import plot_time_update_times
from plot_time_SNR import plot_time_SNR
from plot_who_foundN import plot_who_foundN
from plot_time_start_end_pointsN import plot_time_start_end_pointsN
from plot_A90_angles import plot_A90_angles
#plot_A90_angles()
file_name='recordingsN16.xlsx'
print('plot_time_dif')
plot_time_dif()

print('plot_time_runs')
plot_time_runs(file_name)

print('plot_time_update_times')
plot_time_update_times(file_name)


print('plot_who_foundN')
plot_who_foundN(file_name)

print('plot_BIG_arrival')
plot_BIG_arrival(file_name)

print('plot_time_start_end_points')
plot_time_start_end_points(file_name)

print('plot_who_foundN')
plot_who_foundN(file_name)



print('plot_time_start_end_pointsN')
plot_time_start_end_pointsN(file_name)

print('plot_time_A90')
plot_time_A90(file_name)

print('plot_time_SNR')
plot_time_SNR(file_name)
