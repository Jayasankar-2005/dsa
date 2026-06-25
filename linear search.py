list= []
for i in range(6):
    s = int(input())
    list.append(s)

target = int(input("enter the value"))

def linear(list,target):
    for i in range(len(list)):
        if list[i] == target :
            return i
    return -1

result = linear(list,target)

if result != -1 :
    print(result)
else :
    print("not found")