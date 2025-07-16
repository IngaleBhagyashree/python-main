class myclass:
    """ This is example of doc string."""
    rollno=101
    name= "Nilesh"
    def display(self):
       print(self.rollno, self.name)
s=myclass() #creating object
print(myclass.__doc__) #accessing doc string
s.display() #101 Nile
