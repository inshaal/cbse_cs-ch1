#To find sum of 2 distances with feet and inches
print "Enter information for 1st distance "
a=input("Enter feet : ")
b=input("Enter inch : ")
print
print "Enter information for 2nd distance "
x=input("Enter feet : ")
y=input("Enter inch : ")
print
s1=a+x
s2=b+y
#Since 1feet=12inch, convert inches to feet if >12
if s2>12:
    c=s2/12
    s1=s1+c
    s2=s2-(12*c)
print "Sum of their distance is",s1,"feet and",s2,"inches"
