#made by GM Harshvardhan
#To input a particular numnber in a particular position in list
lst=input("Enter list : ")
enter=input("Enter the digit to be input : ")
pos=input("Enter position after which it will be added : ")
newlst=lst[:pos] + [enter] + lst[pos:]
print newlst
