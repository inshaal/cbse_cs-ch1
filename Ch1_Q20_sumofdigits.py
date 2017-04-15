#To find sum of all digits entered by user.
a=input("Enter a number : ")
k=a
s=0
while k>0:
    c=k%10
    s=s+c
    k=k/10
print "Sum is ",s
