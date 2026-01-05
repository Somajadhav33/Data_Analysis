n = 10

for i in range(n, 0, -1):
    for j in range(1, i+1):
        if j == 1 or i == n or j==i:
            print("*", end=" ")
        else:
            print("  ", end="")
    print()
        
            