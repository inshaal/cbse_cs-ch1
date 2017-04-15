#Reversal of a number entered by an user.
num=input("Enter any number ")
n=num
r=0
while n>0:
    d=n%10
    n=n/10
    r=(r*10)+d
print "Reverse of that no. is :",r
