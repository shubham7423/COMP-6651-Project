import numpy as np

class FloydWarshall:
    def __init__(self, N):
        self.N = N
        # self.A = np.zeros((N, N), dtype = np.int64)

    def floydWarshall(self, A):
        count = 0
        for k in range(self.N):
            for i in range(self.N):
                for j in range(self.N):
                    A[i][j] = min(A[i][k]+A[k][j], A[i][j])
                    count += 1

        print(np.array(A))
        print("Number of Operations Performed: ", count)