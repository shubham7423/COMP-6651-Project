import numpy as np

class RectangleAlgorithm:
    def __init__(self, N):
        self.N = N
        self.inc, self.outc, self.selected_k = np.zeros(N, dtype=np.int64), np.zeros(N, dtype=np.int64), np.zeros(N, dtype=np.int64)
        self.inlist, self.outlist = np.zeros((N, N), dtype=np.int64), np.zeros((N, N), dtype=np.int64)
        self.r = np.zeros((N, N), dtype=np.int64)
        
    def improved_FW(self, A):
        
        for i in range(self.N):
            for j in range(self.N):
                if A[i][j] < float("inf"):
                    self.r[i][j] = j
                else:
                    self.r[i][j] = -1
                if i == j:
                    self.r[i][j] = -1
                    
        cnt = 0
        for k in range(self.N):
            
            infs_lst_x = []
            infs_lst_y = []
            for i in range(self.N):
                if A[i][k] == float('inf'):
                    infs_lst_y.append(i)
                if A[k][i] == float('inf'):
                    infs_lst_x.append(i)
            
            if k not in infs_lst_x:
                infs_lst_x.append(k)
            
            if k not in infs_lst_y:
                infs_lst_y.append(k)

            for i in [x for x in range(self.N) if x not in infs_lst_y]:
                for j in [x for x in range(self.N) if x not in infs_lst_x]:
                    if A[i][j] > A[k][j]+A[i][k]:
                        A[i][j] = A[k][j]+A[i][k]
                        self.r[i][j] = k
                    cnt += 1
        
        print(np.array(A))
        print("Number of Operations Performed: ", cnt)