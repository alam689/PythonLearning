print("Welcome to Basic Calculator Project")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

option = int(input("Select an option for Basic Calculator Operator: "))
if option==1:
    n1=int(input("Enter 1st Number :"))
    n2=int(input("Enter 2nd Number :"))
    n3=n1+n2
    print("Addition is :"+str(n3))
elif option==2:
    n1 = int(input("Enter 1st Number :"))
    n2 = int(input("Enter 2nd Number :"))
    n3 = n1 - n2
    print("Subtraction is :" + str(n3))
elif option==3:
    n1 = int(input("Enter 1st Number :"))
    n2 = int(input("Enter 2nd Number :"))
    n3 = n1 * n2
    print("Multiplication is :" + str(n3))
elif option==4:
    n1 = int(input("Enter 1st Number :"))
    n2 = int(input("Enter 2nd Number :"))
    if n2==0:
        print("Number is not divisible by Zero")
    else:
        n3 = n1 / n2
        print("Division is :" + str(n3))
else:
    print("Invalid option")

