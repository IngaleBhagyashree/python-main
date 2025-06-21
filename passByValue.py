def modify(x): 
    x=15 
    print ("inside",x,id(x)) 
x=10 
modify(x) 
print( "outside",x,id(x)) 