# recordingsort
automatic abf sorter and trace image creator

requirements:
- csv of files to be moved laid out with the following headers (in any order):

|| location || first_file || last_file || destination ||

NOTE: directories with the destination names will be created in the directory containing the csv file uploaded to recording_sort.py

- abf files must have the standard naming convention:

YYMDD###

- python3+ with the following packages:

|| pyabf || pandas ||