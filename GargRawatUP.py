import numpy as np

class GargRawatUP:
    def __init__(self, N):
        self.N = N
        self.inc, self.outc, self.selected_k = np.zeros(N, dtype=np.int64), np.zeros(N, dtype=np.int64), np.zeros(N, dtype=np.int64)
        self.inlist, self.outlist = np.zeros((N, N), dtype=np.int64), np.zeros((N, N), dtype=np.int64)
        self.r = np.zeros((N, N), dtype=np.int64)
        
    def improved_FW(self, A):
        # generate self.inlist and self.outlist for each vertex

        for i in range(self.N):
            for j in range(self.N):
                if A[i][j] < float("inf"):
                    self.r[i][j] = j
                else:
                    self.r[i][j] = -1
                if i == j:
                    self.r[i][j] = -1

        for i in range(self.N):
            for j in range(self.N):
                if A[i][j] != 0 and A[i][j] < float("inf"):
                    self.inc[j] += 1
                    self.outc[i] += 1
                    self.inlist[j, self.inc[j]-1] = i
                    self.outlist[i, self.outc[i]-1] = j
        
        cnt = 0
        for k in range(self.N):
            
            for i in range(self.N):
                for j in range(self.N):
                    if i == k or j == k:
                        continue
                    elif A[k][j] + A[i][k] < A[i][j]:
                        A[i][j] = A[k][j] + A[i][k]
                        self.r[i][j] = k 
                    cnt += 1

        
        print(np.array(A))
        print("Number of Operations Performed: ", cnt)

