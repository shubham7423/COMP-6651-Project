import numpy as np
import copy
from FloydWarshall import FloydWarshall
from GargRawatUP import GargRawatUP
from ImprovingFWA import ImprovingFWA
from Johnson import Johnson
from OurAlgorithm import OurAlgorithm
from RectangleAlgorithm import RectangleAlgorithm
import time

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
    JA = copy.deepcopy(A)
    OA = copy.deepcopy(A)

    print("---------------Adjacency Matrix---------------\n", np.array(A))

    print("\n---------------Floyd Warshall---------------")
    start = time.time()
    floydWarshall = FloydWarshall(N)
    floydWarshall.floydWarshall(A)
    print(time.time() - start)

    print("\n---------------Garg Rawat Paper Approach---------------")
    start = time.time()
    gargRawatUP = GargRawatUP(N)
    gargRawatUP.improved_FW(GR)
    print(time.time() - start)

    print("\n---------------Rectangle Method Paper Approach---------------")
    start = time.time()
    rectangleAlgorithm = RectangleAlgorithm(N)
    rectangleAlgorithm.improved_FW(RA)
    print(time.time() - start)

    print("\n---------------Improved FW Paper Approach---------------")
    start = time.time()
    improvingFWA = ImprovingFWA(N)
    improvingFWA.improved_FW(IF)
    print(time.time() - start)

    print("\n---------------Johnson's Algorithm---------------")
    start = time.time()
    johnson = Johnson(N)
    johnson.johnson(JA)
    print(time.time() - start)

    print("\n---------------Our Approach---------------")
    start = time.time()
    ourAlgo = OurAlgorithm(N)
    ourAlgo.improved_FW(OA)
    print(time.time() - start)


