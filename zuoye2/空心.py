i = 0
while i < 5:
    j = 0
    while j < 5:
        if i == 0 or i == 4:
            print("*", end=" ")
        elif j == 0 or j == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
        j += 1
    print()
    i+=1