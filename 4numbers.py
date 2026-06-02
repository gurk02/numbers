
import csv
import pprint
import numpy as np
import pandas as pd


numbers_file_csv = 'data/4numbers.csv'

#
#import data
#
def import_csv_data_as_dataframe(df):    
    print(f"importing data file {df}")



def import_csv_data_as_dictlist(df):
    # read the numbers from the csv file
    # store them in a list of dictionaries
    with open(df, 'r') as f: 
        reader = csv.DictReader(f)   # instaniate a dictreader from obj file f
        num_dict_list = list(reader)  # convert dictreader to list of dictionaires
    return num_dict_list

#
# 
#


#
# main
#

print("start.")
numbers_dl = import_csv_data_as_dictlist(numbers_file_csv)

#
# calculate
#
n1 = np.arange(len(numbers_dl))
n2 = []
n3 = []
n4 = []

n1_cnt = [0,0,0,0,0,0,0,0,0,0]
i=0
for entry in numbers_dl:
    n1[i] = (int(entry['n1']))
    n1_cnt[n1[i]] += 1
    #print(f"i {i}, n1 {entry['n1']}")
    i +=1
   
# frequency distribution 
n = 0
freq_dist_header = ""
freq_dist = ""
for num_count in n1_cnt:
    freq_dist_header += f"\t{n}"
    freq_dist += f"\t{num_count} "
    n +=1

print(f"{freq_dist_header}")
print(f"{freq_dist}")

series = pd.Series(n1)
print(series)

print("done.")