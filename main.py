
import csv
import pprint

numbers_file_csv = 'data/4numbers.csv'

####IMPORT
# read the numbers from the csv file and store them in a list of dictionaries
with open(numbers_file_csv, 'r') as f:
    reader = csv.DictReader(f)      # instaniate a dictreader from obj file f
    numbers_dict_list = list(reader) # convert dictreader obj to a list of dictionaires

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

eve_n1_number_9_dates = [
    #dates
]

eve_n1_numbers = [10]


universe = [
    {
        "draw": "eve",
        "position": 1,
        "number": 9,
        "dates": ["05/21/26","05/08/26"]
    },
    {
        
    }
]

### PROCESS
print("-"*20)
print("processing...")
i = 0
p = 0
# process the numbers and calculate statistics
# process line by line in the csv; each line represent a dict datastruct that is an element of the list
for number in numbers_dict_list:
    i = i + 1

    ## check if number valid
    if int(number['n1']) > 9 or int(number['n1']) < 0:
        continue
    if int(number['n2']) > 9 or int(number['n2']) < 0:
        continue
    if int(number['n3']) > 9 or int(number['n3']) < 0:
        continue
    if int(number['n4']) > 9 or  int(number['n4']) < 0:
        continue

    # calculate tally up number 0-9 for each pos n1-n4
    stats_by_number_pos['n1'][int(number['n1'])] += 1
 
    stats_by_number_pos['n2'][int(number['n2'])] += 1
 
    stats_by_number_pos['n3'][int(number['n3'])] += 1
 
    stats_by_number_pos['n4'][int(number['n4'])] += 1
 
    #print(f"Number1: {number['date']} {number['draw']} {number['n1']},{number['n2']}") #debug
    p = p + 1


#### DISPLAY STATS
print("-"*20)
print(f"Total numbers: {i}")
print(f"Valid numbers: {p}")

print("stats by number position:")
for number in stats_by_number_pos:
    print(f"{number}: {stats_by_number_pos[number]}")


print("###n1")
# todo: make a function TOP3

count_top3 = [{
    "number": 0,
    "count": 0
},{
    "number": 0,
    "count": 0
},{
    "number": 0,
    "count": 0
}]

### n1 TOP3
number = 0
for count in stats_by_number_pos['n1']:
    print(f"{number} -> {count}", '=' * count)

    number = count
    
    top_idx = 0
    while top_idx < len(count_top3):
        #print(f"top_number {top_number} top3_{top3[top_number]}")
        print(f"compare {number} at idx {top_idx} top_number {count_top3[top_idx]['count']}")
        if count > count_top3[top_idx]['count']: #found new top3 number
            #shift down all top3 numbers
            print(f"new top number found {count} top_idx {top_idx}")

            idx = top_idx
            swap1 = -1
            swap2 = -1
            while idx < len(count_top3):
                if swap1 == -1:
                    swap1 = count_top3[idx]['count']
                    count_top3[idx]['count'] = count
                else:
                    swap2 = count_top3[idx]['count']
                    count_top3[idx]['count'] = swap1
                    swap1=swap2
                print(f"idx{idx}, swap1={swap1}, swap2={swap2} top3[idx]={count_top3[top_idx]}")
                idx += 1
            break
        top_idx +=1   
    number +=1
###end for

print("n1_Top3: ")
for top in count_top3:
    print(f"{top['number']} has {top['count']}")

print("###n2")

# todo: make a function TOP3
number = 0
count_top3 = [{
    "number": 0,
    "count": 0
},{
    "number": 0,
    "count": 0
},{
    "number": 0,
    "count": 0
}]

### n2 TOP3
number = 0
for count in stats_by_number_pos['n2']:
    print(f"{number} -> {count}", '=' * count)

    number = count
    
    top_idx = 0
    while top_idx < len(count_top3):
        #print(f"top_number {top_number} top3_{top3[top_number]}")
        print(f"compare {number} at idx {top_idx} top_number {count_top3[top_idx]['count']}")
        if count > count_top3[top_idx]['count']: #found new top3 number
            #shift down all top3 numbers
            print(f"new top number found {count} top_idx {top_idx}")

            idx = top_idx
            swap1 = -1
            swap2 = -1
            while idx < len(count_top3):
                if swap1 == -1:
                    swap1 = count_top3[idx]['count']
                    count_top3[idx]['count'] = count
                else:
                    swap2 = count_top3[idx]['count']
                    count_top3[idx]['count'] = swap1
                    swap1=swap2
                print(f"idx{idx}, swap1={swap1}, swap2={swap2} top3[idx]={count_top3[top_idx]}")
                idx += 1
            break
        top_idx +=1   
    number +=1
###end for



print("n2_Top3: ")
for top in count_top3:
    print(f"{top['number']} has {top['count']}")


### TOP 3 n1-n4

print("done.")

