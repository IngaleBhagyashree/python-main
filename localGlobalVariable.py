a=11 
def myfunction(): 
    b=10 
    print ("Inside function",a) #display global var 
    print ("Inside function",b) #display local var 
myfunction() 
print ("outside function",a) # available print 
# print ("outside function",b) # error