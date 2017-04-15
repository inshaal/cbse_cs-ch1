#To input n numbers and search in the list
l=[]
c="y"
while c=="y":
    n=input("Enter number to add in the list : ")
    l.append(n)
    c=raw_input("Do you want to add more numbers ? 'y' or 'n' ")
print "list created"
print "list is - ",l
#Search program begins
while True:
    x=input("Enter the no. you want to search in list : ")
    if x in l:
        print "Yes, The list contains",x,"and the index of that is ",l.index(x)
    else:
        print "No. There's no element like this."
    j=raw_input("Do you want to continue searching for numbers? 'y' or 'n'")
    if j=='y':
        continue
    else:
        print "Okay. The program is quitting."
        break
