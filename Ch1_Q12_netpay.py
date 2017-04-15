#To find net pay with help of basic salary, HRA and Da
a=raw_input("Enter name of employee : ")
b=raw_input("Enter employee number : ")
c=input("Enter basic pay of the employee : ")
if c>100000:
    hra=c*0.15
    da=c*0.08
    netpay=c+hra+da
    print "Salary of",a,"is",netpay,"in which HRA is",hra,"and Da is",da
elif c>50000 and c<=100000:
    hra=c*0.1
    da=c*0.05
    netpay=c+hra+da
    print "Salary of",a,"is",netpay,"in which HRA is",hra,"and Da is",da
elif c<=50000:
    hra=c*0.05
    da=c*0.03
    netpay=c+hra+da
    print "Salary of",a,"is",netpay,"in which HRA is",hra,"and Da is",da
