
import csv
from datetime import datetime
# 6/17/26 

#
# 5 numbers
# 

numbers_file_csv = 'data/5numbers.csv'
hotpicks_file_csv = 'data/5numbers_hotpicks.csv'
generated_hotpicks_combo_file_csv = 'data/5numbers_generated_hotpicks_combo.csv'

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

# 
# collect data
#

def print_arr(arr, low_num, high_num):
    debug = True

    n = low_num
    n -= 1      # skip the 1st one is -1
    idx = 0 
    while idx < len(arr):
        print (n, ' ', arr[idx])
        idx += 1
        n += 1

numbers = []
numbers_cnt = []
n1_cnt = []
n1     = []
n2_cnt = []
n2     = []
n3_cnt = []
n3     = []
n4_cnt = []
n4     = []
n5_cnt = []
n5     = []

numbers_cnt_top3_cnt = [0, 0, 0]
numbers_cnt_top3_nums = [0, 0, 0]

n1_top3 = [0, 0, 0]
n1_top3_cnt = [0, 0, 0]
n1_top3_nums = [0, 0, 0]

n2_top3 = [0, 0, 0]
n2_top3_cnt = [0, 0, 0]
n2_top3_nums = [0, 0, 0]

n3_top3 = [0, 0, 0]
n3_top3_cnt = [0, 0, 0]
n3_top3_nums = [0, 0, 0]

n4_top3 = [0, 0, 0]
n4_top3_cnt = [0, 0, 0]
n4_top3_nums = [0, 0, 0]

n5_top3 = [0, 0, 0]
n5_top3_cnt = [0, 0, 0]
n5_top3_nums = [0, 0, 0]


debug = False

low_range_numbers = 1
high_range_numbers = 45

n = low_range_numbers
reset = 0
i = 0
numbers_cnt.append(-1)
n1_cnt.append(-1)
n2_cnt.append(-1)
n3_cnt.append(-1)
n4_cnt.append(-1)
n5_cnt.append(-1)
# numbers.append(-1)

while n <= high_range_numbers :
    numbers_cnt.append(reset)
    n1_cnt.append(reset)
    n2_cnt.append(reset)
    n3_cnt.append(reset)
    n4_cnt.append(reset)
    n5_cnt.append(reset)

    # print(n, ' ', numbers_cnt[i])
    i +=1
    n += 1

print('numbers len ', len(numbers_cnt))
print("reset",numbers_cnt)

i =0
for entry in numbers_dl:
    # print (i, ' ', entry)
    n1_num = int(entry['n1'])
    n2_num = int(entry['n2'])
    n3_num = int(entry['n3'])
    n4_num = int(entry['n4'])
    n5_num = int(entry['n5'])
    true_win = entry['true_win']

    # numbers_cnt[n1_num-1] +=1 
    # numbers_cnt[n2_num-1] +=1
    # numbers_cnt[n3_num-1] +=1
    # numbers_cnt[n4_num-1] +=1
    # numbers_cnt[n5_num-1] +=1

    # n1_cnt[n1_num-1] +=1 
    # n2_cnt[n2_num-1] +=1
    # n3_cnt[n3_num-1] +=1
    # n4_cnt[n4_num-1] +=1
    # n5_cnt[n5_num-1] +=1

    
    numbers_cnt[n1_num] +=1 
    numbers_cnt[n2_num] +=1
    numbers_cnt[n3_num] +=1
    numbers_cnt[n4_num] +=1
    numbers_cnt[n5_num] +=1

    n1_cnt[n1_num] +=1 
    n2_cnt[n2_num] +=1
    n3_cnt[n3_num] +=1
    n4_cnt[n4_num] +=1
    n5_cnt[n5_num] +=1


    n1.append(n1_num)       #pattern n1..n5
    n2.append(n2_num)
    n3.append(n3_num)
    n4.append(n4_num)
    n5.append(n5_num)

    numbers.append(n1_num)       #pattern 1 thru all the way to last digit
    numbers.append(n2_num)
    numbers.append(n3_num)
    numbers.append(n4_num)
    numbers.append(n5_num)

    i += 1

# print ('len numbers ', len(numbers))
# print(numbers)
# exit(1)

debug = False
if debug == True:
    print('numbers counted')
    print ('numbers cnt', len(numbers_cnt), numbers_cnt)
    print ('n1 cnt', len(n1_cnt), n1_cnt)
    print ('n2 cnt', len(n2_cnt), n2_cnt)
    print ('n3 cnt', len(n3_cnt), n3_cnt)
    print ('n4 cnt', len(n4_cnt), n4_cnt)
    print ('n5 cnt', (n5_cnt), n5_cnt)
    print('n1',len(n1), n1)
    print('n2',len(n2), n2)
    print('n3',len(n3), n3)
    print('n4',len(n4), n4)
    print('n5',len(n5), n5)
    print(' total count',print_arr(numbers_cnt,low_range_numbers, high_range_numbers))
    print('n1 count', print(print_arr(n1_cnt,low_range_numbers, high_range_numbers)))

#
# get Top3 Numbers & N1-N5
#

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

# print ('Numbers Top3')
# print(find_top3(numbers_cnt,numbers_cnt_top3_cnt,numbers_cnt_top3_nums))

# print('N1 Top3')
# print(find_top3(n1_cnt,n1_top3_cnt,n1_top3_nums))
# print('N2 Top3')
# print(find_top3(n2_cnt,n2_top3_cnt,n2_top3_nums))
# print('N3 Top3')
# print(find_top3(n3_cnt,n3_top3_cnt,n3_top3_nums))
# print('N4 Top3')
# print(find_top3(n4_cnt,n4_top3_cnt,n4_top3_nums))
# print('N5 Top3')
# print(find_top3(n5_cnt,n5_top3_cnt,n5_top3_nums))



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

def hot_pick_10(row_draw_cnt, num, seen_count, diff_last_seen_draw, prev_diff_last_seen_draw, prev_last_seen_loc, last_seen_rate_change):
    hot_pick_dial = 0
    # if seen_count > 1 and diff_last_seen_loc < 6 and (last_seen_rate_change > -5 and last_seen_rate_change < 5):
    #     return True
    # else:
    #     return False     # steps diff from 1st and 2nd last seen  # rate > -15 means compacting   and rate < 5 means compacting still everything else means expanding              
    # if seen_count > 1 and diff_last_seen_draw < 21 and prev_diff_last_seen_draw < 21 and (last_seen_rate_change > -15 and last_seen_rate_change < 10):
    # if seen_count > 1 and (diff_last_seen_draw < 21 and prev_diff_last_seen_draw < 21) and (last_seen_rate_change < 10):
    if seen_count > 1 and ((diff_last_seen_draw <= 25 and prev_diff_last_seen_draw <= 25) or last_seen_rate_change < 6):
        return True
    else:
        return False

def reset_arr_to_value(arr, start, stop, value):
    low_range_numbers = start   # 1
    high_range_numbers = stop   # 45

    n = low_range_numbers
    reset = 0
    i = 0
    while n <= high_range_numbers :
        arr[i] = value

        i +=1
        n += 1
def build_arr(arr, max_len, value):
    # arr = []
    n = 0
    # while n < max_len:
    while n <= max_len:
        arr.append(value)
        n += 1

    return arr

#
# Calculate Hot Pattern Data - last saw, count, diff last saw, rate of change of last saw
#
def calculate_pattern(pattern):
    # print("pattern ", pattern)
    i = 0   # current count draws
    prev_cnt = 0 # previous count draws since last seen
    find_number_count = 0
    # draw_number_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    draw_number_count = [] 
    # build_arr(draw_number_count,45 + 1, 0)
    build_arr(draw_number_count, high_range_numbers, 0)
    prev_draw_number_count = 0
    # last_seen_draw_loc = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    last_seen_draw_loc = []
    # build_arr(last_seen_draw_loc,45 + 1, 0)
    build_arr(last_seen_draw_loc, high_range_numbers, 0)

    # diff_last_seen_draw = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    diff_last_seen_draw = []
    # build_arr(diff_last_seen_draw,45 + 1, 0)
    build_arr(diff_last_seen_draw,high_range_numbers, 0)

    # hot_picks =  [False, False, False, False, False, False, False, False, False, False]
    hot_picks =  []
    # build_arr(hot_picks,45 + 1, False)
    build_arr(hot_picks,high_range_numbers, False)
    # hot_picks_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    hot_picks_count = []
    # build_arr(hot_picks_count,45 + 1, False)
    build_arr(hot_picks_count,high_range_numbers, 0)
    print (' len ', len(hot_picks_count), hot_picks_count)
    debug = False
    i = 0
    total_draws = len(pattern)
    print("calculate_pattern - total draws ", total_draws)
    mean_draw_number_count = 0
    if debug == True:
        print (i, " ", "n", "s_cnt", " steps_diff", " ", "steps_diff_prev", " ", "steps_diff", " ", "HP")
    
    for n in pattern:
        i += 1                  # i is location in pattern
        
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


def calculate_pattern_10(pattern):
    # print("pattern ", pattern)
    i = 0   # current count draws
    prev_cnt = 0 # previous count draws since last seen
    find_number_count = 0
    # draw_number_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    draw_number_count = [] 
    # build_arr(draw_number_count,45 + 1, 0)
    build_arr(draw_number_count, high_range_numbers, 0)
    prev_draw_number_count = 0
    # last_seen_draw_loc = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    last_seen_draw_loc = []
    # build_arr(last_seen_draw_loc,45 + 1, 0)
    build_arr(last_seen_draw_loc, high_range_numbers, 0)

    # diff_last_seen_draw = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    diff_last_seen_draw = []
    # build_arr(diff_last_seen_draw,45 + 1, 0)
    build_arr(diff_last_seen_draw,high_range_numbers, 0)

    # hot_picks =  [False, False, False, False, False, False, False, False, False, False]
    hot_picks =  []
    # build_arr(hot_picks,45 + 1, False)
    build_arr(hot_picks,high_range_numbers, False)
    # hot_picks_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    hot_picks_count = []
    # build_arr(hot_picks_count,45 + 1, False)
    build_arr(hot_picks_count,high_range_numbers, 0)
    print (' len ', len(hot_picks_count), hot_picks_count)
    debug = False
    i = 0
    total_draws = len(pattern)
    print("calculate_pattern - total draws ", total_draws)
    mean_draw_number_count = 0
    if debug == True:
        print (i, " ", "n", "s_cnt", " steps_diff", " ", "steps_diff_prev", " ", "steps_diff", " ", "HP")
    
    for n in pattern:
        i += 1                  # i is location in pattern
        
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
        
        debug = True
        if hot_pick_10(i, n, draw_number_count[n], diff_last_seen_draw[n],  prev_diff_last_seen_draw, prev_last_seen_draw_loc, rate_of_change) == True:
            if debug == True:
                print(i," ",n, draw_number_count[n], " ",diff_last_seen_draw[n], " ",prev_diff_last_seen_draw, " ", rate_of_change, "HP")
            hot_picks[n] = True
            hot_picks_count[n] += 1
        else:
            # hot_picks[n] = False
            if debug == True:
                print(i," ",n, draw_number_count[n], " ",diff_last_seen_draw[n], " ",prev_diff_last_seen_draw, " ", rate_of_change,)

    return hot_picks, draw_number_count, hot_picks_count 


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
    # print (mid_top3_cnt)
    # print (mid_top3_nums)
    # print (eve_top3_cnt)
    # print (eve_top3_nums)

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


def generate_numbers_10(digit, draw_time, sample_arr, sampling_draws):

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
    # sampling_arr = [0, 6, 5, 3, 3, 9, 2, 4, 1, 4, 5, 6, 2, 4, 6,]
    # sampling_arr_trim = sampling_arr[:80] # TEST

    sampling_arr_trim = sampling_arr[:sampling_draws] # TEST

    # hot_picks, draw_number_count, hot_picks_count = calculate_pattern_10(sampling_arr[:sample_draws])
    hot_picks, draw_number_count, hot_picks_count = calculate_pattern_10(sampling_arr_trim)

    print("draw number count ", draw_number_count)
    ## TOP 5
    # draw_count_top3_nums = [0, 0, 0, 0, 0 ]
    # draw_count_top3_cnt = [0, 0, 0, 0, 0 ]
    # pattern_hot_picks_top3_nums = [0, 0, 0, 0, 0]
    # pattern_hot_picks_top3_cnt = [0, 0, 0, 0, 0]
    
    ## TOP 10
    draw_count_top3_nums = [ ]
    build_arr(draw_count_top3_nums, 10, 0)
    draw_count_top3_cnt = []
    build_arr(draw_count_top3_cnt, 10, 0)
    pattern_hot_picks_top3_nums = []
    build_arr(pattern_hot_picks_top3_nums, 10, 0)
    pattern_hot_picks_top3_cnt = []
    build_arr(pattern_hot_picks_top3_cnt, 10, 0)

    print("\n\n")
    print(f"\t\t***calulcate {digit} - {draw_time}")

    print(f"{digit} {draw_time} {sample_draws} Find Top5 Draw Count Hot Picks -> {find_top3(draw_number_count,draw_count_top3_cnt,draw_count_top3_nums)}")

    # cross_ref_cnt_vs_pattern_hop_picks = [-1,-1,-1,-1,-1]
    cross_ref_cnt_vs_pattern_hop_picks = [-1,-1,-1,-1,-1]
    build_arr(cross_ref_cnt_vs_pattern_hop_picks, high_range_numbers, -1)

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
    

    print (f"{digit} TOP5 Draw Count PICKS -> ", draw_count_top3_nums)
    print("Pattern Hot picks Count ->",hot_picks_count)
    print ("TOP5 Pattern Hot Picks Count ->", find_top3(hot_picks_count,pattern_hot_picks_top3_cnt,pattern_hot_picks_top3_nums))

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
    # print (mid_top3_cnt)
    # print (mid_top3_nums)
    # print (eve_top3_cnt)
    # print (eve_top3_nums)

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


#
# Main 
#

# element 3 - get all
sampling_draws =  [14, 21, 30, 60, 90, 120, 150, 365, len(n1)]
draw_sz = sampling_draws[2]  
draw_sz = sampling_draws[6]
draw_sz = sampling_draws[4]     # 1st pick - sample length good
draw_sz = sampling_draws[6] 
draw_sz = sampling_draws[2] 
draw_sz = sampling_draws[6]

# draw_sz = sampling_draws[7] 
draw_sz = sampling_draws[2] 


draw_types = ['DAILY']
draw_type = draw_types[0]

sample_arr_n1 = n1
sample_arr_n2 = n2
sample_arr_n3 = n3
sample_arr_n4 = n4
sample_arr_n5 = n5

# 
# Old method count and pattern (see generate_pattern_10)
#

# n1_picks, n1_draw_count_top3_nums ,n1_pattern_hot_picks_top3_nums = generate_numbers('N1', draw_type,sample_arr_n1,draw_sz)
# print("generate numbers for N1 ...", n1_picks)
# print (n1_draw_count_top3_nums)
# print(n1_pattern_hot_picks_top3_nums)

# n2_picks, n2_draw_count_top3_nums ,n2_pattern_hot_picks_top3_nums = generate_numbers('N2', draw_type,sample_arr_n2,draw_sz)
# print("generate numbers for N2 ...", n2_picks)
# print (n2_draw_count_top3_nums)
# print(n2_pattern_hot_picks_top3_nums)

# n3_picks, n3_draw_count_top3_nums ,n3_pattern_hot_picks_top3_nums = generate_numbers('n3', draw_type,sample_arr_n3,draw_sz)
# print("generate numbers for n3 ...", n3_picks)
# print (n3_draw_count_top3_nums)
# print(n3_pattern_hot_picks_top3_nums)

# n4_picks, n4_draw_count_top3_nums ,n4_pattern_hot_picks_top3_nums = generate_numbers('n4', draw_type,sample_arr_n4,draw_sz)
# print("generate numbers for n4 ...", n4_picks)
# print (n4_draw_count_top3_nums)
# print(n4_pattern_hot_picks_top3_nums)

# n5_picks, n5_draw_count_top3_nums ,n5_pattern_hot_picks_top3_nums = generate_numbers('n5', draw_type,sample_arr_n5,draw_sz)
# print("generate numbers for n5 ...", n5_picks)
# print (n5_draw_count_top3_nums)
# print(n5_pattern_hot_picks_top3_nums)

today_date = datetime.today().strftime("%m/%d/%Y")
print(today_date)

# print ('Generate Numbers of N1-N5')
# print ('N1', "\t", 'N2',"\t",  'N3',"\t",  'N4',"\t",  'N5')
# print("hot numbers by count")

# n = 0 
# while n < 3:
#     print (n1_draw_count_top3_nums[n],"\t",n2_draw_count_top3_nums[n],"\t",n3_draw_count_top3_nums[n],"\t",n4_draw_count_top3_nums[n],"\t", n5_draw_count_top3_nums[n])
#     data = f"{today_date},{draw_type},{draw_sz},count,{n1_draw_count_top3_nums[n]},{n2_draw_count_top3_nums[n]},{n3_draw_count_top3_nums[n]},{n4_draw_count_top3_nums[n]},{n5_draw_count_top3_nums[n]}\n"
#     # print(f"dump to file {data}")
#     dump_to_file(hotpicks_file_csv, data, 'a')
#     n += 1

# print("hot numbers by pattern")
# n = 0 
# while n < 3:
#     print (n1_pattern_hot_picks_top3_nums[n],"\t",n2_pattern_hot_picks_top3_nums[n],"\t",n3_pattern_hot_picks_top3_nums[n],"\t",n4_pattern_hot_picks_top3_nums[n],"\t",n5_pattern_hot_picks_top3_nums[n])
#     data = f"{today_date},{draw_type},{draw_sz},pattern,{n1_pattern_hot_picks_top3_nums[n]},{n2_pattern_hot_picks_top3_nums[n]},{n3_pattern_hot_picks_top3_nums[n]},{n4_pattern_hot_picks_top3_nums[n]},{n5_pattern_hot_picks_top3_nums[n]}\n"
#     # print(f"dump to file {data}")
#     dump_to_file(hotpicks_file_csv, data, 'a')
#     n += 1


draw_sz = sampling_draws[8] 

draw_sz = 30
# [6, 44, 4, 43, 11]
# [6, 44, 4, 43, 37]

# draw_sz = 300      # 60 days
# [6, 4, 21, 40, 44]
# [4, 6, 44, 2, 38]

# draw_sz = 150      # 30 days
# [44, 6, 4, 14, 40]
# [44, 6, 4, 38, 40]

# draw_sz = 100      # 20 days
# [44, 6, 14, 40, 10]
# [44, 6, 40, 41, 20]

# draw_sz = 50      # 10 days
# [41, 44, 6, 14, 1]
# [41, 6, 23, 27, 32]


run = 0
run_number_picks_arr = []
run_numbers_draw_count_top10_nums = []
run_numbers_pattern_hot_picks_top10_nums = []
draws = [30, 50, 100, 150, 300]
for draw in draws:
    draw_sz = draw
    numbers_picks, numbers_draw_count_top10_nums ,numbers_pattern_hot_picks_top10_nums = generate_numbers_10('N1-N5', draw_type,numbers, draw_sz)
    run_number_picks_arr.append(numbers_picks)
    run_numbers_draw_count_top10_nums.append(numbers_draw_count_top10_nums)
    run_numbers_pattern_hot_picks_top10_nums.append(numbers_pattern_hot_picks_top10_nums)
    # print (f"RUN# {run} , draw_sample {draw_sz}")
    # print("generate using seq numbers for N1-N5 ...", numbers_picks)
    # print (numbers_draw_count_top5_nums)
    # print(numbers_pattern_hot_picks_top5_nums)
    # print("")
    run += 1

print("\t\t**RESULTS")

i = 0
while(i < run):
    draw_sz = draws[i]
    print (f"RUN# {i} , draw_sample {draw_sz}")
    print("generate using seq numbers for N1-N5 ...", numbers_picks)
    # print(run_numbers_draw_count_top10_nums[i])
    print(run_numbers_pattern_hot_picks_top10_nums[i])
    print("")
    i += 1

print("done.")