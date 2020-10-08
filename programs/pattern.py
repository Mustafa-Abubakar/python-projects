row = 8
for r in range(row):
    for col in range(r+1):
        print("*", end="")
    print()


num_steps = 6
for r in range(num_steps):
    for c in range(r):
        print(" ", end='')
    print("#")