#to find all prime no.s upto a given number.
a=input("Enter end no. : ")
print "The prime numbers upto ",a,"are : "
for num in range(1,a+1):
    for i in range(2,num):
        if (num%i)==0:
            break
    else:
        print num,
    
