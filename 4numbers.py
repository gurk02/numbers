
import csv
import pprint
import numpy as np
# import pandas as pd


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
n1_mid = np.arange(int(len(numbers_dl)/2))
print("n1_mid len", len(n1_mid))
n1_eve = np.arange(int(len(numbers_dl)/2))
print("n1_mid len", len(n1_eve))

n2 = np.arange(len(numbers_dl))
n2_mid = np.arange(int(len(numbers_dl)/2))
print("n2_mid len", len(n2_mid))
n2_eve = np.arange(int(len(numbers_dl)/2))
print("n2_mid len", len(n2_eve))


n3 = np.arange(len(numbers_dl))
n3_mid = np.arange(int(len(numbers_dl)/2))
print("n3_mid len", len(n3_mid))
n3_eve = np.arange(int(len(numbers_dl)/2))
print("n3_mid len", len(n3_eve))

n4 = np.arange(len(numbers_dl))
n4_mid = np.arange(int(len(numbers_dl)/2))
print("n4_mid len", len(n4_mid))
n4_eve = np.arange(int(len(numbers_dl)/2))
print("n4_mid len", len(n4_eve))


n1_cnt = [0,0,0,0,0,0,0,0,0,0]
n1_mid_cnt = [0,0,0,0,0,0,0,0,0,0]
n1_eve_cnt = [0,0,0,0,0,0,0,0,0,0]

n2_cnt = [0,0,0,0,0,0,0,0,0,0]
n2_mid_cnt = [0,0,0,0,0,0,0,0,0,0]
n2_eve_cnt = [0,0,0,0,0,0,0,0,0,0]

n3_cnt = [0,0,0,0,0,0,0,0,0,0]
n3_mid_cnt = [0,0,0,0,0,0,0,0,0,0]
n3_eve_cnt = [0,0,0,0,0,0,0,0,0,0]

n4_cnt = [0,0,0,0,0,0,0,0,0,0]
n4_mid_cnt = [0,0,0,0,0,0,0,0,0,0]
n4_eve_cnt = [0,0,0,0,0,0,0,0,0,0]

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

        #
    # n4
    #
    i = 0
i_mid = 0
i_eve = 0
for entry in numbers_dl:
    n4[i] = int(entry['n4']) #extract n4 from each line entry
    n4_cnt[n4[i]] += 1
    
    if entry['draw']=='MID':

        n4_mid[i_mid] = int(entry['n4'])
        n4_mid_cnt[n4[i]] += 1
        i_mid += 1

    elif entry['draw']=='EVE':
      
        n4_eve[i_eve] = int(entry['n4'])
        n4_eve_cnt[n4[i]] += 1
        i_eve += 1

    #print(f"i {i}, n4 {n4[i]}")
    i += 1

#
# Reports
#
print("REPORTS")
# print(n1)
print('N1')
print(n1_cnt)
print(n1_mid_cnt)
print(n1_eve_cnt)
print('N2')
print(n2_cnt)
print(n2_mid_cnt)
print(n2_eve_cnt)
print('N3')
print(n3_cnt)
print(n3_mid_cnt)
print(n3_eve_cnt)
print('N4')
print(n4_cnt)
print(n4_mid_cnt)
print(n4_eve_cnt)


print('N1 Freq Distribution')
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
print("finding mid top3 from n1_mid_cnt{n2_mid_cnt}")
print(f"N2 MID results -> {find_top3(n4_mid_cnt,mid_top3_cnt,mid_top3_nums)}")
print (mid_top3_cnt)
print (mid_top3_nums)

tag_mid_top3_nums = ""
for n in n1_mid:
    if n == mid_top3_nums[0]:
         tag_mid_top3_nums += f" {n}*"
    elif n == mid_top3_nums[1]:
         tag_mid_top3_nums += f" {n} "
    elif n == mid_top3_nums[2]:
        tag_mid_top3_nums += f" {n} "
    else:
       tag_mid_top3_nums += f" {n} "

# print("tag mid top3 numbers")
# print(tag_mid_top3_nums)

#
# Regression - eve
#

print("finding eve top3 from n1_eve_cnt{n2_eve_cnt}")
print(f"N2 EVE results -> {find_top3(n4_eve_cnt,eve_top3_cnt,eve_top3_nums)}")
print (eve_top3_cnt)
print (eve_top3_nums)


tag_eve_top3_nums = ""
for n in n1_eve:
    if n == eve_top3_nums[0]:
         tag_eve_top3_nums += f" {n}*"
    elif n == eve_top3_nums[1]:
         tag_eve_top3_nums += f" {n} "
    elif n == eve_top3_nums[2]:
        tag_eve_top3_nums += f" {n} "
    else:
       tag_eve_top3_nums += f" {n} "

# print("tag eve top3 numbers")
# print(tag_eve_top3_nums)

pattern = [ 9, 3,  2,  8,  8,  9,  0,  6,  7,  9,  2,  1, 3,  8,  3,  5,  1]


#
# Find N1 Hot Pattern
#

      #
    # find hot number
    #
def hot_pick(row_draw_cnt, num, seen_count, diff_last_seen_draw, prev_diff_last_seen_draw, prev_last_seen_loc, last_seen_rate_change):
    hot_pick_dial = 0
    # if seen_count > 1 and diff_last_seen_loc < 6 and (last_seen_rate_change > -5 and last_seen_rate_change < 5):
    #     return True
    # else:
    #     return False     # steps diff from 1st and 2nd last seen  # rate > -15 means compacting   and rate < 5 means compacting still everything else means expanding              
    if seen_count > 1 and diff_last_seen_draw < 7 and prev_diff_last_seen_draw < 7 and (last_seen_rate_change > -15 and last_seen_rate_change < 5):
        return True
    else:
        return False

#
# Calculate Hot Pattern Data - last saw, count, diff last saw, rate of change of last saw
#
def calculate_pattern(pattern):
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
    i = 0
    total_draws = len(pattern)
    print("total draws ", total_draws)
    mean_draw_number_count = 0
    if debug == True:
        print (i, " ", "n", "s_cnt", " steps_diff", " ", "steps_diff_prev", " ", "steps_diff", " ", "HP")
    
    for n in pattern:
        i += 1
        
        draw_number_count[n] +=1
    
        #
        # rate of last seen
        #
        prev_last_seen_draw_loc = last_seen_draw_loc[n]
        last_seen_draw_loc[n] = i

        prev_diff_last_seen_draw = diff_last_seen_draw[n]
        diff_last_seen_draw[n] = last_seen_draw_loc[n] - prev_last_seen_draw_loc
    
        # rate_of_change =  prev_diff_last_seen_draw - diff_last_seen_draw[n]

        rate_of_change =  diff_last_seen_draw[n] - prev_diff_last_seen_draw

        if hot_pick(i, n, draw_number_count[n], diff_last_seen_draw[n],  prev_diff_last_seen_draw, prev_last_seen_draw_loc, rate_of_change) == True:
            if debug == True:
                print(i," ",n, draw_number_count[n], " ",diff_last_seen_draw[n], " ",prev_diff_last_seen_draw, " ", rate_of_change, "HP")
            hot_picks[n] = True
            hot_picks_count[n] += 1
        else:
            # hot_picks[n] = False
            if debug == True:
                print(i," ",n, draw_number_count[n], " ",diff_last_seen_draw[n], " ",prev_diff_last_seen_draw, " ", rate_of_change,)

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
print("calulcate N1 - MID hot picks")
# print(n1_mid)

test_pattern = [3, 8, 9, 6, 9, 1, 8, 5, 5, 5, 8, 1, 4, 0, 9, 7, 5, 8, 7, 0, 5, 5, 8, 5, 9, 1, 7, 2, 5, 9, 7, 0, 4, 3, 5, 1, 0
, 6, 2, 3, 6, 8, 0, 3, 5]

# n1_mid = test_pattern
sampling_arr = n4_eve
sampling_draws =  [14, 30, 90, len(sampling_arr)]
sample_draws = sampling_draws[2]
digit = 'n1'
draw_time = 'eve'

print(test_pattern)
hot_picks, draw_number_count, hot_picks_count = calculate_pattern(sampling_arr[:sample_draws])
print(draw_number_count)
draw_count_top3_nums = [0, 0, 0]
draw_count_top3_cnt = [0, 0, 0]
pattern_hot_picks_top3_nums = [0, 0, 0]
pattern_hot_picks_top3_cnt = [0, 0, 0]

print(f"{digit} {draw_time} {sample_draws} Find Top3 Hot Picks -> {find_top3(draw_number_count,draw_count_top3_cnt,draw_count_top3_nums)}")

cross_ref_cnt_vs_pattern_hop_picks = [-1,-1,-1]

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


print ("N1 TOP3 Draw Count PICKS -> ", draw_count_top3_nums)
print("Pattern Hot picks ->",hot_picks_count)
print ("TOP3 Pattern Hot Picks ->", find_top3(hot_picks_count,pattern_hot_picks_top3_cnt,pattern_hot_picks_top3_nums))

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
print (mid_top3_cnt)
print (mid_top3_nums)
print (eve_top3_cnt)
print (eve_top3_nums)

print("---RESULTS---")
print("N1 =>", )
for n in cross_ref_cnt_vs_pattern_hop_picks:
    if n != -1:
        print(n)



# debug = True
# print("calulcate N1 - EVEs hot picks")
# print(n1_eve)
# hot_picks = calculate_pattern(n1_eve)
# i = 0 
# for hot_pick in hot_picks:
#     if debug == True:
#         print(i, " ", hot_pick, " ")
#     if hot_pick == True:
#         print(i)
#     i += 1



# series = pd.Series(n1)
# print(series)

print("done.")