#Simple Interactive Python Calculator where users are able to enter Mathematical Expression


number1 = float(input("Enter first number : "))
operation = input ("Enter the mathematical expression you want to perform : ")
number2 = float(input("Enter second number : "))

if operation == "+":
    print (number1+number2)
elif operation == "-":
    print (number1-number2)
elif operation == "*":
    print (number1*number2)
elif operation == "/":
    print (number1/number2)
elif operation == "//":
    print (number1//number2)
elif operation == "%":
    print (number1%number2)
elif operation == "**":
    print (number1**number2)
else:
    print ("invalid expression")
