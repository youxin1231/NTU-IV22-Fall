from logging import INFO
import math
from random import seed, sample, random
import time
start_time = time.time()
seed(59)

def cost(n, tau, P, C, T):
    # Find B
    B = []
    for i in range(n):
        max = -1
        for j in range(n):
            if ((P[j] >= P[i]) and (max < C[j])):
                max = C[j]
        B.append(max)

    NotSchedulable = False

    Q = B.copy()
    R = []
    for i in range(n):
        while (1):
            # Compute RHS
            sum = 0
            for j in range(n):
                if (P[j] < P[i]):
                    sum += math.ceil((Q[i]+tau)/T[j])*C[j]
            RHS = B[i] + sum
            # Check RHS
            if (RHS+C[i] > T[i]):
                R.append(None)
                NotSchedulable = True
                break
            elif (Q[i] == RHS):
                R.append(round(Q[i]+C[i], 2))
                break
            else:
                Q[i] = RHS

    if NotSchedulable:
        return math.inf
    else:
        return math.fsum(R)


def main():
    # Data Input
    with open('input.dat') as input:
        n = int(input.readline())
        tau = float(input.readline())
        P, C, T = [], [], []

        for i in range(n):
            string = input.readline().split()
            P.append(int(string[0]))
            C.append(float(string[1]))
            T.append(float(string[2]))

    S = P.copy()
    Temp = 1000
    S_star = S.copy()
    r = 0.999

    while (Temp > 1):
        # Pick a random neighbor S' of S
        S_prime = S.copy()
        swap = sample(range(n), 2)
        S_prime[swap[0]], S_prime[swap[1]] = S_prime[swap[1]], S_prime[swap[0]]

        cost_S = cost(n, tau, S, C, T)
        cost_S_prime = cost(n, tau, S_prime, C, T)

        if(cost_S_prime < cost_S):
            S_star = S_prime.copy()
        
        C_delta = cost_S_prime - cost_S
        if C_delta <= 0:
            S = S_prime.copy()
        else:
            if (random() < math.exp(-C_delta/Temp)):
                S = S_prime.copy()

        Temp = r*Temp

    # Print S_star
    for i in range(len(S_star)):
        print(S_star[i])
    print("Objective time:", cost(n, tau, S_star, C, T))
    print(f"Total runtime: {time.time() - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
