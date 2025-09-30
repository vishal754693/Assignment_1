#Perform Basic Mathematical Operations (with user input)

# Step 1: Take two numbers as input from the user
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

# Step 2: Perform basic mathematical operations
addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number

# Handling division safely
if second_number != 0:
    division = first_number / second_number
else:
    division = "Undefined (cannot divide by zero)"

# Step 3: Display the results
print("\nResults of Basic Mathematical Operations:")
print(f"Addition: {first_number} + {second_number} = {addition}")
print(f"Subtraction: {first_number} - {second_number} = {subtraction}")
print(f"Multiplication: {first_number} * {second_number} = {multiplication}")
print(f"Division: {first_number} / {second_number} = {division}")
