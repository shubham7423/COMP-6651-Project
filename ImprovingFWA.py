import numpy as np

class ImprovingFWA:
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
        for t in range(self.N):
            # for choosing best k value (one with minumum in*out)
            mink = -1
            mininxout = 2*self.N*self.N
            for k in range(self.N):
                if self.selected_k[k] == 0 and self.inc[k]*self.outc[k] < mininxout:
                    mink = k
                    mininxout = self.inc[k] * self.outc[k]
            k = mink
            self.selected_k[k] = 1  # vertex is marked selected
            
            # explore useful relaxation attempts
            for i in range(self.inc[k]):
                for j in range(self.outc[k]):
                    if (A[self.inlist[k, i]][k] + A[k][self.outlist[k, j]]) < A[self.inlist[k, i]][self.outlist[k, j]]:
                        if A[self.inlist[k, i]][self.outlist[k, j]] == float("inf"):
                            self.outc[self.inlist[k, i]] += 1
                            self.outlist[self.inlist[k, i], self.outc[self.inlist[k, i]]-1] = self.outlist[k, j]
                            self.inc[self.outlist[k, j]] += 1
                            self.inlist[self.outlist[k, j], self.inc[self.outlist[k, j]]-1] = self.inlist[k, i]
                        A[self.inlist[k, i]][self.outlist[k, j]] = A[self.inlist[k, i]][k] + A[k][self.outlist[k, j]]
                        self.r[i, j] = k
                    cnt += 1
        
        print(np.array(A))
        print("Number of Operations Performed: ", cnt)