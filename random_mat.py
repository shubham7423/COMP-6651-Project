import numpy as np
import random

N = 3
x = [[random.randint(-10, 10) for _ in range(N)] for _ in range(N)]

inf_cnt = 0

while inf_cnt < 4:
    i = random.randint(0, N-1)
    j = random.randint(0, N-1)

    if x[i][j] < float('inf'):
        x[i][j] = float('inf')
        inf_cnt += 1

print(np.array(x))