a=11 
def myfunction(): 
    a=10 
    print ("Inside function",a) # display local variable 
myfunction() 
print ("outside function",a)# display global variable 