#Made by Inshaal
#To input a particular numnber in a particular position in list
lst=input("Enter list : ")
enter=input("Enter the digit to be input : ")
pos=input("Enter position after which it will be added : ")
lst.insert(pos, enter) #We can directly use the built-in function
print lst
'''newlst=lst[:pos] + [enter] + lst[pos:] #this was GM's idea.
print newlst''
