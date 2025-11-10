a=int(input("Enter first no."))
b=int(input("Enter second no."))
choice=input("Enter your choice +,-,*,/,%")
if choice == "+":
      print(a+b)
elif choice == "-":
    print(a-b)
elif choice == "*":
    print(a*b)
elif choice == "/":
    print(a/b)
elif choice == "%":
    print(a%b)
else:
    print("Invaild choice")
