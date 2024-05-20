def is_safe_state(R, A, C, D):
    n = len(C)  # Number of tasks
    m = len(R)  # Number of resource types

    Finish = [False] * n
    tau = []

    def search(D, Finish, A):
        for r in range(n):
            if not Finish[r] and all(D[r][j] <= A[j] for j in range(m)):
                return r
        return -1

    while len(tau) < n:
        r = search(D, Finish, A)
        if r == -1:
            break
        else:
            for j in range(m):
                A[j] += C[r][j]
            Finish[r] = True
            tau.append(r)

    return len(tau) == n

def banker_algorithm(R, A, C, D, task_id, resource_request):
    n = len(C)
    m = len(R)

    A_prime = A[:]
    D_prime = [row[:] for row in D]
    C_prime = [row[:] for row in C]

    for j in range(m):
        A_prime[j] -= resource_request[j]
        D_prime[task_id][j] -= resource_request[j]
        C_prime[task_id][j] += resource_request[j]

    if is_safe_state(R, A_prime, C_prime, D_prime):
        for j in range(m):
            A[j] -= resource_request[j]
            D[task_id][j] -= resource_request[j]
            C[task_id][j] += resource_request[j]
        print(f"Request by task {task_id} granted.")
    else:
        print(f"Request by task {task_id} denied.")

# Example usage:
R = [10, 5, 7]  # Total resources in the system
A = [3, 2, 2]   # Available resources in the system
C = [           # Current allocation matrix
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 3],
    [2, 1, 1],
    [0, 0, 2]
]
D = [           # Demand matrix (maximum claim)
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [4, 2, 2],
    [5, 3, 3]
]

task_id = 1
resource_request = [1, 0, 2]

banker_algorithm(R, A, C, D, task_id, resource_request)
