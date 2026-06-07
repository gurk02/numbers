
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


n1 = np.arange(len(numbers_dl))
n2 = []
n3 = []
n4 = []

n1_cnt = [0,0,0,0,0,0,0,0,0,0]
n1_mid_cnt = [0,0,0,0,0,0,0,0,0,0]
n1_eve_cnt = [0,0,0,0,0,0,0,0,0,0]

mid_top3_cnt = [0,0,0]
mid_top3_nums = [0,0,0]
eve_top3_cnt = [0,0,0]
eve_top3_nums = [0,0,0]

# def n1_cnt():
#     i=0
#     for entry in numbers_dl:
#         n1[i] = (int(entry['n1']))
#         n1_cnt[n1[i]] += 1
#         #print(f"i {i}, n1 {entry['n1']}")
#         i +=1
#     return 1

#
# calculate
#

i = 0
for entry in numbers_dl:
    n1[i] = int(entry['n1']) #extract n1 from each line entry
    n1_cnt[n1[i]] += 1
    if entry['draw']=='MID':
        n1_mid_cnt[n1[i]] += 1
    elif entry['draw']=='EVE':
        n1_eve_cnt[n1[i]] += 1

    #print(f"i {i}, n1 {n1[i]}")
    i += 1


#
# Reports
#
print("REPORTS")
print(n1)
print(n1_cnt)
print(n1_mid_cnt)
print(n1_eve_cnt)

# 
# frequency distribution 
#
n = 0
freq_dist_header = ""
freq_dist = ""
for num_count in n1_cnt:
    freq_dist_header += f"\t{n}"
    freq_dist += f"\t{num_count} "
    n +=1

print(f"{freq_dist_header}")
print(f"{freq_dist}")

#
# mid
#
print("mid")
n = 0
for num_count in n1_mid_cnt:
    print(f"{n}", "=" * num_count)
    n += 1

print("\n\n")

#
# eve
#
print("eve")
n = 0
for num_count in n1_eve_cnt:
    print(f"{n}", "=" * num_count)
    n += 1



#
# find top3 - ascending order 46,43, 40
#
def find_top3(numbers,top3,nums):
        debug = False
        n = 0
        if debug == True:
            print (f"top3 {top3} top3 len {len(top3)}")
        while n < len(numbers):
            number = numbers[n]
            if debug == True:
               print(f"{n}, checking number{number}")

            top_idx = 0
            while top_idx < len(top3):      # scan each top numbers
                #print(f"top_number {top_number} top3_{top3[top_number]}")
                if debug == True:
                    print(f"compare {number} at idx {top_idx} top_number {top3[top_idx]}")
                if number > top3[top_idx]: #found new top3 number
                    # new number found!: shift down all top3 numbers
                    if debug == True:
                        print(f"new top number found {number} top_idx {top_idx}")

                    idx = top_idx
                    swap1_cnt = -1
                    swap2_cnt = -1
                    swap1_num = -1
                    swap2_num = -1
                    while idx < len(top3):          # new number found!: shift down all top3 numbers
                        if swap1_cnt == -1:
                            swap1_cnt = top3[idx]
                            swap1_num = nums[idx]
                            top3[idx] = number
                            nums[idx] = n
                        else:
                            swap2_cnt = top3[idx]
                            swap2_num = nums[idx]
                            top3[idx] = swap1_cnt
                            nums[idx] = swap1_num
                            swap1_cnt = swap2_cnt
                            swap1_num = swap2_num
                        if debug == True:
                            print(f"idx{idx}, swap1={swap1_cnt}, swap2={swap2_cnt} top3[idx]={top3[idx]}")
                        idx += 1
                    break

                top_idx +=1

            n += 1
            if debug == True:
                print(f"top3 {top3}")
        return top3, nums

#
# Regression - mid
#
print("REGRESSION")
print("finding mid top3 from n1_mid_cnt{n1_mid_cnt}")
print(f"results -> {find_top3(n1_mid_cnt,mid_top3_cnt,mid_top3_nums)}")
print (mid_top3_cnt)
print (mid_top3_nums)

tag_mid_top3_nums = ""
for n in n1:
    if n == mid_top3_nums[0]:
         tag_mid_top3_nums += f" {n}*"
    elif n == mid_top3_nums[1]:
         tag_mid_top3_nums += f" {n} "
    elif n == mid_top3_nums[2]:
        tag_mid_top3_nums += f" {n} "
    else:
       tag_mid_top3_nums += f" {n} "

print("tag mid top3 numbers")
print(tag_mid_top3_nums)

#
# Regression - eve
#

print("finding eve top3 from n1_eve_cnt{n1_eve_cnt}")
print(f"results -> {find_top3(n1_eve_cnt,eve_top3_cnt,eve_top3_nums)}")
print (eve_top3_cnt)
print (eve_top3_nums)


# tag_eve_top3_nums = ""
# for n in n1:
#     if n == eve_top3_nums[0]:
#          tag_eve_top3_nums += f" {n}*"
#     elif n == eve_top3_nums[1]:
#          tag_eve_top3_nums += f" {n} "
#     elif n == eve_top3_nums[2]:
#         tag_eve_top3_nums += f" {n} "
#     else:
#        tag_eve_top3_nums += f" {n} "

# print("tag eve top3 numbers")
# print(tag_eve_top3_nums)

pattern = [ 9, 3,  2,  8,  8,  9,  0,  6,  7,  9,  2,  1, 3,  8,  3,  5,  1]

series = pd.Series(n1)
print(series)

print("done.")