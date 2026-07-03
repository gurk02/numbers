import random



def remove_arr_item(arr, item):
    new_arr = []
    for i in arr:
        if (i == item):
            continue
        new_arr.append(i)
    return new_arr
            
sequence = [ 1, 3, 4, 5]

my_guess = [ 5, 3 ]     # guess
my_guess_idx = 0

available_choices = [ 1, 2, 3, 4, 5  ]

win_score = 0
win_cnt = 0

runs = 2
run = 1 
events = len(sequence)
possible_choices = available_choices
prop_of_succ = 1 / len(possible_choices)

print('\n')
print('start')
print('sequence', sequence)
print('my_guess', my_guess )
print('possible_choices', possible_choices)

print('\n')
print("\t**RUN#", run)

event = 0
for target in sequence:
    event += 1
    
    if (my_guess[my_guess_idx] == target):
        win_cnt += 1
        win_score = win_cnt / events
        print('event#',event, ' target(', target, ') my guess(', my_guess[my_guess_idx], ') outcome Y', 'prop_of_succ 1 /', len(possible_choices), ' is ', prop_of_succ)
    else:
        print('event#',event, ' target(', target, ') my guess(', my_guess[my_guess_idx], ') outcome X', 'prop_of_succ 1 /', len(possible_choices), ' is ', prop_of_succ)
        # missed remove from choices
        possible_choices = remove_arr_item(available_choices, my_guess[my_guess_idx])
    
    prop_of_succ = 1 / len(possible_choices)
    my_guess_idx = 1

print('\n')
print("\t**STATS")
print('win_cnt', win_cnt)
print('win_score', win_score)

print('done.')
