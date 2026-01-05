n = 10
for i in range(n):
    for k in range(i+1):
        print(" ", end="")
    for j in range(n-i):
        print("* ", end="")
    print()