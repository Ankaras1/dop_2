import random

n = random.randint(3, 20)
print('Первая вставка', n)
m = 0
print('Вторая вставка', end=' ')
stop_flag = False
for i in range(1, n):
    for j in range(1, n):
        if i < j:
            if n % (i + j) == 0:
                m = i, j
                print(m, end=' ')
print(' ')
print('Путь открыт')


