import numpy as np
import os
import csv
import argparse

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# from scipy.interpolate import spline

from utils import read_csv

from settings import MEDIANS_PATH, MEDIANS_PLOT_PATH

PLOT_DPI = 500
PLOT_FORMAT = 'png'
PLOT_COLORS = [
    '#000000',
    '#000000',
    '#000000',
    '#000000',
    '#000000',
    '#000000',
    '#000000',
    '#000000',
]

Y_TOP_LIMIT = 3000
Y_BOTTOM_LIMIT = -3000

def generate_ecg_plot(ecg_data, ecg_id, save_path=None):

    if not os.path.exists(save_path):
        os.makedirs(save_path)
    
    plt.figure(dpi=PLOT_DPI)
    plt.axis('off')

    for index, row in enumerate(ecg_data):

        x = range(len(row))
        y = row

        # x_smooth = np.linspace(min(x), max(x), 600)
        # y_smooth = spline(x, y, x_smooth)
        
        plt.plot(x, y, color=PLOT_COLORS[index], linewidth=0.1)

    plt.ylim(Y_BOTTOM_LIMIT, Y_TOP_LIMIT)
    plt.savefig(os.path.join(save_path, f'{ ecg_id }.{ PLOT_FORMAT }'), format=PLOT_FORMAT)
    plt.clf()
    plt.cla()
    plt.close()

if __name__ == '__main__':

    median_files = sorted(os.listdir(MEDIANS_PATH))

    for index, ecg_file in enumerate(median_files):
        print(f'Generating plots: { index + 1 } / { len(median_files) }', end='\r')

        ecg_data = read_csv(
            os.path.join(MEDIANS_PATH, ecg_file),
            delimiter=' ',
            transpose=True,
            skip_header=False,
            dtype=np.int)

        generate_ecg_plot(ecg_data, os.path.splitext(ecg_file)[0], MEDIANS_PLOT_PATH)
    
    print('\n', end='\r')