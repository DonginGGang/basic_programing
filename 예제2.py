import random

list=[]
for i in range(4):
    a = random.randint(1,28)
    while a in list :
        a = random.randint(1,28)
    list.append(a)
list.sort()

print("아 {0} 시발".format(list))