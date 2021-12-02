import numpy as np
from queue import PriorityQueue
import time

def bellman_ford(A, src = 0, cnt = 0):
    N = len(A)
    distances = [float('inf')] * N
    distances[src] = 0

    for _ in range(N-1):
        for i in range(N):
            for j in range(N):
                if distances[i] != float("inf") and distances[i] + A[i][j] < distances[j]:
                    distances[j] = distances[i] + A[i][j]
                    cnt += 1
    return distances, cnt

def dijkstra(A, start_vertex, cnt=0):
    visited = []
    N = len(A)
    D = {v:float('inf') for v in range(N)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        visited.append(current_vertex)

        for neighbor in range(N):
            if A[current_vertex][neighbor] < float('inf'):
                distance = A[current_vertex][neighbor]
                if neighbor not in visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
                    cnt += 1
    return D, cnt


if __name__ == "__main__":
    start = time.time()
    N = 5
    A = [
        [0, 6, float("inf"), 5, float("inf")],
        [2, 0, 3, -1, 2],
        [-2, float("inf"), 0, 2, float("inf")],
        [-1, 1, 2, 0, -1],
        [1, float("inf"), float("inf"), float("inf"), 0],
    ]
    # A = [
    #     [0, -5, 2, 3],
    #     [float("inf"), 0, 4, float("inf")],
    #     [float("inf"), float("inf"), 0, 1],
    #     [float("inf"), float("inf"), float("inf"), 0],
    # ]

    A_m =  np.zeros((N+1, N+1))
    A_m[0, :] = 0
    for i in range(1, N+1):
        for j in range(N+1):
            if j == 0:
                A_m[i, j] = float('inf')
            else:
                A_m[i, j] = A[i-1][j-1] 
    bellman_opt = bellman_ford(A_m, 0)
    vertice_weights = bellman_opt[0][1:]
    print("CCCC: ", vertice_weights)
    cnt = bellman_opt[1]
    print(cnt)
    updated_A = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            updated_A[i, j] = A[i][j] + vertice_weights[i] - vertice_weights[j]
    print(updated_A)
    for i in range(N):
        dij_opt = dijkstra(updated_A, i)
        print(list(dij_opt[0].values()))
        cnt += dij_opt[1]
    print(cnt)
    print("Time: ", time.time()-start)
    # print(dijkstra(updated_A, 0))