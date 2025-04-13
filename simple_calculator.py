<<<<<<< HEAD
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLICATION")
print("4.DIVIDE")
option=int(input("Enter the operation number to perform an action: "))

if(option in [1,2,3,4]):
    num1= int(input("Enter first number: "))
    num2= int(input("Enter Second number: "))

    if(option==1):
        result=num1+num2
    elif(option==2):
        result=num1-num2
    elif(option==3):
        result=num1*num2
    elif(option==4):
        result=num1/num2
else:
    print("Invalid operation enetered")

print("The result of the operation is {}".format(result))

=======
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLICATION")
print("4.DIVIDE")
option=int(input("Enter the operation number to perform an action: "))

if(option in [1,2,3,4]):
    num1= int(input("Enter first number: "))
    num2= int(input("Enter Second number: "))

    if(option==1):
        result=num1+num2
    elif(option==2):
        result=num1-num2
    elif(option==3):
        result=num1*num2
    elif(option==4):
        result=num1/num2
else:
    print("Invalid operation enetered")

print("The result of the operation is {}".format(result))

>>>>>>> e918ebbfd5dd19b092988c31ccd9400f60cb1272
