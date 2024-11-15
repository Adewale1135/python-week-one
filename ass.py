# Perform the operation based on the user's input
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    else:
        result = "Error: Invalid operation"

    # Print the result
    print(f"The result of {num1} {operation} {num2} = {result}")

# Run the main function
if __name__ == "__main__":
    main()
