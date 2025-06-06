from array import * 
a=array('i', [10,20,30,40,50,60,70]) 
print ("length is",len(a) )
print (" 1st position character", a[1] )
print ("Characters from 2 to 4", a[2:5] )
print ("Characters from 2 to end", a[2:] )
print ("Characters from start to 4",a[:5] )
print ("Characters from start to end",a[:] )
a[3]=45 
a[4]=55 
print ("Characters from start to end after modifications ",a[:] )