# pass a list to a function and modify it
def modify(a): 
    a.append(5) 
    print ("inside",a,id(a))
a=[1,2,3,4] 
modify(a) 
print ("outside",a,id(a))