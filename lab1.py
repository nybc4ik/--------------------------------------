from threading import Thread
import time
from random import randrange

x = int(input("Введите размер матриц: ")) # размер матрицы

matrix1 = [[randrange(10) for j in range(x)] for i in range(x)]
matrix2 = [[randrange(10) for j in range(x)] for i in range(x)]

print("исходные матрицы:")
print(matrix1)
print(matrix2)

res = [[0 for j in range(x)] for i in range(x)]
t0 =  time.time() # запуск таймера
for i in range(x):
    for j in range(x):
        for k in range(x):
            res[i][j] += matrix1[i][k] * matrix2[k][j]
t1 =  time.time() - t0 # остановка таймера

print("результат умножения: ", res)
print("Время работы программы: ", t1)

res = [[0 for j in range(x)] for i in range(x)]
def kek(a1,a2,b1,b2):
    global res
    for i in range(a1,a2):
        for j in range(b1,b2):
            for k in range(x):
                res[i][j] += matrix1[i][k] * matrix2[k][j]


threads = []
t2 =  time.time() # запуск таймера
n = x//2
t = Thread(target = kek, args=(0,n,0,n))
threads.append(t)
t.start()

t = Thread(target = kek, args=(n,x,0,n)) 
threads.append(t)
t.start()

t = Thread(target = kek, args=(0,n,n,x)) 
threads.append(t)
t.start()

t = Thread(target = kek, args=(n,x,n,x)) 
threads.append(t)
t.start()

for t in threads:
    t.join()
t3 =  time.time() - t2 # остановка таймера

print("результат умножения: ", res)
print("Время работы программы: ", t3)
print("Разница во времени работы программ: ", t1-t3)
