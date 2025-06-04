for i in range(1,9):
    for j in range(1,9):
        if i==j:
            print("$",end=" ")
        elif i==1 or j==1 or i==8 or j==8:
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print(" ")