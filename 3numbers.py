
import csv
import pprint
import numpy as np
# import pandas as pd
import random
from datetime import datetime

numbers_file_csv = 'data/3numbers.csv'
hotpicks_file_csv = 'data/3numbers_hotpicks.csv'
generated_hotpicks_combo_file_csv = 'data/3numbers_generated_hotpicks_combo.csv'

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

hotpicks_dl = import_csv_data_as_dictlist(hotpicks_file_csv)

n1 = np.arange(len(numbers_dl))
print("len N1",len(n1))
n1_mid = np.arange(int(len(numbers_dl)/2)+1)
print("n1_mid len", len(n1_mid))
n1_eve = np.arange(int(len(numbers_dl)/2)+1)
print("n1_mid len", len(n1_eve))

n2 = np.arange(len(numbers_dl))
n2_mid = np.arange(int(len(numbers_dl)/2)+1)
print("n2_mid len", len(n2_mid))
n2_eve = np.arange(int(len(numbers_dl)/2)+1)
print("n2_mid len", len(n2_eve))


n3 = np.arange(len(numbers_dl))
n3_mid = np.arange(int(len(numbers_dl)/2)+1)
print("n3_mid len", len(n3_mid))
n3_eve = np.arange(int(len(numbers_dl)/2)+1)
print("n3_mid len", len(n3_eve))

# n4 = np.arange(len(numbers_dl))
# n4_mid = np.arange(int(len(numbers_dl)/2)+1)
# print("n4_mid len", len(n4_mid))
# n4_eve = np.arange(int(len(numbers_dl)/2)+1)
# print("n4_mid len", len(n4_eve))


n1_cnt = [0,0,0,0,0,0,0,0,0,0]
n1_cnt_prec = [0,0,0,0,0,0,0,0,0,0]
n1_mid_cnt = [0,0,0,0,0,0,0,0,0,0]
n1_eve_cnt = [0,0,0,0,0,0,0,0,0,0]

n2_cnt = [0,0,0,0,0,0,0,0,0,0]
n2_cnt_prec = [0,0,0,0,0,0,0,0,0,0]
n2_mid_cnt = [0,0,0,0,0,0,0,0,0,0]
n2_eve_cnt = [0,0,0,0,0,0,0,0,0,0]

n3_cnt = [0,0,0,0,0,0,0,0,0,0]
n3_mid_cnt = [0,0,0,0,0,0,0,0,0,0]
n3_eve_cnt = [0,0,0,0,0,0,0,0,0,0]

# n4_cnt = [0,0,0,0,0,0,0,0,0,0]
# n4_mid_cnt = [0,0,0,0,0,0,0,0,0,0]
# n4_eve_cnt = [0,0,0,0,0,0,0,0,0,0]

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
i_mid = 0
i_eve = 0
for entry in numbers_dl:
    n1[i] = int(entry['n1']) #extract n1 from each line entry
    n1_cnt[n1[i]] += 1

    n1_cnt_prec[n1[i]] = round( n1_cnt[n1[i]] / len(numbers_dl) , 3)


    if entry['draw']=='MID':

        n1_mid[i_mid] = int(entry['n1'])
        n1_mid_cnt[n1[i]] += 1
        i_mid += 1

    elif entry['draw']=='EVE':
      
        n1_eve[i_eve] = int(entry['n1'])
        n1_eve_cnt[n1[i]] += 1
        i_eve += 1

    #print(f"i {i}, n1 {n1[i]}")
    i += 1


    #
    # N2
    #
i = 0
i_mid = 0
i_eve = 0
for entry in numbers_dl:
    n2[i] = int(entry['n2']) #extract n2 from each line entry
    n2_cnt[n2[i]] += 1
    
    n2_cnt_prec[n2[i]] = round( n2_cnt[n2[i]] / len(numbers_dl) , 3)


    if entry['draw']=='MID':

        n2_mid[i_mid] = int(entry['n2'])
        n2_mid_cnt[n2[i]] += 1
        i_mid += 1

    elif entry['draw']=='EVE':
      
        n2_eve[i_eve] = int(entry['n2'])
        n2_eve_cnt[n2[i]] += 1
        i_eve += 1

    #print(f"i {i}, n2 {n2[i]}")
    i += 1

        #
    # n3
    #
i = 0
i_mid = 0
i_eve = 0
for entry in numbers_dl:
    n3[i] = int(entry['n3']) #extract n3 from each line entry
    n3_cnt[n3[i]] += 1
    
    if entry['draw']=='MID':

        n3_mid[i_mid] = int(entry['n3'])
        n3_mid_cnt[n3[i]] += 1
        i_mid += 1

    elif entry['draw']=='EVE':
      
        n3_eve[i_eve] = int(entry['n3'])
        n3_eve_cnt[n3[i]] += 1
        i_eve += 1

    #print(f"i {i}, n3 {n3[i]}")
    i += 1

#     #
#     # n4
#     #
# i = 0
# i_mid = 0
# i_eve = 0
# for entry in numbers_dl:
#     n4[i] = int(entry['n4']) #extract n4 from each line entry
#     n4_cnt[n4[i]] += 1
    
#     if entry['draw']=='MID':

#         n4_mid[i_mid] = int(entry['n4'])
#         n4_mid_cnt[n4[i]] += 1
#         i_mid += 1

#     elif entry['draw']=='EVE':
      
#         n4_eve[i_eve] = int(entry['n4'])
#         n4_eve_cnt[n4[i]] += 1
#         i_eve += 1

#     #print(f"i {i}, n4 {n4[i]}")
#     i += 1

#
# Reports
#
print("\t\t***REPORTS")
# print(n1)
print("Digits N1-N2 Count Distribution")
print('N1')
# print("N1 data", n1)
print(n1_cnt)
print(n1_cnt_prec)
print(n1_mid_cnt)
print(n1_eve_cnt)
print('N2')
# print("N2 data", n2)
print(n2_cnt)
print(n2_cnt_prec)
print(n2_mid_cnt)
print(n2_eve_cnt)
print('N3')
print(n3_cnt)
print(n3_mid_cnt)
print(n3_eve_cnt)
# print('N4')
# print(n4_cnt)
# print(n4_mid_cnt)
# print(n4_eve_cnt)

debug = False

# if debug == True:
#     print('***\t\tN1 Freq Distribution')
#     # 
#     # frequency distribution 
#     #
#     n = 0
#     freq_dist_header = ""
#     freq_dist = ""
#     for num_count in n1_cnt:
#         freq_dist_header += f"\t{n}"
#         freq_dist += f"\t{num_count} "
#         n +=1

#     print(f"{freq_dist_header}")
#     print(f"{freq_dist}")

#     #
#     # mid
#     #
#     print("mid")
#     n = 0
#     for num_count in n1_mid_cnt:
#         print(f"{n}", "=" * num_count)
#         n += 1

#     print("\n\n")

#     #
#     # eve
#     #
#     print("eve")
#     n = 0
#     for num_count in n1_eve_cnt:
#         print(f"{n}", "=" * num_count)
#         n += 1



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
# print("\n\n")
# print("\t\t***REGRESSION")
# print("finding mid top3 from n1_mid_cnt{n2_mid_cnt}")
# print(f"N2 MID results -> {find_top3(n4_mid_cnt,mid_top3_cnt,mid_top3_nums)}")
# print (mid_top3_cnt)
# print (mid_top3_nums)

# tag_mid_top3_nums = ""
# for n in n1_mid:
#     if n == mid_top3_nums[0]:
#          tag_mid_top3_nums += f" {n}*"
#     elif n == mid_top3_nums[1]:
#          tag_mid_top3_nums += f" {n} "
#     elif n == mid_top3_nums[2]:
#         tag_mid_top3_nums += f" {n} "
#     else:
#        tag_mid_top3_nums += f" {n} "

# # print("tag mid top3 numbers")
# # print(tag_mid_top3_nums)

# #
# # Regression - eve
# #
# print("\n\n")
# print("finding eve top3 from n1_eve_cnt{n2_eve_cnt}")
# print(f"N2 EVE results -> {find_top3(n4_eve_cnt,eve_top3_cnt,eve_top3_nums)}")
# print (eve_top3_cnt)
# print (eve_top3_nums)


# tag_eve_top3_nums = ""
# for n in n1_eve:
#     if n == eve_top3_nums[0]:
#          tag_eve_top3_nums += f" {n}*"
#     elif n == eve_top3_nums[1]:
#          tag_eve_top3_nums += f" {n} "
#     elif n == eve_top3_nums[2]:
#         tag_eve_top3_nums += f" {n} "
#     else:
#        tag_eve_top3_nums += f" {n} "

# # print("tag eve top3 numbers")
# # print(tag_eve_top3_nums)

# # pattern = [ 9, 3,  2,  8,  8,  9,  0,  6,  7,  9,  2,  1, 3,  8,  3,  5,  1]


#
# Find N1 Hot Pattern
#

    #
    # find hot number
    #
rate_of_change_sensitive = [5, 7, 10, 12, 15, 17, 20, 22, 25 ] # from tighter rate to most related
def hot_pick(row_draw_cnt, num, seen_count, diff_last_seen_draw, prev_diff_last_seen_draw, prev_last_seen_loc, last_seen_rate_change):
    hot_pick_dial = 0
    # if seen_count > 1 and diff_last_seen_loc < 6 and (last_seen_rate_change > -5 and last_seen_rate_change < 5):
    #     return True
    # else:
    #     return False     # steps diff from 1st and 2nd last seen  # rate > -15 means compacting   and rate < 5 means compacting still everything else means expanding              
    # if seen_count > 1 and diff_last_seen_draw < 7 and prev_diff_last_seen_draw < 7 and (last_seen_rate_change > -15 and last_seen_rate_change < 5):
    # if seen_count > 1 and ((diff_last_seen_draw <= 7 and prev_diff_last_seen_draw <= 7) or (last_seen_rate_change > -10 and last_seen_rate_change < 5)): # ok: default rule works decent 7/4/26
    # if seen_count > 1 and (last_seen_rate_change >= -10 and last_seen_rate_change <= 10):   # rate_of_change_sensitive[2] = 10 for every 10 draws check pattern exists
    if seen_count > 1 and (last_seen_rate_change >= -10 and last_seen_rate_change <= 10):   #modified for 3 numbers instead of five numbers # rate_of_change_sensitive[2] = 10 for every 10 draws check pattern exists

        return True
    else:
        return False


def gen_pairs():
    layer1 = [0,1, 2,3, 4,5, 6,7, 8,9]
    layer2 = [0,1, 2,3, 4,5, 6,7, 8,9]
    pairs=[]
    cnt = 0

    for i in layer1:
        for j in layer2:
            pairs.append((i,j))
            print(f"{i},{j}")   
            cnt += 1

    print(f"total pairs {cnt}")     
    return pairs

# def get_high(numbers):
#     high = numbers[0]
#     high_idx = 0
#     idx = 0
#     for i in numbers:
#         if i > high:
#             high = i
#             high_idx = idx
#         idx += 1

#     # print(f"high_idx {high_idx} high {high}")
#     return high_idx

def get_high(numbers, start, end):
    high = numbers[start]
    high_idx = start
    idx = start
    for i in numbers[start:end]:
        if i > high:
            high = i
            high_idx = idx
        idx += 1

    # print(f"high_idx {high_idx} high {high}")
    return high_idx


# def get_lowest(numbers):
#     low = numbers[0]
#     low_idx = 0
#     idx = 0
#     for i in numbers:
#         # print (f"idx{idx}, i {i}, low{low}")
#         if i < low:
#             low = i
#             low_idx = idx
        
#         idx += 1

#     return low_idx

def get_lowest(numbers, start, end):
    low = numbers[start]
    low_idx = start
    idx = start
    for i in numbers[start:end]:
        # print (f"idx{idx}, i {i}, low{low}")
        if i < low:
            low = i
            low_idx = idx
        
        idx += 1

    return low_idx

n1_ppoints = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
n1_cnt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
prev_n1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
curr_n1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
pred_n1 = 5
n1_cnt_sorted = []
n1_match_cnt = 0
n1_below_five = 0
n1_above_five = 0
n1_at_five = 0


def calculate_n1_ppattern_V1(pattern):
    print('\t calculate_n1_ppattern')
    n1_match_cnt = 0
    n1_below_five = 0
    n1_above_five = 0
    n1_at_five = 0
    prev_num1 = 0
    curr_num1 = 0
    last_num_lower = False

    # gen_pairs()
    # exit()

    for n in pattern:

        # if n == 5:
        #     n1_at_five += 1
        # elif n < 5:    
        #     n1_below_five += 1
        # else: 
        #     n1_above_five += 1
        
        # print(f"at_five {n1_at_five} below_five {n1_below_five} above_five {n1_above_five}")
        print(f"prev_num1 {prev_num1} curr_num1 {curr_num1} n {n}")

        if n1_below_five == n1_above_five:
            # 50 - 50 split go with opposite last seen
            if last_num_lower == True:
                pred_n1 = get_high(n1_ppoints, 5, 9)
            else:
                pred_n1 = get_high(n1_ppoints, 0, 5)
            # last_num_lower = not last_num_lower

        elif n1_below_five > n1_above_five:
            pred_n1 = get_high(n1_ppoints, 5, 9)
        elif n1_above_five > n1_below_five:
            pred_n1 = get_high(n1_ppoints, 0, 5)
        else:
            pred_n1 = get_high(n1_ppoints, 0, 9)

        # pred_n1 = get_high(n1_ppoints)
        #pred_n1 = get_high(n1_ppoints)
        # pred_n1 = 4
        print(f"pred_n1 {pred_n1}")
        
          
        if n == pred_n1:
            n1_ppoints[pred_n1] += 1
            n1_match_cnt += 1
            print(f"{n} Match {pred_n1}? Y")
        else:
            print(f"{n} Match {pred_n1}? N")
            n1_ppoints[pred_n1] -= 1

        print(f"n {n}, prev_n1 {prev_n1[n]}, curr_n1 {curr_n1[n]}", f"\nn1_cnt {n1_cnt}",f"\nn1_ppoints {n1_ppoints}\n")

        n1_cnt[n] += 1
        if n == 5:
            n1_at_five += 1
        elif n < 5:    
            n1_below_five += 1
        else: 
            n1_above_five += 1
        
        prev_num1 = curr_num1
        curr_num1 = n
        
        if n < 5:
            last_num_lower = True
        else:
            last_num_lower = False

        print(f"at_five {n1_at_five} below_five {n1_below_five} above_five {n1_above_five}")

    print(f"match_cnt {n1_match_cnt} pattern len {len(pattern)} win_rate {int((n1_match_cnt / len(pattern)) * 100)}")

def calculate_n1_ppattern_V2(pattern):
    print('\t calculate_n1_ppattern V2')
    n1_match_cnt = 0
    n1_below_five = 0
    n1_above_five = 0
    prev_num1 = 0
    curr_num1 = 0

    # gen_pairs()
    # exit()

    direction = ""
    direction_rate = 0
    below_five_prec = 0
    above_five_prec = 0

    below_five_cnt = 0
    above_five_cnt = 0
    i_cnt = 0

    for n in pattern:

        print(f"prev_num1 {prev_num1} curr_num1 {curr_num1} n {n}")

        # decision rules here

        if below_five_prec > 50:
            print("go high")
            direction="high"
            pred_n1 = get_high(n1_ppoints, 0, 5)
        elif above_five_prec > 50:
            print("go low")
            direction="low"
            pred_n1 = get_high(n1_ppoints, 0, 5)
        elif n1_below_five > n1_above_five:
            print("go low")
            direction="low"
            pred_n1 = get_high(n1_ppoints, 0, 5)
        elif n1_below_five < n1_above_five:
            print("go high")
            direction="high"
            pred_n1 = get_high(n1_ppoints, 5, 9)
        else:
            # 0 point tied flip a coin or random or opposite last direction high or low
            if direction == "low":
                # go high
                print("go high")
                direction="high"
                pred_n1 = get_high(n1_ppoints, 5, 9)
            elif direction == "high":
                # go low - opposite
                direction="low"
                pred_n1 = get_high(n1_ppoints, 0, 5)
            else:
                # undecided go with next in line all range
                print("go all range")
                direction="all"
                pred_n1 = get_high(n1_ppoints, 0, 9)


        # pred_n1 = get_high(n1_ppoints)
        #pred_n1 = get_high(n1_ppoints)
        # pred_n1 = 4
        print(f"pred_n1 {pred_n1}, below_five {n1_below_five} above_five {n1_above_five} direction {direction}")
        
        # predict
        if n == pred_n1:
            n1_ppoints[pred_n1] += 1
            n1_match_cnt += 1
            print(f"{n} Match {pred_n1}? Y")
        else:
            print(f"{n} Match {pred_n1}? N")
            n1_ppoints[pred_n1] -= 1

        print(f"n {n}, prev_n1 {prev_n1[n]}, curr_n1 {curr_n1[n]}", f"\nn1_cnt {n1_cnt}",f"\nn1_ppoints {n1_ppoints}")


        # calcutaions 
        n1_cnt[n] += 1
        i_cnt += 1 

        if n < 5:    
            n1_below_five += 1
            n1_above_five -= 1
        else: 
            n1_above_five += 1
            n1_below_five -= 1
    
        if n < 5:
            below_five_cnt += 1
        elif n >=5:
            above_five_cnt += 1

        below_five_prec = int((below_five_cnt / i_cnt) * 100)
        above_five_prec = int((above_five_cnt / i_cnt) * 100)
        
        # direction_rate = int(())
        prev_num1 = curr_num1
        curr_num1 = n

        #report
        print(f"below_five {n1_below_five} above_five {n1_above_five} below_five_cnt{below_five_cnt} below_five_prec{below_five_prec} %, above_five_cnt{above_five_cnt} above_five_prec{above_five_prec} %")
        print("\n")
    

    #final report outcomes
    print(f"match_cnt {n1_match_cnt} pattern len {len(pattern)} win_rate {int((n1_match_cnt / len(pattern)) * 100)}")


#
# Calculate Hot Pattern Data - last saw, count, diff last saw, rate of change of last saw
#
def calculate_pattern(pattern):
    # print("pattern ", pattern)
    
    calculate_n1_ppattern_V2(pattern)
    exit()

    i = 0   # current count draws
    prev_cnt = 0 # previous count draws since last seen
    find_number_count = 0
    draw_number_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    prev_draw_number_count = 0
    last_seen_draw_loc = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    diff_last_seen_draw = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    hot_picks =  [False, False, False, False, False, False, False, False, False, False]
    hot_picks_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    debug = False
    debug = True
    i = 0
    total_draws = len(pattern)
    print("calculate_pattern - total draws ", total_draws)
    mean_draw_number_count = 0
    if debug == True:
        print (i, " ", "n", "s_cnt", " steps_diff", " ", "steps_diff_prev", " ", "steps_diff", " ", "HP")
    
    prev_n = 0
    n1_n2_spread = 0

    pattern_spreads = []
    total_nums_val = 0
    below_five = 0
    above_five = 0
    at_five = 0
    spread_five = 0
    for n in pattern:
        i += 1
        total_nums_val += n

        draw_number_count[n] +=1
        if n == 5:
            at_five += 1 
        elif n < 5:
            below_five += 1
        elif n > 5:
            above_five += 1

        spread_five = n - 5

        #
        # rate of last seen
        #
        prev_last_seen_draw_loc = last_seen_draw_loc[n]
        last_seen_draw_loc[n] = i

        prev_diff_last_seen_draw = diff_last_seen_draw[n]
        diff_last_seen_draw[n] = last_seen_draw_loc[n] - prev_last_seen_draw_loc
    
        # rate_of_change =  prev_diff_last_seen_draw - diff_last_seen_draw[n]

        rate_of_change =  diff_last_seen_draw[n] - prev_diff_last_seen_draw

        n1_n2_spread = int(n - prev_n)

        if hot_pick(i, n, draw_number_count[n], diff_last_seen_draw[n],  prev_diff_last_seen_draw, prev_last_seen_draw_loc, rate_of_change) == True:
            if debug == True:
                print(i," ",n, draw_number_count[n],diff_last_seen_draw[n], " ",prev_diff_last_seen_draw, " ", rate_of_change, "HP", hot_picks_count[n]+1, '\t', n,prev_n, n1_n2_spread, ' ', 'at_five',at_five, 'below_five', below_five, 'above_five', above_five, 'spread_five', spread_five)
            hot_picks[n] = True
            hot_picks_count[n] += 1
        else:
            # hot_picks[n] = False
            if debug == True:
                print(i," ",n, draw_number_count[n], diff_last_seen_draw[n], " ",prev_diff_last_seen_draw, " ", rate_of_change, "    ", '\t',n,prev_n, n1_n2_spread, ' ', 'at_five',at_five, 'below_five', below_five, 'above_five', above_five,'spread_five', spread_five)
        
        prev_n = n
        pattern_spreads.append(n1_n2_spread)

    print('mean distribution: ', total_nums_val/i)
    print('at_five',at_five, 'below_five', below_five, 'above_five', above_five)
    print('pattern_spreads,', len(pattern_spreads), pattern_spreads)
    
    for s in pattern_spreads:
        print('=' * abs(s))

    return hot_picks, draw_number_count, hot_picks_count 


# debug = False
# print("calulcate N1 hot picks")
# hot_picks = calculate_pattern(n1[::-1])
# i = 0 
# for hot_pick in hot_picks:
#     if hot_pick == True:
#         print(i)
#     i += 1

debug = False

def generate_numbers(digit, draw_time, sample_arr, sampling_draws):

    debug = False

    # sampling_arr = n1_eve
    sampling_arr = sample_arr
    sample_draws = len(sample_arr)
    if sampling_draws > 0:
        sample_draws = sampling_draws
    print("\n\n")
    print('sample draws', sample_draws)
    # sampling_draws =  [14, 30, 90, len(sampling_arr)]
    # sample_draws = sampling_draws[3]

    print("len of sampling_arr[:sample_draws] ",len(sampling_arr[:sample_draws]))

    if digit == '':
        digit = 'unknown'
    if draw_time == '':
        draw_time = 'unknown'

    # print(test_pattern)
    print("calculate_pattern ...")
    hot_picks, draw_number_count, hot_picks_count = calculate_pattern(sampling_arr[:sample_draws])
    print("draw number count ", draw_number_count)
    draw_count_top3_nums = [0, 0, 0]
    draw_count_top3_cnt = [0, 0, 0]
    pattern_hot_picks_top3_nums = [0, 0, 0]
    pattern_hot_picks_top3_cnt = [0, 0, 0]

    print("\n\n")
    print(f"\t\t***calulcate {digit} - {draw_time}")

    print(f"{digit} {draw_time} {sample_draws} Find Top3 Draw Count Hot Picks -> {find_top3(draw_number_count,draw_count_top3_cnt,draw_count_top3_nums)}")

    cross_ref_cnt_vs_pattern_hop_picks = [-1,-1,-1]

    debug = False
    i = 0 
    for hot_pick in hot_picks:
        # print(i," ", hot_pick)
        if debug == True:
            print(i, " ", hot_pick, " ")
            if hot_pick == True:
                print(i)
        # j = 0
        # print("checking ", i)
        # for num in hot_pick_top3_nums:
        #     if num == i and hot_pick == True:
        #         # cross referance top3 based on count vs pattern
        #         print(num, " ", j, " ", i)
        #         cross_ref_cnt_vs_pattern_hop_picks[j] = num
        #         print("break")
        #         break;
        #     j += 1
        i += 1
    

    print (f"{digit} TOP3 Draw Count PICKS -> ", draw_count_top3_nums)
    print("Pattern Hot picks Count ->",hot_picks_count)
    print ("TOP3 Pattern Hot Picks Count ->", find_top3(hot_picks_count,pattern_hot_picks_top3_cnt,pattern_hot_picks_top3_nums))

    for hot_pick_num in pattern_hot_picks_top3_nums:
        i = 0
        # print("checking ", hot_pick_num)
        for draw_count_num in draw_count_top3_nums:
            # print("against ", draw_count_num)
            if hot_pick_num == draw_count_num:
                cross_ref_cnt_vs_pattern_hop_picks[i] = hot_pick_num
                # print("ok hotpick", hot_pick_num)
                break
            i +=1

    print ("cross_ref_cnt_vs_pattern_hop_picks ", cross_ref_cnt_vs_pattern_hop_picks)
    print (f"{draw_time} All Freq Picks")
    # find_top3(n4_mid_cnt,mid_top3_cnt,mid_top3_nums)
    print (mid_top3_cnt)
    print (mid_top3_nums)
    print (eve_top3_cnt)
    print (eve_top3_nums)

    print("\t\t---RESULTS---")
    print(f"\t\t{digit} =>", )
    picks = []
    for n in cross_ref_cnt_vs_pattern_hop_picks:
        if n != -1:
            picks.append(n)
            print(n)

    # picks = cross_ref_cnt_vs_pattern_hop_picks
    
    # print ('picks -> ', picks)
    # return picks
    return picks, draw_count_top3_nums ,pattern_hot_picks_top3_nums


#
# GENERATE - numbers by count and pattern, also their generated combos  dump to files
#
def dump_to_file(file, data, mode):
    debug = False
    if debug == True:
        print (f"file {file}, {mode}, {data}")
    
    if file == '':
        return False

    if mode != 'w' and mode != 'a' and mode != '+':
        return False
    
    if debug == True:
        print (f"writing to file {file} {mode}, {data}")

    with open(file, mode) as f:
        f.write(data)

    return True

                   # element 3 - get all
sampling_draws =  [14, 21, 30, 90, 120, 365, len(n1)]
draw_sz = sampling_draws[2]  
draw_sz = sampling_draws[5]
draw_sz = sampling_draws[2]
draw_sz = sampling_draws[5]
draw_sz = sampling_draws[2]
# draw_sz = sampling_draws[5]
draw_sz = sampling_draws[2]
draw_sz = sampling_draws[1]
# draw_sz = sampling_draws[0]

# draw_sz = 15
# draw_sz = 10
draw_sz = 100
draw_sz = 30
draw_sz = 21
# draw_sz = 14

draw_types = ['MID', 'EVE', 'ALL']
draw_type = draw_types[1]
# draw_type = draw_types[0]
# sample_arr_n1 = n1_mid
# sample_arr_n2 = n2_mid
# sample_arr_n3 = n3_mid
# sample_arr_n4 = n4_mid

draw_type = draw_types[1]   # EVE
# draw_type = draw_types[0] # MID

sample_arr_n1 = n1_eve
sample_arr_n2 = n2_eve
sample_arr_n3 = n3_eve
# sample_arr_n1 = n1_mid
# sample_arr_n2 = n2_mid
# sample_arr_n3 = n3_mid
# sample_arr_n4 = n4_eve

n1_picks, n1_draw_count_top3_nums ,n1_pattern_hot_picks_top3_nums = generate_numbers('N1', draw_type,sample_arr_n1,draw_sz)
print("generate numbers for N1 ...", n1_picks)

n2_picks, n2_draw_count_top3_nums ,n2_pattern_hot_picks_top3_nums = generate_numbers('N2', draw_type,sample_arr_n2,draw_sz)
print("generate numbers for N2 ...", n2_picks)

n3_picks, n3_draw_count_top3_nums ,n3_pattern_hot_picks_top3_nums = generate_numbers('N3', draw_type,sample_arr_n3,draw_sz)
print("generate numbers for N3 ...", n3_picks)

# n4_picks, n4_draw_count_top3_nums ,n4_pattern_hot_picks_top3_nums = generate_numbers('N4', draw_type,sample_arr_n4,draw_sz)
# print("generate numbers for N4 ...", n4_picks)

# date,draw,sampledrawsize,type,n1,n2,n3,n4

# already_recorded = false
# for entry in hotpicks_dl:
#     if entry['date'] == datetime.today().strftime("%m/%d/%Y"):


today_date = datetime.today().strftime("%m/%d/%Y")
print('\n\n\t\t***REPORT***',today_date)
print('\n')

print ('Generate Numbers of N1-N3')
# print ('N1', "\t", 'N2',"\t",  'N3',"\t",  'N4')
print ('N1', "\t", 'N2',"\t",  'N3')
print("hot numbers by count")
n = 0 
while n < 3:
    # print (n1_draw_count_top3_nums[n],"\t",n2_draw_count_top3_nums[n],"\t",n3_draw_count_top3_nums[n],"\t",n4_draw_count_top3_nums[n])
    # data = f"{today_date},{draw_type},{draw_sz},count,{n1_draw_count_top3_nums[n]},{n2_draw_count_top3_nums[n]},{n3_draw_count_top3_nums[n]},{n4_draw_count_top3_nums[n]}\n"
    print (n1_draw_count_top3_nums[n],"\t",n2_draw_count_top3_nums[n],"\t",n3_draw_count_top3_nums[n])
    data = f"{today_date},{draw_type},{draw_sz},count,{n1_draw_count_top3_nums[n]},{n2_draw_count_top3_nums[n]},{n3_draw_count_top3_nums[n]}\n"
    # print(f"dump to file {data}")
    dump_to_file(hotpicks_file_csv, data, 'a')
    n += 1

print("hot numbers by pattern")
n = 0 
while n < 3:
    # print (n1_pattern_hot_picks_top3_nums[n],"\t",n2_pattern_hot_picks_top3_nums[n],"\t",n3_pattern_hot_picks_top3_nums[n],"\t",n4_pattern_hot_picks_top3_nums[n])
    print (n1_pattern_hot_picks_top3_nums[n],"\t",n2_pattern_hot_picks_top3_nums[n],"\t",n3_pattern_hot_picks_top3_nums[n])
    data = f"{today_date},{draw_type},{draw_sz},pattern,{n1_pattern_hot_picks_top3_nums[n]},{n2_pattern_hot_picks_top3_nums[n]},{n3_pattern_hot_picks_top3_nums[n]}\n"
    # print(f"dump to file {data}")
    dump_to_file(hotpicks_file_csv, data, 'a')
    n += 1


def generate_random_picks(picks_arr):
    generated_picks = []
    return random.sample(picks_arr,1)

# def generate_combo_picks(n1_top3_arr,n2_top3_arr,n3_top3_arr,n4_top3_arr):
def generate_combo_picks(n1_top3_arr,n2_top3_arr,n3_top3_arr):
    generated_picks = []
          #across_i #1   #2   #3
    # n1_top3_count = ['2', '3', '7']     #n
    # n2_top3_count = ['9', '5', '3']     #j
    # n3_top3_count = ['3', '0', '5']     #k
    # n4_top3_count = ['2', '4', '0']     #m
    across_i = 0    #column
    down_i = 0      #rows

    total_combos = 0    # total combos generated
    for n in n1_top3_arr:
        # print(n, ':')
    
        for j in n2_top3_arr:      # down
            # print('n', n, ', ', ' j', j, ' down_i ')
        
            for k in n3_top3_arr:      # down
                # print('n', n, ', ', ' j', j, ' k',k)

                #   for m in n4_top3_arr:      # down
                #     # print('n', n, ', ', ' j', j, ' k',k, ' m',m)
                #     generated_picks.append([n,j,k,m])
                #     total_combos += 1

                # generated_picks.append([n,j,k,m])
                generated_picks.append([n,j,k])
                total_combos += 1
            
        across_i += 1
        # print('n across', across_i)
    print(total_combos)

    return generated_picks

def lookup_number_exists(num, arr):
    print(f"checking {num} ..")
    is_found = False
    for n in arr:
        # print(f"{n} check in arr")
        if n == num:
            print(f"found {num}")
            is_found = True
            break

    return is_found

# def is_numbers_in_source(n1,n2,n3,n4, source):
#     i = 0
#     for entry in source:
#         if n1 == int(entry['n1']) and  n2 == int(entry['n2']) and  n3 == int(entry['n3']) and n4 == int(entry['n4']):
#             return True
#         i += 1
#     return False

def is_numbers_in_source(n1,n2,n3, source):
    i = 0
    for entry in source:
        if n1 == int(entry['n1']) and  n2 == int(entry['n2']) and  n3 == int(entry['n3']):
            return True
        i += 1
    return False

# def is_number_repeat(combo_pick0,combo_pick1,combo_pick2,combo_pick3):
#     number_repeat_cnt = 0
#     combo_pick = [combo_pick0, combo_pick1, combo_pick2, combo_pick3]

#     if combo_pick[0] == combo_pick[1] or combo_pick[0] == combo_pick[2] or combo_pick[0] == combo_pick[3]:
#         # print (f"number repeat {combo_pick}")
#         # return True
#         number_repeat_cnt += 1

#     if combo_pick[1] == combo_pick[0] or combo_pick[1] == combo_pick[2] or combo_pick[1] == combo_pick[3]:
#         # print (f"number repeat {combo_pick}")
#         # return True
#         number_repeat_cnt += 1

#     if combo_pick[2] == combo_pick[0] or combo_pick[2] == combo_pick[1] or combo_pick[2] == combo_pick[3]:
#         # print (f"number repeat {combo_pick}")
#         # return True
#         number_repeat_cnt += 1

#     if combo_pick[3] == combo_pick[0] or combo_pick[3] == combo_pick[1] or combo_pick[3] == combo_pick[2]:
#         # print (f"number repeat {combo_pick}")
#         # return True
#         number_repeat_cnt += 1


#     if number_repeat_cnt > 2:
#         return True

#     return False

# modified for 3 numbers only
def is_number_repeat(combo_pick0,combo_pick1,combo_pick2):
    number_repeat_cnt = 0
    combo_pick = [combo_pick0, combo_pick1, combo_pick2]

    if combo_pick[0] == combo_pick[1] or combo_pick[0] == combo_pick[2]:
        # print (f"number repeat {combo_pick}")
        # return True
        number_repeat_cnt += 1

    if combo_pick[1] == combo_pick[0] or combo_pick[1] == combo_pick[2]:
        # print (f"number repeat {combo_pick}")
        # return True
        number_repeat_cnt += 1

    if combo_pick[2] == combo_pick[0] or combo_pick[2] == combo_pick[1]:
        # print (f"number repeat {combo_pick}")
        # return True
        number_repeat_cnt += 1

    if number_repeat_cnt > 2:
        return True

    return False

# refnum,date,draw,sampledrawsize,type,refnum,n1,n2,n3,n4,pastwinner

dump_to_file(generated_hotpicks_combo_file_csv, "date,draw,sampledrawsize,type,refnum,n1,n2,n3,n4,pastwinner\n", "w")
generated_methods = ['random', 'combo']
generated_method = generated_methods[1]

print (f'generated_method selected {generated_method}')


if generated_method == 'random':
    n = 0
    max_generate_picks = 500
    print("\t\t*** generate_picks by count")

    print('generating methond random')

    while n < max_generate_picks:

        n1_picked = generate_random_picks(n1_draw_count_top3_nums)
        n2_picked = generate_random_picks(n2_draw_count_top3_nums)
        n3_picked = generate_random_picks(n3_draw_count_top3_nums)
        # n4_picked = generate_random_picks(n4_draw_count_top3_nums)

        # if is_numbers_in_source(n1_picked[0],n2_picked[0],n3_picked[0],n4_picked[0], numbers_dl) == True:
        if is_numbers_in_source(n1_picked[0],n2_picked[0],n3_picked[0], numbers_dl) == True:
            # print(n1_picked[0],"\t",  n2_picked[0],"\t", n3_picked[0],"\t", n4_picked[0],"\t", "exists")
            print(n1_picked[0],"\t",  n2_picked[0],"\t", n3_picked[0],"\t", "exists")
            # data = f"{today_date},{draw_type},{draw_sz},count,{n},{n1_picked[0]},{n2_picked[0]},{n3_picked[0]},{n4_picked[0]},exists\n"
            data = f"{today_date},{draw_type},{draw_sz},count,{n},{n1_picked[0]},{n2_picked[0]},{n3_picked[0]},exists\n"
        else:
            # print(n1_picked[0],"\t",  n2_picked[0],"\t", n3_picked[0],"\t", n4_picked[0],"\t")
            print(n1_picked[0],"\t",  n2_picked[0],"\t", n3_picked[0])
            # data = f"{today_date},{draw_type},{draw_sz},count,{n},{n1_picked[0]},{n2_picked[0]},{n3_picked[0]},{n4_picked[0]},\n"
            data = f"{today_date},{draw_type},{draw_sz},count,{n},{n1_picked[0]},{n2_picked[0]},{n3_picked[0]}\n"

        dump_to_file(generated_hotpicks_combo_file_csv, data, 'a')
        n +=1
    

    print("\t\t*** generate_picks by pattern")
    n = 0
    while n < max_generate_picks:
        # n1_picked = generate_picks(n1_pattern_hot_picks_top3_nums)
        # n2_picked = generate_picks(n2_pattern_hot_picks_top3_nums)
        # n3_picked = generate_picks(n3_pattern_hot_picks_top3_nums)
        # # n4_picked = generate_picks(n4_pattern_hot_picks_top3_nums)
        # if is_numbers_in_source(n1_picked[0],n2_picked[0],n3_picked[0],n4_picked[0], numbers_dl) == True:
        #     print(n1_picked[0],"\t",  n2_picked[0],"\t", n3_picked[0],"\t", n4_picked[0],"\t", "exists")
        #     data = f"{today_date},{draw_type},{draw_sz},pattern,{n},{n1_picked[0]},{n2_picked[0]},{n3_picked[0]},{n4_picked[0]},exists\n"
        # else:
        #     print(n1_picked[0],"\t",  n2_picked[0],"\t", n3_picked[0],"\t", n4_picked[0],"\t")
        #     data = f"{today_date},{draw_type},{draw_sz},pattern,{n},{n1_picked[0]},{n2_picked[0]},{n3_picked[0]},{n4_picked[0]},\n"
    
        # dump_to_file(generated_hotpicks_combo_file_csv, data, 'a')
        n +=1

elif generated_method == 'combo':
        
        print("\t\t*** generate_picks by count")

        print('generating methond combo')
    
        n = 0
        # generated_combo_picks = generate_combo_picks(n1_draw_count_top3_nums,n2_draw_count_top3_nums,n3_draw_count_top3_nums,n4_draw_count_top3_nums)
        generated_combo_picks = generate_combo_picks(n1_draw_count_top3_nums,n2_draw_count_top3_nums,n3_draw_count_top3_nums)
        

        for combo_pick in generated_combo_picks:
            # print ('combo_pick', combo_pick)
            # if is_numbers_in_source(combo_pick[0],combo_pick[1],combo_pick[2],combo_pick[3], numbers_dl) == True:
            #     print(combo_pick[0],"\t",  combo_pick[1],"\t", combo_pick[2],"\t", combo_pick[3],"\t", "exists")
            #     data = f"{today_date},{draw_type},{draw_sz},count,{n},{combo_pick[0]},{combo_pick[1]},{combo_pick[2]},{combo_pick[3]},exists\n"
            # elif is_number_repeat(combo_pick[0],combo_pick[1],combo_pick[2],combo_pick[3]):
            #     print(combo_pick[0],"\t",  combo_pick[1],"\t", combo_pick[2],"\t", combo_pick[3],"\t", "nr")        # digit repeat
            #     data = f"{today_date},{draw_type},{draw_sz},count,{n},{combo_pick[0]},{combo_pick[1]},{combo_pick[2]},{combo_pick[3]},nr\n" #number repeat
            # else:
            #     print(combo_pick[0],"\t",  combo_pick[1],"\t", combo_pick[2],"\t", combo_pick[3],"\t")
            #     data = f"{today_date},{draw_type},{draw_sz},count,{n},{combo_pick[0]},{combo_pick[1]},{combo_pick[2]},{combo_pick[3]},\n"

            if is_numbers_in_source(combo_pick[0],combo_pick[1],combo_pick[2], numbers_dl) == True:
                print(combo_pick[0],"\t",  combo_pick[1],"\t", combo_pick[2],"\t", "exists")
                data = f"{today_date},{draw_type},{draw_sz},count,{n},{combo_pick[0]},{combo_pick[1]},{combo_pick[2]},exists\n"
            elif is_number_repeat(combo_pick[0],combo_pick[1],combo_pick[2]):
                print(combo_pick[0],"\t",  combo_pick[1],"\t", combo_pick[2],"\t", "nr")        # digit repeat
                data = f"{today_date},{draw_type},{draw_sz},count,{n},{combo_pick[0]},{combo_pick[1]},{combo_pick[2]},nr\n" #number repeat
            else:
                print(combo_pick[0],"\t",  combo_pick[1],"\t", combo_pick[2],"\t")
                data = f"{today_date},{draw_type},{draw_sz},count,{n},{combo_pick[0]},{combo_pick[1]},{combo_pick[2]},\n"


            dump_to_file(generated_hotpicks_combo_file_csv, data, 'a')
            n +=1
        print ('total combos#', n)


        print("\t\t*** generate_picks by pattern")

        n = 0
        # generated_combo_picks = generate_combo_picks(n1_pattern_hot_picks_top3_nums,n2_pattern_hot_picks_top3_nums,n3_pattern_hot_picks_top3_nums,n4_pattern_hot_picks_top3_nums)
        generated_combo_picks = generate_combo_picks(n1_pattern_hot_picks_top3_nums,n2_pattern_hot_picks_top3_nums,n3_pattern_hot_picks_top3_nums)
        
        for combo_pick in generated_combo_picks:
            # print ('combo_pick', combo_pick)
            # if is_numbers_in_source(combo_pick[0],combo_pick[1],combo_pick[2], numbers_dl) == True:
            #     print(combo_pick[0],"\t",  combo_pick[1],"\t", combo_pick[2],"\t", "exists")
            #     data = f"{today_date},{draw_type},{draw_sz},pattern,{n},{combo_pick[0]},{combo_pick[1]},{combo_pick[2]},exists\n"
            # elif is_number_repeat(combo_pick[0],combo_pick[1],combo_pick[2]):
            #     print(combo_pick[0],"\t",  combo_pick[1],"\t", combo_pick[2],"\t", "nr")        # digit repeat
            #     data = f"{today_date},{draw_type},{draw_sz},count,{n},{combo_pick[0]},{combo_pick[1]},{combo_pick[2]},nr\n" #number repeat
            # else:
            #     print(combo_pick[0],"\t",  combo_pick[1],"\t", combo_pick[2],"\t", combo_pick[3],"\t")
            #     data = f"{today_date},{draw_type},{draw_sz},pattern,{n},{combo_pick[0]},{combo_pick[1]},{combo_pick[2]},{combo_pick[3]},\n"

            if is_numbers_in_source(combo_pick[0],combo_pick[1],combo_pick[2], numbers_dl) == True:
                print(combo_pick[0],"\t",  combo_pick[1],"\t", combo_pick[2],"\t", "exists")
                data = f"{today_date},{draw_type},{draw_sz},pattern,{n},{combo_pick[0]},{combo_pick[1]},{combo_pick[2]},exists\n"
            elif is_number_repeat(combo_pick[0],combo_pick[1],combo_pick[2]):
                print(combo_pick[0],"\t",  combo_pick[1],"\t", combo_pick[2],"\t", "nr")        # digit repeat
                data = f"{today_date},{draw_type},{draw_sz},count,{n},{combo_pick[0]},{combo_pick[1]},{combo_pick[2]},nr\n" #number repeat
            else:
                print(combo_pick[0],"\t",  combo_pick[1],"\t", combo_pick[2],"\t")
                data = f"{today_date},{draw_type},{draw_sz},pattern,{n},{combo_pick[0]},{combo_pick[1]},{combo_pick[2]},\n"


            dump_to_file(generated_hotpicks_combo_file_csv, data, 'a')
            n +=1
        print ('total combos#', n)

else:
    print('skip generating picks..')

print("done.")