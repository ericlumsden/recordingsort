# Utilizes pyabf and matplotlib to create an image of the trace being sorted and save to the created directory

import pyabf
import matplotlib.pyplot as plt

def create_image(abf_file_name, abf_file_location, destination):
    plt.figure(0)
    abf = pyabf.ABF(f"{abf_file_location}{abf_file_name}.abf")
    for sweep in abf.sweepList:
        abf.setSweep(sweep=sweep, channel=0)
        plt.plot(abf.sweepX, abf.sweepY, label=f'sweep#_{sweep}')
    
    plt.xlabel('time (s)')
    plt.ylabel('current (pA)')
    plt.title(f'{abf_file_name}')

    plt.savefig(f'{destination}/{abf_file_name}.png')

    return None