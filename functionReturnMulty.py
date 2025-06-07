#  trying to return multiple values from a function and then unpack them
def calc(a,b): 
    c=a+b 
    d=a-b 
    e=a*b 
    return c,d,e
x,y,z=calc(5,8) 
print ("Addition=",x )
print ("Subtraction=",y)
print("multiplication",z)