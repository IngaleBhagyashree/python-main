def add(farg,*args): 
    sum =0 
    for i in args: 
        sum = sum+i 
    print ("sum is",sum+farg) 
add(5,10) 
add(5,10,20) 
add(5,10,20,30)