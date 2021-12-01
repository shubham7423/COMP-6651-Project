import numpy as np
import copy

class FloydWarshall:
    def __init__(self, N):
        self.N = N
        # self.A = np.zeros((N, N), dtype = np.int64)

    def floydWarshall(self, A):
        count = 0
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    A[i][j] = min(A[i][k]+A[k][j], A[i][j])
                    count += 1
        print(np.array(A))
        print("Number of Operations Performed: ", count)


class GargRawatUP:
    def __init__(self, N):
        self.N = N
        self.inc, self.outc, self.selected_k = np.zeros(N, dtype=np.int64), np.zeros(N, dtype=np.int64), np.zeros(N, dtype=np.int64)
        self.inlist, self.outlist = np.zeros((N, N), dtype=np.int64), np.zeros((N, N), dtype=np.int64)
        self.r = np.zeros((N, N), dtype=np.int64)
        
    def improved_FW(self, A):
        # generate self.inlist and self.outlist for each vertex

        for i in range(N):
            for j in range(N):
                if A[i][j] < float("inf"):
                    self.r[i][j] = j
                else:
                    self.r[i][j] = -1
                if i == j:
                    self.r[i][j] = -1

        for i in range(N):
            for j in range(N):
                if A[i][j] != 0 and A[i][j] < float("inf"):
                    self.inc[j] += 1
                    self.outc[i] += 1
                    self.inlist[j, self.inc[j]-1] = i
                    self.outlist[i, self.outc[i]-1] = j
        
        cnt = 0
        for k in range(N):
            
            for i in range(N):
                for j in range(N):
                    if i == k or j == k:
                        continue
                    elif A[k][j] + A[i][k] < A[i][j]:
                        A[i][j] = A[k][j] + A[i][k]
                        self.r[i][j] = k 
                    cnt += 1

        
        print(np.array(A))
        print("Predecessor Matrix: ")
        print(self.r)
        print("Number of Operations Performed: ", cnt)


class ImprovingFWA:
    def __init__(self, N):
        self.N = N
        self.inc, self.outc, self.selected_k = np.zeros(N, dtype=np.int64), np.zeros(N, dtype=np.int64), np.zeros(N, dtype=np.int64)
        self.inlist, self.outlist = np.zeros((N, N), dtype=np.int64), np.zeros((N, N), dtype=np.int64)
        self.r = np.zeros((N, N), dtype=np.int64)
        
    def improved_FW(self, A):
        # generate self.inlist and self.outlist for each vertex

        for i in range(N):
            for j in range(N):
                if A[i][j] < float("inf"):
                    self.r[i][j] = j
                else:
                    self.r[i][j] = -1
                if i == j:
                    self.r[i][j] = -1

        for i in range(N):
            for j in range(N):
                if A[i][j] != 0 and A[i][j] < float("inf"):
                    self.inc[j] += 1
                    self.outc[i] += 1
                    self.inlist[j, self.inc[j]-1] = i
                    self.outlist[i, self.outc[i]-1] = j
        
        cnt = 0
        for t in range(N):
            # for choosing best k value (one with minumum in*out)
            mink = -1
            mininxout = 2*N*N
            for k in range(N):
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
        print("Predecessor Matrix: ")
        print(self.r)
        print("Number of Operations Performed: ", cnt)


class RectangleAlgorithm:
    def __init__(self, N):
        self.N = N
        self.inc, self.outc, self.selected_k = np.zeros(N, dtype=np.int64), np.zeros(N, dtype=np.int64), np.zeros(N, dtype=np.int64)
        self.inlist, self.outlist = np.zeros((N, N), dtype=np.int64), np.zeros((N, N), dtype=np.int64)
        self.r = np.zeros((N, N), dtype=np.int64)
        
    def improved_FW(self, A):
        
        for i in range(N):
            for j in range(N):
                if A[i][j] < float("inf"):
                    self.r[i][j] = j
                else:
                    self.r[i][j] = -1
                if i == j:
                    self.r[i][j] = -1
                    
        cnt = 0
        for k in range(N):
            
            infs_lst_x = []
            infs_lst_y = []
            for i in range(N):
                if A[i][k] == float('inf'):
                    infs_lst_y.append(i)
                if A[k][i] == float('inf'):
                    infs_lst_x.append(i)
            
            if k not in infs_lst_x:
                infs_lst_x.append(k)
            
            if k not in infs_lst_y:
                infs_lst_y.append(k)

            for i in [x for x in range(5) if x not in infs_lst_y]:
                for j in [x for x in range(5) if x not in infs_lst_x]:
                    if i != j:
                        if A[i][j] > A[k][j]+A[i][k]:
                            A[i][j] = A[k][j]+A[i][k]
                            self.r[i][j] = k
                        cnt += 1
        
        print(np.array(A))
        print("Predecessor Matrix: ")
        print(self.r)
        print("Number of Operations Performed: ", cnt)




class OurAlgorithm:
    def __init__(self, N):
        self.N = N
        self.inc, self.outc, self.selected_k = np.zeros(N, dtype=np.int64), np.zeros(N, dtype=np.int64), np.zeros(N, dtype=np.int64)
        self.inlist, self.outlist = np.zeros((N, N), dtype=np.int64), np.zeros((N, N), dtype=np.int64)
        self.r = np.zeros((N, N), dtype=np.int64)
        
    def improved_FW(self, A):
        # generate self.inlist and self.outlist for each vertex

        for i in range(N):
            for j in range(N):
                if A[i][j] < float("inf"):
                    self.r[i][j] = j
                else:
                    self.r[i][j] = -1
                if i == j:
                    self.r[i][j] = -1

        for i in range(N):
            for j in range(N):
                if A[i][j] != 0 and A[i][j] < float("inf"):
                    self.inc[j] += 1
                    self.outc[i] += 1
                    self.inlist[j, self.inc[j]-1] = i
                    self.outlist[i, self.outc[i]-1] = j
        
        cnt = 0
        for t in range(N):
            # for choosing best k value (one with minumum in*out)
            mink = -1
            mininxout = 2*N*N
            for k in range(N):
                if self.selected_k[k] == 0 and self.inc[k]*self.outc[k] < mininxout:
                    mink = k
                    mininxout = self.inc[k] * self.outc[k]
            k = mink
            self.selected_k[k] = 1  # vertex is marked selected
            
            infs_lst_x = []
            infs_lst_y = []
            for i in range(N):
                if A[i][k] == float('inf'):
                    infs_lst_y.append(i)
                if A[k][i] == float('inf'):
                    infs_lst_x.append(i)
            
            if k not in infs_lst_x:
                infs_lst_x.append(k)
            
            if k not in infs_lst_y:
                infs_lst_y.append(k)

            for i in [x for x in range(5) if x not in infs_lst_y]:
                for j in [x for x in range(5) if x not in infs_lst_x]:
                    if i != j:
                        if A[i][j] > A[k][j]+A[i][k]:
                            A[i][j] = A[k][j]+A[i][k]
                            self.r[i][j] = k
                        cnt += 1
        
        print(np.array(A))
        print("Predecessor Matrix: ")
        print(self.r)
        print("Number of Operations Performed: ", cnt)


if __name__ == "__main__":
    N = 5
    A = [
        [0, 6, float("inf"), 5, float("inf")],
        [2, 0, 3, -1, 2],
        [-2, float("inf"), 0, 2, float("inf")],
        [-1, 1, 2, 0, -1],
        [1, float("inf"), float("inf"), float("inf"), 0],
    ]
    
    GR = copy.deepcopy(A)
    RA = copy.deepcopy(A)
    IF = copy.deepcopy(A)
    OA = copy.deepcopy(A)

    print("---------------Adjacency Matrix---------------\n", np.array(A))

    print("\n---------------Floyd Warshall---------------")
    floydWarshall = FloydWarshall(N)
    floydWarshall.floydWarshall(A)

    print("\n---------------Garg Rawat Paper Approach---------------")
    gargRawatUP = GargRawatUP(N)
    gargRawatUP.improved_FW(GR)

    print("\n---------------Rectangle Method Paper Approach---------------")
    rectangleAlgorithm = RectangleAlgorithm(N)
    rectangleAlgorithm.improved_FW(RA)

    print("\n---------------Improved FW Paper Approach---------------")
    improvingFWA = ImprovingFWA(N)
    improvingFWA.improved_FW(IF)

    print("\n---------------Our Approach---------------")
    ourAlgo = OurAlgorithm(N)
    ourAlgo.improved_FW(OA)


