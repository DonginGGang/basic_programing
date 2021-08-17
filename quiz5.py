import random

client = 0
for i in range(1, 51):
    a = random.randint(5,51)
    if 5 <= a <= 15:
        print("[O] {0}번째 손님 (소요시간 : {1}분)\n".format(i, a))
        client = client + 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)\n".format(i, a))

print("Total client : {0}".format(client))