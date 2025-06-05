n=int(input("enter number: "))
f0=1
f1=2
sum=f1
print(f0,"\n",f1)
for i in range(n):
    f2=f0+f1
    print(f2)
    f0=f1
    f1=f2
    if f2%2==0:
        sum=sum+f2
print("sum of even fibonaci series is :",sum)