#A program for converting decimal input into binary. It goes through normal mathematical calculations to find the output
#You should be aware of the method of conversion of decimal to binary to be able to understand this code with accuracy
#This will take decimal as input and give binary output in string form

a=float(input("Enter decimal value"))
e=str(a)
l=e.split(".") #creates a list that contains integer part as 0th index and fraction part as 1st index
#solving for integer part

i=qi=int(l[0])#integer part
ri=''
while qi<>0: 
    r=qi%2
    qi=qi/2 
    ri+=str(r) #adding the remainder to string
ip=ri[::-1] #reversing the string as the output we require will be in reversed form
#now comes the fraction part

if int(l[1])<>0:
    f=int(l[1])#fraction part
    fp='.'
    frac=a%1 #value of decimal part as float
    while frac<>1:
        frac=(frac%1)*2
        x=int(frac)
        fp+=str(x)
else:
    fp=""
#if integer part is zero, a '0' will be instead of empty string
if i==0:
    ip='0'
p=ip+fp
print p
