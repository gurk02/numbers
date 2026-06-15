

# 06/14/2026,EVE,30,count,2,9,3,2
# 06/14/2026,EVE,30,count,3,5,0,4
# 06/14/2026,EVE,30,count,7,3,5,0
# 06/14/2026,EVE,30,pattern,2,5,3,2
# 06/14/2026,EVE,30,pattern,3,6,7,0
# 06/14/2026,EVE,30,pattern,9,9,0,4

        #across_i #1   #2   #3
n1_top3_count = ['2', '3', '7']     #n
n2_top3_count = ['9', '5', '3']     #j
n3_top3_count = ['3', '0', '5']     #k
n4_top3_count = ['2', '4', '0']     #m

                # ['3', '0'],
                # ['2', '4'] ]

across_i = 0    #column
down_i = 0      #rows

total_combos = 0    # total combos generated
for n in n1_top3_count:
    # print(n, ':')
    
    for j in n2_top3_count:      # down
        # print('n', n, ', ', ' j', j, ' down_i ')
        
        for k in n3_top3_count:      # down
            # print('n', n, ', ', ' j', j, ' k',k)

            for m in n4_top3_count:      # down
                print('n', n, ', ', ' j', j, ' k',k, ' m',m)
                total_combos += 1
                 
    across_i += 1
    print('n across', across_i)
    
print(total_combos)