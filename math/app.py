def calculations():
    # PROMPT user "Enter the first number:"
    # SET num1 TO user input converted to integer
    # PROMPT user "Enter the second number:"
    # SET num2 TO user input converted to integer
    # PRINT "Enter the operation you want to perform:"
    # PRINT "1. Addition"
    # PRINT "2. Subtraction"
    # PRINT "3. Multiplication"
    # PRINT "4. Division"
    # PROMPT user "Enter the operation:"
    
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    operation = input("Enter the operation you want to perform: \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n")

    # perform addition
    if operation == 1:
        sum = num1 + num2
        if 10 <= sum <= 20:
            print("The sum is between 10 and 20")
        elif sum > 100:
            print("No negative numbers")
        else:
            print("The sum is", sum)
    
    # calculate subtraction
    elif operation == 2:
        sub = num1 - num2
        if sub < 0:
            print("No negative numbers")
        else:
            print("The sub is", sub)

    # calculate multiplication
    elif operation == 4:
        product = num1 * num2
        if product > 50:
            print("The product is greater than 50")
        else:
            print("The product is", product)
    
    # calculate division
    elif operation == 5:
        if num2 != 0:
            quotient = num1 / num2
            if quotient < 1:
                print("The quotient is less than 1")
            else:
                print("The quotient is", quotient)
        else:
            print("Division by zero is mission imposible")
    
calculations()