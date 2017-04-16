#To check if a number is armstrong number.
x=input("Enter any no. ")
lth=len(str(x)) #length of the number to be taken as power
k=x
sum=0
while k>0:
    j=k%10    #this takes out the last digit.
    sum=sum+(j**lth)
    k=k/10    #this removes the last digit
if sum==x:
    print "It IS an Armstrong number. "
else:
    print "It IS NOT an Armstrong number. "
