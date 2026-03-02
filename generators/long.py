import random

n = random.randint(1, 100000)
print(n)
for i in range(n):
    x = random.randint(1, 99)
    y = random.randint(1, 99)
    ops = random.choice(['+', '-'])
    print(x, ops, y)