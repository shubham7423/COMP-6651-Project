import numpy as np
import copy
from FloydWarshall import FloydWarshall
from GargRawatUP import GargRawatUP
from ImprovingFWA import ImprovingFWA
from OurAlgorithm import OurAlgorithm
from RectangleAlgorithm import RectangleAlgorithm

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


