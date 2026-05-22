
import csv

numbers_file_csv = 'data/4numbers.csv'

# read the numbers from the csv file and store them in a list of dictionaries
with open(numbers_file_csv, 'r') as f:
    reader = csv.DictReader(f)
    numbers_dict_list = list(reader)

numbers_stats = []
valid_numbers = [0,1,2,3,4,5,6,7,8,9]
number_1_stats = []
number_2_stats = []
number_3_stats = []
number_4_stats = []


stats_by_number_pos = {
        'n1': [0,0,0,0,0,0,0,0,0,0],
        'n2': [0,0,0,0,0,0,0,0,0,0],
        'n3': [0,0,0,0,0,0,0,0,0,0],
        'n4': [0,0,0,0,0,0,0,0,0,0],
}

print("-"*20)
print("processing...")
i = 0
p = 0
# process the numbers and calculate statistics
for number in numbers_dict_list:
    i = i + 1
    if int(number['n1']) > 9 or int(number['n1']) < 0:
        continue
    if int(number['n2']) > 9 or int(number['n2']) < 0:
        continue
    if int(number['n3']) > 9 or int(number['n3']) < 0:
        continue
    if int(number['n4']) > 9 or  int(number['n4']) < 0:
        continue

    stats_by_number_pos['n1'][int(number['n1'])] += 1
 
    stats_by_number_pos['n2'][int(number['n2'])] += 1
 
    stats_by_number_pos['n3'][int(number['n3'])] += 1
 
    stats_by_number_pos['n4'][int(number['n4'])] += 1
 

   
    print(f"Number1: {number['date']} {number['draw']} {number['n1']},{number['n2']}")
    p = p + 1

print("-"*20)
print(f"Total numbers: {i}")
print(f"Valid numbers: {p}")

print("stats by number position:")
for number in stats_by_number_pos:
    print(f"{number}: {stats_by_number_pos[number]}")

print("###n1")
number = 0
for count in stats_by_number_pos['n1']:
    print(f"{number} -> {count}", '=' * count)
    number +=1

print("###n2")
number = 0
for count in stats_by_number_pos['n2']:
    print(f"{number} -> {count}", '=' * count)
    number += 1


print("done.")

