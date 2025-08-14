print("Welcome to the Calculator!")
print("You can perform 5 operations:")

for i in range(6): 
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '5':
        print("Exiting calculator. Thank you!")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", num1 + num2)
    elif choice == '2':
        print("Result:", num1 - num2)
    elif choice == '3':
        print("Result:", num1 * num2)
    elif choice == '4':
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Cannot divide by zero!")
    else:
        print("Invalid input. Please enter a valid choice.")

       
