def factorial(n):
    if n==0:
        result=1
    else:
        result=n* factorial(n-1)
    return result
for i in range(1,10):
    print("factorial os",i,"is",factorial(i))