list = [1000,4000001,455,36,5000,400]
greatest = 0
second_greatest=0

for i in range(len(list)):
    if list[i] > greatest :
        second_greatest = greatest
        greatest = list[i]
    else :
        if list[i]>second_greatest:
            second_greatest = list[i]

print(second_greatest)