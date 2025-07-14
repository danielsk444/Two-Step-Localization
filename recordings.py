import matplotlib.pyplot as plt

def recordings(tele_times,who_found_arr,phiI, thetaI, phiI2, thetaI2,rax,decx,A90,tele1,tele2,t_pre_merge,file_name,run,thetaLVK,phiLVK,psiLVK,ILVK,SNRs,track_times,dis,D,SNRs_filtered,t_pre_merge_filtered,A90_filtered ):

    # Format these variables into a string with spaces in between
    track_time1=track_times[0]
    track_time2 = track_times[1]
    track_time3 = track_times[2]

    time_dif1=track_time2-track_time1
    time_dif2=track_time3-track_time1

    new_line = f"{time_dif1} {time_dif2}  {track_time1} {track_time2} {track_time3} {tele_times} {who_found_arr[0]} {who_found_arr[1]} {who_found_arr[2]} {phiI} {thetaI} {phiI2} {thetaI2} {rax} {decx} {A90} {A90_filtered} {tele1.name} {tele2.name} {t_pre_merge} {t_pre_merge_filtered} {file_name}  {tele1.max_vel} {tele1.acc} {tele1.FOV} {run} {thetaLVK} {phiLVK} {psiLVK} {ILVK} {SNRs} {SNRs_filtered}  {dis} {D} \n"
    print('new_line',new_line)
    #plt.plot(2,2)
    #plt.show()
    # Specify the file name
    file_name = "recordingsP10_13.txt"

    # Open the file in append mode to add the new line
    with open(file_name, 'a') as file:
        file.write(new_line)

    # Optionally, read and print the updated content of the file
    with open(file_name, 'r') as file:
        updated_content = file.read()
        print(updated_content)
