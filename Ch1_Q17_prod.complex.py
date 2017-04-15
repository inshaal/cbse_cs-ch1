#To find product of 2 complex no.s
print "Enter complex no. in which 'a' is real part and 'b' is imaginary part"
a=input("Enter a (real part) : ")
b=input("Enter b (imaginary part without 'i') : ")
print "Complex no. 1 is = ",a,"+",b,"i"
print "Enter another imaginary no. in same way. "
x=input("Enter 'a' (real part) for another complex no. : ")
y=input("Enter 'b' (imaginary part without 'i') : ")
print "Complex no. 2 is =",x,"+",y,"i"
p1=(a*x) 
p2=(a*y)+(b*x)
p3=(b*y)
print "product is ",p1,"+",p2,"i"," +",p3,"i^2"
