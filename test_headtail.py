


from random import random


sequence = ['h', 't', 'h', 'h', 'h', 'h', 'h', 'h', 'h'] # rate from 100%to 88% win if H picked in this run
sequence = ['h', 't', 'h', 't', 't', 't', 'h']
sequence = ['h', 't', 'h', 't', 'h', 'h', 'h', 't']
sequence = ['h', 't', 'h', 't']
sequence = ['t', 't', 'h', 't']

tail_points = 0
prev_tail_points = 0
head_points = 0
prev_head_points = 0

# guess = ['h', 't', 't', 't']
guess = []


draw_cnt =0
win_rate = 0
match_cnt = 0
guess_idx = 0
hot_pick = 'h'
prev_hot_pick = 'h'

for draw in sequence:
    draw_cnt += 1
  
    if draw == 'h':
        head_points += 1
        tail_points -= 1
    elif draw == 't':
        tail_points += 1
        head_points -= 1
    else:
        tail_points += 0
        head_points -= 0

    # rule1
    prev_hot_pick = hot_pick
    if head_points > tail_points:
        hot_pick = 'h'
    elif tail_points > head_points:
        hot_pick = 't'
    else:
        hot_pick = 'h' # random.choice(['h', 't'])

    #rule2
    print(f'rule1: hot_pick:{hot_pick}')

    guess.append(hot_pick)

    if draw == guess[guess_idx]:
        match_cnt +=1
        is_match = True
    else:
        # match_cnt -=1
        is_match = False


    win_rate = int((match_cnt / draw_cnt) * 100)

    # Reports
    print(f'guess: {hot_pick} prev_guess: {prev_hot_pick}')
    print(f'\t outcome i#{draw_cnt}', draw, guess[guess_idx], win_rate, 'match', is_match)   
    print(f'\t\thead_points: {head_points}, tail_points: {tail_points}')
    
    if guess_idx == len(guess)-1:
        guess_idx = 0
    else:
        guess_idx += 1

    
