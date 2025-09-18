import math

# Get user input for a number
try:
    num = float(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter a numerical value.")
    exit()

# Calculate square root
square_root = math.sqrt(num)

# Calculate natural logarithm (log base e)
try:
    natural_log = math.log(num)
except ValueError:
    natural_log = "Undefined (logarithm of non-positive number)"

# Calculate sine of the number (in radians)
sine_value = math.sin(num)

# Display the calculated results
print(f"\nCalculated Results for {num}:")
print(f"Square Root: {square_root}")
print(f"Natural Logarithm (base e): {natural_log}")
print(f"Sine (in radians): {sine_value}")