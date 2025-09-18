def factorial(number):
    if number < 0:
        return "Factorial is not defined for negative numbers."
    elif number == 0:
        return 1
    else:
        return number * factorial(number - 1)

sample_number = 5
result = factorial(sample_number)
print(f"The factorial of {sample_number} is {result}")  