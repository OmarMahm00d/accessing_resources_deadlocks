def deadlock_detection(R, A, C, D):
    n = len(C)  # Number of tasks
    m = len(R)  # Number of resource types

    # Initialize Finish array
    Finish = [False] * n

    # List to store the order of task completion
    tau = []

    # Function to search for a task that can proceed
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
            # Task r completes, release its resources
            for j in range(m):
                A[j] += C[r][j]
            Finish[r] = True
            tau.append(r)

    if len(tau) < n:
        deadlocked_tasks = [i for i in range(n) if not Finish[i]]
        print("Deadlock detected. Deadlocked tasks:", deadlocked_tasks)
    else:
        print("No deadlock detected. All tasks can be completed.")

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

deadlock_detection(R, A, C, D)
