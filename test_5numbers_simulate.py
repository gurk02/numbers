
# number = [2, 14, 17, 27 , 38]

def size_arr(arr, low, high):
    i = low
    while i < high + 1:
        arr.append(i)
        i += 1
    return arr

def reset_arr(arr, low, high, valve):
    i = low - 1
    while i < high:
        arr[i] = valve
        i += 1
    return arr

def remove_arr_val(arr, val):
    i = 0
    removed = False
    found_match = False
    new_arr = []
    while i < len(arr):
        if (arr[i] == val):
            print("removing val ", val, " found at idx", i )
            found_match = True
            # remove item from arr
            new_arr = arr[:i]
            new_arr = new_arr + arr[i+1:]
        i += 1
    return new_arr

game_numbers = []
range_low = 1
range_high = 45
#
# Test size_arr, remove_arr_val functions
#
# print(size_arr(game_numbers, 1, 45))
# print("len arr", len(game_numbers))

# remaining_numbers = remove_arr_val(game_numbers, 1)
# print("len arr", len(remaining_numbers))
# print(remaining_numbers)

my_pick = [2, 14, 17, 27 , 38]

size_arr(game_numbers, 1, 45)
reset_arr(game_numbers,1, 45, 5 )

print(game_numbers)
print("my pick ", my_pick)
print("probability experiments")
experiments = 10
target = my_pick[0]
experiment = 0
match_cnt = 0
print("my pick ->", target)
print("rand draw ->",game_numbers[0])
while experiment < experiments:
    rand_draw = game_numbers[0]
    
    print("experiment#",experiment, "# rand_draw", rand_draw, "number ", target, )
    if (rand_draw == target):
        match_cnt += 1
        print("match")
    experiment += 1

prob_score = match_cnt / experiments
print("number", target, "has prob score ", prob_score)
print("done.")