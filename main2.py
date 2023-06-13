# Задача 24:
# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке,
# причем кусты высажены только по окружности. Таким образом, у каждого куста
# есть ровно два соседних. Всего на грядке растет N кустов. 


import random
k = int(input())
berryes = list(random.randint(0, 10) for i in range(k))
result = []
i = 0
sum = 0

print(berryes)

while (i < k):
    if (i == k - 1):
        sum = berryes[i] + berryes[i - 1] + berryes[0]
    else:
        sum = berryes[i] + berryes[i - 1] + berryes[i + 1]
        result.append(sum)
        result.sort()
    i+=1

print(f"максимальное число ягод за одну итерацию {result[-1]}")