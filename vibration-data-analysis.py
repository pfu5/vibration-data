import csv
from itertools import count
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy.fft import rfft, rfftfreq
import numpy as np


def get_accel(filename):

    time_log = []

    accel_x = []
    accel_y = []
    accel_z = []
    all_accel = []

    column_time_idx = 0
    column_x_idx = 1
    column_y_idx = 2
    column_z_idx = 3

    with open(filename, newline="") as csvfile:
        time_log = [row[column_time_idx] for row in csv.reader(csvfile)]

    column_x_idx = 1
    with open(filename, newline="") as csvfile:
        accel_x = [row[column_x_idx] for row in csv.reader(csvfile)]

    column_x_idx = 2
    with open(filename, newline="") as csvfile:
        accel_y = [row[column_y_idx] for row in csv.reader(csvfile)]

    column_x_idx = 3
    with open(filename, newline="") as csvfile:
        accel_z = [row[column_z_idx] for row in csv.reader(csvfile)]
    all_accel = [time_log, accel_x, accel_y, accel_z]

    return all_accel


def make_raw_plot(time_log, accel, axis):
    ax = plt.axes()
    time_log = [float(n) for n in time_log]
    accel = [float(n) for n in accel]

    ax.xaxis.set_major_locator(ticker.MaxNLocator(10))
    ax.yaxis.set_major_locator(ticker.MaxNLocator(16))
    
    title = "Vibration Over Time in " + axis
    plt.xlabel("Time (s)")
    plt.ylabel("Acceleration (g)")
    plt.title(title)
    plt.plot(time_log, accel)
    plt.tight_layout()
    plt.grid()
    plt.show()


def get_fft_plot(time_log, accel, axis):

    time_log = [float(n) for n in time_log]
    accel = [float(n) for n in accel]

    n = len(time_log)
    data_step = 0.000249
    yf = rfft(accel)
    xf = rfftfreq(n, data_step)
    plt.plot(xf, np.abs(yf))
    plt.grid()
    title = "Frequency Domain Data in " + axis
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Occurance")
    plt.title(title)
    plt.show()


def main():

    filename = (
        "FrontRightLidarMount_FullSpeedLap_FN_SSC09622_193.csv"
        # "UnderAK_FullSpeedLap_FN_DAQ11945_000133.csv"  
        # "FrontRightLidarTop_FullSpeedLap_DAQ11945_000137_Ch80_40g_DC_Acceleration.csv"
        #"MastSensorBox_FullSpeedLap1_DAQ11945_000135_Ch80_40g_DC_Acceleration.csv"
        # "MastSensorBox_FullSpeedLap2_DAQ11945_000136_Ch80_40g_DC_Acceleration.csv"
        # "test_data.csv"
    )
    all_accel = get_accel(filename)
    time_log = all_accel[0]
    accel_x = all_accel[1]
    accel_y = all_accel[2]
    accel_z = all_accel[3]

    ### Print max and min values:
    def list_min(str_list):
        return str(min([float(n) for n in str_list]))
    def list_max(str_list):
        return str(max([float(n) for n in str_list]))  
    
    print('Time - Min value: ' + list_min(time_log))
    print('Time - Max value: ' + list_max(time_log))
    print('X - Min value: ' + list_min(accel_x))
    print('X - Max value: ' + list_max(accel_x))
    print('Y - Min value: ' + list_min(accel_y))
    print('Y - Max value: ' + list_max(accel_y))
    print('Z - Min value: ' + list_min(accel_z))
    print('Z - Max value: ' + list_max(accel_z))

    ### Plot raw data set:
    # make_raw_plot(time_log, accel_x, "X-Axis")
    # make_raw_plot(time_log, accel_y, "Y-Axis")
    # make_raw_plot(time_log, accel_z, "Z-Axis")

    ### Plot fft data set:      
    # get_fft_plot(time_log, accel_x, "X-Axis") # 0.31 Hz & 42.66 Hz
    # get_fft_plot(time_log, accel_y, "Y-Axis") # 0.09 Hz & 10.11 Hz
    # get_fft_plot(time_log, accel_z, "Z-Axis") # 10 Hz & 12.53 Hz & 32.77 Hz


if __name__ == "__main__":
    main()
