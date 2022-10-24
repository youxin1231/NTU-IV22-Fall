import math

# Data Input
with open('input.dat') as input:
    n = int(input.readline())
    tau = float(input.readline())
    P = []
    C = []
    T = []
    for i in range(n):
        string = input.readline().split()
        P.append(int(string[0]))
        C.append(float(string[1]))
        T.append(float(string[2]))

# Find B
B = []
for i in range(n):
    max = -1
    for j in range(n):
        if((P[j]>=P[i])and(max<C[j])):
            max = C[j]
    B.append(max)

Q = B.copy()
R = []
for i in range(n):
    while(1):
        # Compute RHS
        sum = 0
        for j in range(n):
            if(P[j]<P[i]):
                sum += math.ceil((Q[i]+tau)/T[j])*C[j]
        RHS = B[i] + sum
        # Check RHS
        if(RHS+C[i]>T[i]):
            R.append(None)
            break
        elif(Q[i]==RHS):
            R.append(round(Q[i]+C[i], 2))
            break
        else:
            Q[i] = RHS

# Print R
for i in range(len(R)):
    if (R[i] == None):
        print("Unschedulable")
    else:
        print(R[i])