'''
recording_sort accomplishes the following:
- reads in a csv file via pandas
- creates directory based on a certain column
- creates range of abf file numbers to move
- moves those files to their respective directories
- uses create_image to make a .png of the traces, then saves those traces to the correct directories
'''

from create_image import create_image
import pandas as pd
import shutil, os

csv_path = input("Enter csv file location: ")
csv_file = input("Enter csv file name: ")
df = pandas.read_csv(f'{csv_path}/{csv_file}.csv')

load_count = 0
for index, row in df.iterrows():
    print("\r" + f'{load_count}/{len(df)}', end="")
    os.mkdir(f'{csv_path}/{row['destination']}')
    files = range(row[first_file], row[last_file])

    for file in files:
        shutil.copy(f'{row['location']}/{file}.abf', f'{csv_path}/{row['destination']}/')
        create_image(file, row['location'], f'{csv_path}/{row['destination']}')
    
    load_count += 1
    
