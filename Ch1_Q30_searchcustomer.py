#Input and store n customer names and numbers.
d={}
while True:
    a=raw_input("Enter customer's name : ")
    b=raw_input("Enter phone no. : ")
    d[a]=b
    c=raw_input("Do you want to add more customers? 'y' / 'n' ")
    if c=='Y' or c=='y':
        continue
    else:
        break
print "The customer list has been created. It is - "
#Search function begins
while True:
    x=raw_input("Enter customer name to search their phone no. ")
    print "The number of that customer is - ",d[x]
    y=raw_input("Do you want to search for more customer numbers? 'y' / 'n' : ")
    if y=='Y' or y=='y':
        continue
    else:
        break
print "Program stopped. "    
    
