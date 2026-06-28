
import csv
import pprint
import numpy as np
# import pandas as pd
import random
from datetime import datetime

numbers_file_csv = 'data/4numbers.csv'

#date,draw,sampledrawsize,type,n1,n2,n3,n4
hotpicks_file_csv = 'data/4numbers_hotpicks.csv'

#date,draw,sampledrawsize,type,refnum,n1,n2,n3,n4,pastwinner
generated_hotpicks_combo_file_csv = 'data/4numbers_generated_hotpicks_combo.csv'

generated_hotpicks_combo_file_anaylsis_csv = 'data/4numbers_generated_hotpicks_combo_anaylsis.csv'


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
# Get Score for generate numbers - n1, n2, n3, n4 against winner number
#
def check_number_against_winner(winner_number_n1,winner_number_n2,winner_number_n3,winner_number_n4, n1,n2,n3,n4):
        score = 0

        # print (f"check winner against number {winner_number_n1} vs {n1}")
        if int(winner_number_n1) == int(n1):
            # print (f"WINNER! {n1} matched")
            score += 1
        elif abs(int(winner_number_n1) - int(n1)) == 1:
            # print (f"CLOSE! {n1} match")
            score += .5
        
        if int(winner_number_n2) == int(n2):
            # print (f"WINNER! {n1} matched")
            score += 1
        elif abs(int(winner_number_n2) - int(n2)) == 1:
            # print (f"CLOSE! {n1} match")
            score += .5
        
        if int(winner_number_n3) == int(n3):
            # print (f"WINNER! {n1} matched")
            score += 1
        elif abs(int(winner_number_n3) - int(n3)) == 1:
            # print (f"CLOSE! {n1} match")
            score += .5
        
        if int(winner_number_n4) == int(n4):
            # print (f"WINNER! {n1} matched")
            score += 1
        elif abs(int(winner_number_n4) - int(n4)) == 1:
            # print (f"CLOSE! {n1} match")
            score += .5
        

        return score

print("start.")

hotpicks_dl = import_csv_data_as_dictlist(generated_hotpicks_combo_file_csv)

#date,draw,sampledrawsize,type,refnum,n1,n2,n3,n4,pastwinner

# winner
# 06/13/2026	EVE	
# 9 6 3 5 6
# 6 6 3 5 , 9 6 3 5 , 9 6 6 5 , 9 6 3 6

winner_number = ['9','6','3','5']
# winner_number = ['7', '9', '2', '1']
winner_number = ['5','9','1','4']
winner_number = ['2','7','4','6'] # 6/15/26 EVE
winner_number = ['6','4','3','4'] # 6/16/26
winner_number = ['2','9','9','0'] # 6/17/26 #FB 8 EVE
winner_number = ['5','3','9','3'] # 6/17/26 #FB 8 EVE
winner_number = ['1','9','2','5'] # 6/17/26 #FB 8 EVE
winner_number = ['0', '2', '3', '1'] # 6/23/26 #FB 8 EVE
winner_number = ['1', '0', '7', '2'] # 6/23/26 #FB 8 EVE
winner_number = ['7', '3', '3', '3'] # 6/26/26 #FB 8 EVE

winner_number_fb = ['4']

winner_number_n1 = winner_number[0]
winner_number_n2 = winner_number[1]
winner_number_n3 = winner_number[2]
winner_number_n4 = winner_number[3]

dump_to_file(generated_hotpicks_combo_file_anaylsis_csv, "date,draw,sampledrawsize,type,refnum,n1,n2,n3,n4,score\n", "w")
dump_to_file(generated_hotpicks_combo_file_anaylsis_csv, f"date,draw,sampledrawsize,type,refnum,{winner_number_n1},{winner_number_n2},{winner_number_n3},{winner_number_n4},4.0\n", "a")

i = 0
for entry in hotpicks_dl:
    #print(f"entry is {entry}")
    date = entry['date']
    draw = entry['draw']  #MID, EVE, ALL
    sampledrawsize = entry['sampledrawsize']
    generated_type = entry['type'] #count vs pattern
    n1 = entry['n1']
    n2 = entry['n2']
    n3 = entry['n3']
    n4 = entry['n4']
    pastwinner = entry['pastwinner']

    # skip past winners. no need to check generated guess number
    if pastwinner == 'exists' or pastwinner == 'nr':
        continue

    # analysis check generated combo against winner see difference
    # print(f"checking number {n1}, {n2}, {n3}, {n4} against winner number{winner_number}")
    score = check_number_against_winner(winner_number_n1,winner_number_n2,winner_number_n3,winner_number_n4, n1,n2,n3,n4)
        # print (f"got a good hot pick number {n1}")
    print (f"score {score} for {n1}, {n2}, {n3}, {n4}")
    # print(date, n1)
    data = f"{date},{draw},{sampledrawsize},{generated_type},{n1},{n2},{n3},{n4},{score}\n" 
    dump_to_file(generated_hotpicks_combo_file_anaylsis_csv, data, 'a')

    i +=1