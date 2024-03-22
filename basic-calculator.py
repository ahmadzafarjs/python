
new_calc = True
while new_calc:
    first_number = int(input("What is your first number? "))
    print("+\n-\n*\n/")
    calc_operation = input("Pick an operation: ")
    next_number = int(input("What's the next number? "))
    result = calculation(first_number, next_number, calc_operation)
    print(result)


def calculation(first, last, operation):
    if operation == "+":
        return first + last
    elif operation == "-":
        return first - last
    elif operation == "*":
        return first * last
    elif operation == "/":
        return first / last

# continue calcualtions:
decision = input(f"Type 'y' to continue calculation with '{result}' or type 'n' to restart calculator: ")
if decision == "y":
    print("+\n-\n*\n/")
    calc_operation = input("Pick an operation: ")
    next_number = int(input("What's the next number? "))
    print(calculation(result, next_number, calc_operation))
else:
    new_calc = True