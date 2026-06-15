num_1 = float(input("Enter the first number: "))
abbrviation = input("Enter operation (+, -, *, /, **): ")
num_2 = float(input("Enter the second number: "))

if abbrviation not in ["+", "-", "*", "/", "**"]:
    print("wrong abbreviation input")
    exit()

if abbrviation == "+":
    result = num_1 + num_2
    print(f"The result of {num_1} + {num_2} is: {result:.3f}")
elif abbrviation == "-":
    result = num_1 - num_2
    print(f"The result of {num_1} - {num_2} is: {result:.3f}")
elif abbrviation == "*":
    result = num_1 * num_2
    print(f"The result of {num_1} * {num_2} is: {result:.3f}")
elif abbrviation == "/":
    if num_2 == 0:
        print("Error: Cannot divide by zero")
    else:
        result = num_1 / num_2
        print(f"The result of {num_1} / {num_2} is: {result:.3f}")
elif abbrviation == "**":
    result = num_1 ** num_2
    print(f"The result of {num_1} ** {num_2} is: {result:.3f}")
