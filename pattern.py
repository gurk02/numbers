
pattern = [ 9, 3,  2,  8,  8,  9,  0,  6,  7,  9,  2,  1, 3,  8,  3,  5,  1, ]

pattern = [ 9, 1,  2,  9,  8,  3,  0,  4,  3, 3,  2,  8,  8, 7,  3, 5, 1, 2, 9, 4, 5]


pick = [ 0, 1, 5, 9 ]

# target = [0, 1, 5, 6, 9]
# target = [0, 1, 5, 9 ]

target = [ 0, 1, 5, 9  ]

target = [  9  ]


target_last_seen = [0, 0]

target_prec = [0, 0]

total_nums = int(len(pattern))

find_prec = 0

vega  = 0 
rho =  0

print(total_nums)
print (pattern)

find_number = 8
found_number = False

mean = 0
mode = 0
median = 0 

i = 0   # current count draws
prev_cnt = 0 # previous count draws since last seen
find_number_count = 0
draw_number_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
last_seen_draw_loc = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
diff_last_seen_draw = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

last_seen_prec = 0
find_prec = 0

# for n in pattern:

#     for find_number in target:

#         if n == find_number:
#             print(f"i {i}, prev_cnt {prev_cnt}")
#             print (f" #{find_number} last seen {i} numbers ago")
#             find_prec = find_number_count / total_nums * 100

#             print(find_number, f" found, last seen {i} draws ago ", find_prec, "%")

#             # if prev_cnt > 0:
#             #     find_prec = ( i - prev_cnt ) / prev_cnt 
#             # else:
#             #     find_prec = i
#             # print(find_number, f" found, last seen {i} draws ago ", find_prec, "% ", prev_cnt, " prev_cnt", last_seen_prec, "last_seen_prec")
#             found_number = True
#             #i = 0 
#             prev_cnt = i
#             find_number_count += 1
#             break;
#         # else:
#         #     print(f"count {i} not found {n} in target {find_number} ")

#     if found_number == True:
#         i = 0
#         print ("reset i to 0")
#         found_number = False
#     i += 1

#     # else:
#     #     print(i)
#     #     i += 1

#         # print(mean)
#         # print(mode)
#         # print(median)

# original
# i = 0
# total_draws = len(pattern)
# print("total draws ", total_draws)
# for n in pattern:
#     i += 1
#     number_count[n] +=1
#     last_seen_count[n] = i
#     print(i," ",n, number_count[n], " ",last_seen_count[n])



    #
    # find hot number
    #
def hot_pick(row_draw_cnt, num, seen_count, diff_last_seen_loc, prev_last_seen_loc, last_seen_rate_change):
    if seen_count > 1 and diff_last_seen_loc < 6 and (last_seen_rate_change > -5 and last_seen_rate_change < 5):
        return True
    else:
        return False


#
# Calculate Pattern Data - last saw, count, diff last saw, rate of change of last saw
#

i = 0
total_draws = len(pattern)
print("total draws ", total_draws)
mean_draw_number_count = 0
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
    
    # rate_of_change = diff_last_seen_draw[n] -  prev_diff_last_seen_draw

    rate_of_change =  prev_diff_last_seen_draw - diff_last_seen_draw[n]

    if hot_pick(i, n, draw_number_count[n], diff_last_seen_draw[n],  prev_last_seen_draw_loc, rate_of_change) == True:
        print(i," ",n, draw_number_count[n], " ",diff_last_seen_draw[n], " ",prev_diff_last_seen_draw, " ", rate_of_change, "HP")
    else:
        print(i," ",n, draw_number_count[n], " ",diff_last_seen_draw[n], " ",prev_diff_last_seen_draw, " ", rate_of_change,)

             # total_draws
             # number_count
             # draws_since_last_seen

    # rate of change of number count
    # number_count_diff = number_count - number_count_prev 
    # rate of change of number count = number_count_diff  / draws_since_last_seen


