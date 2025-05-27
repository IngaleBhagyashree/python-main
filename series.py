s=0
print("Enter number (or 'e' to exit):")
for h in range(10000):
    i=input()
    if(i=="e"):
        break
    else:
        num=int(i)
        s=s+num
print(s)