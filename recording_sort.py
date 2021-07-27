'''
recording_sort accomplishes the following:
- reads in a csv file
- creates directory based on a certain column
- creates range of abf file numbers to move
- moves those files to their respective directories
- uses create_image to make a .png of the traces, then saves those traces to the correct directories
'''

from create_image import create_image
import pandas as pd

