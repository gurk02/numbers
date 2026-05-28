
# test

numbers = [80, 77, 68, 66, 71, 79, 67, 66, 76, 76]

top3 = [0,0,0]


def find_top3(numbers,top3):
        n = 0 
        print (f"top3 {top3} top3 len {len(top3)}")
        while n < len(numbers):
            number = numbers[n]
            print(f"{n}, checking number{number}")

            top_idx = 0
            while top_idx < len(top3):
                #print(f"top_number {top_number} top3_{top3[top_number]}")
                print(f"compare {number} at idx {top_idx} top_number {top3[top_idx]}")
                if number > top3[top_idx]: #found new top3 number
                    #shift down all top3 numbers
                    print(f"new top number found {number} top_idx {top_idx}")

                    idx = top_idx
                    swap1 = -1
                    swap2 = -1
                    while idx < len(top3):
                        if swap1 == -1:
                            swap1 = top3[idx]
                            top3[idx] = number
                        else:
                            swap2 = top3[idx]
                            top3[idx] = swap1
                            swap1=swap2
                        print(f"idx{idx}, swap1={swap1}, swap2={swap2} top3[idx]={top3[idx]}")
                        idx += 1
                    break

                top_idx +=1

            n += 1
            print(f"top3 {top3}")
        return top3


print("finding top3 from numbers{numbers}")
print(f"results -> {find_top3(numbers,top3)}")

