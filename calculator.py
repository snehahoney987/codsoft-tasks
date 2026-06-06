a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
print("Select Operation:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Modulo")
choice=int(input("Enter your choice:"))
if choice==1:
    print("sum of a and b is:",a+b)
elif choice==2:
    print("minus of a and b is:",a-b)
elif choice==3:
    print("multiply of a and b is:",a*b)
elif choice==4:
    if b!=0:
         print("division of a and b is:",a/b)
    else:
        print("Error! divide by zero is not allowed")
elif choice==5:
        print("modulo of a and b is:",a%b)
else:
    print("Invalid choice")