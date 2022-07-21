total = 0
'''initialising a number'''
''' range of 0 to 100 then checking if number is even or not, if yes then adding'''
for i in range(101):
    if i % 2 == 0:
        total += i
    else:
        continue
'''if the number is odd it will loop again without adding'''
print(f"Final total of even number from 1 to 100 is: {total}")