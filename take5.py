
import csv

#
# 5 numbers
# 

numbers_file_csv = 'data/5numbers.csv'

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

numbers_dl = import_csv_data_as_dictlist(numbers_file_csv)

i =0
for entry in numbers_dl:
    print (i, ' ', entry)
    i += 1

print("done.")