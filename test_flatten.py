
# test

# BROKEN need to fix does not work 7/4

arr1= [17, 25, 5, 18, 21, 28, 0, 0, 0, 0, 0]
arr2= [17, 5, 25, 18, 21, 23, 27, 28, 39, 0, 0]
arr3= [6, 44, 17, 40, 41, 5, 14, 18, 20, 21, 25]
arr4= [17, 44, 6, 40, 4, 10, 14, 21, 41, 1, 5]
arr5= [6, 17, 21, 4, 14, 40, 44, 2, 10, 5, 24]

flatten = []

def flatten_to_arr(arr1, arr2):

    flatten_arr = []
    for item1 in arr1:
         if item1 <1:
             continue
         is_same = False
         for item2 in arr2:
             if item2 < 1:
                 continue

             if (item1 == item2):
                 is_same = True
                 for flat in flatten_arr:
                     if item1 == flat:
                         break
                 # print(f"same keep it {item1} {item2}")
                 # continue
                 is_same = False

         if is_same == False:
            flatten_arr.append(item1)

    # for item in arr:
    #     if (item < 1):
    #         continue
    #     for flat in flatten:
    #         if item == flat:
    #             continue:
            

    return flatten_arr
    
flatten = (flatten_to_arr(arr1,arr2))
print(f"flatten {flatten}")
flatten = (flatten_to_arr(arr1,arr3))
print(f"flatten {flatten}")
# flatten = (flatten_to_arr(flatten,arr4))

print(f"flatten {flatten}")