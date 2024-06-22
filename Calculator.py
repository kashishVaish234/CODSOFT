# Python program to implement a simple calculator.
while True:
    print("Select the operator which you want to perform ")
    operator=input("(Add,Subtract,Multiplication,Divide): ")
    num1=float(input("Enter the first number:"))
    num2=float(input("Enter the second number:"))

    # Using if-else and elif statement to perform the operation based on the operator entered

    if operator =='Add':
        result=num1+num2
    elif operator =='Subtract':
        result=num1-num2
    elif operator =='Multiplication':
        result=num1*num2
    elif operator =='Divide':
        result=num1/num2
    else:
        print("Invalid operator")

    # Print the result
    print(num1,operator,num2,'=',result)                    

    next_calculation = input("Want to do next calculation? (yes/no): ")
    if next_calculation == "no":
            break
    else:
        print("Invalid Input")
     