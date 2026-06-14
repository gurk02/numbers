from datetime import datetime

test_dump = 'test_dump'

print(datetime.today())

date1 = datetime.today().strftime("%m/%d/%Y")
print(date1)
with open(test_dump, 'a') as f:
    f.write(date1 + ",EVE,30,4,count,2,9,3,2,no\n")