for i in range(1,6):
    for j in range(1,4):
        if i==1 or i==3 or i==5:
            print("*",end=" ")
        elif i==2 and j==1:
            print("*",end=" ")
        elif i==4 and j==1:
            print("*",end=" ")    
        else:
            print(" ",end=" ")
    print(" ")