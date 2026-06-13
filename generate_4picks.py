
# 4 numbers

# N1-N4
matrix = [
    [0,5,5,2],
    [2,0,0,4],
    [1,5,0,4],
    [8,9,7,8],
    [9,6,5,2],
    [0,5,0,0],
    [8,0,7,4],
    [5,9,0,0],
]


print("matrix ", matrix)

flatten_n1 = []
flatten_nums = []

n1 = []
n2 = []
n3 = []
n4 = []

debug = False

# print ("len ", len(flatten_n1))
# for entry in matrix:
    
#     # print ("*", entry[0])
#     # print ("len flatten_n1", len(flatten_n1))
#     if len(flatten_n1) == 0:

#         # print(" len flatten_n1 is 0 appending", entry[0])
#         flatten_n1.append(entry[0])
#         # print("flatten_n1 append", flatten_n1)
#     else:
#         skip_append = False
#         for n in flatten_n1:
#             # print("checking n ", n, " against entry[0]",entry[0])
#             if entry[0] == n:
#                 skip_append = True
        
#         if skip_append == False:
#             # print(" flatten_n1 is 0 appending", entry[0])
#             flatten_n1.append(entry[0])



def flatten(numbers, flatten_n1):
    print ("len ", len(flatten_n1))
    print("numbers ", numbers)
    for entry in numbers:
    
        # print ("*", entry[0])
        # print ("len flatten_n1", len(flatten_n1))
        if len(flatten_n1) == 0:

            # print(" len flatten_n1 is 0 appending", entry[0])
            flatten_n1.append(entry)
            # print("flatten_n1 append", flatten_n1)
        else:
            skip_append = False
            for n in flatten_n1:
                # print("checking n ", n, " against entry[0]",entry[0])
                if entry == n:
                    skip_append = True
        
            if skip_append == False:
                # print(" flatten_n1 is 0 appending", entry[0])
                flatten_n1.append(entry)
    return flatten_n1

for entry in matrix:
    n1.append(entry[0])
    n2.append(entry[1])
    n3.append(entry[2])
    n4.append(entry[3])


print("n1 ->", flatten(n1, flatten_nums))

flatten_nums = []
print("n2 ->", flatten(n2, flatten_nums))

flatten_nums = []
print("n3 ->", flatten(n3, flatten_nums))

flatten_nums = []
print("n4 ->", flatten(n4, flatten_nums))