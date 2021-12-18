import numpy as np
import copy
from FloydWarshall import FloydWarshall
from GargRawatUP import GargRawatUP
from ImprovingFWA import ImprovingFWA
from OurAlgorithm import OurAlgorithm
from RectangleAlgorithm import RectangleAlgorithm
import time
import random

def getRandomGraph(V, num_infs):
    
    while True:
        x = [[random.randint(-8, 20) for _ in range(V)] for _ in range(V)]
        for i in range(N):
            for j in range(N):
                if i == j:
                    x[i][j] = 0
        
        inf_cnt = 0
        while inf_cnt < num_infs:
            i = random.randint(0, V-1)
            j = random.randint(0, V-1)

            if i != j:
                if x[i][j] < float('inf'):
                    x[i][j] = float('inf')
                    inf_cnt += 1
        
        temp = copy.deepcopy(x)
        for k in range(V):
            for i in range(V):
                for j in range(V):
                    temp[i][j] = min(temp[i][k]+x[k][j], temp[i][j])
    
        i = 0 
        j = 0
        cnt = 0
        for i in range(N):
            for j in range(N):
                if i == j and temp[i][j] == 0:
                    cnt += 1

        if cnt == V:
            return x

if __name__ == "__main__":
    N = 8 # Number of edges in graph
    inf = 20 # Number of infinite values in graph
    
    A = getRandomGraph(N, inf)
    
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


