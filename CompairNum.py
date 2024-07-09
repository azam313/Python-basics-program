# Python-basics-program
Variables Variables are containers for storing data values.  Creating Variables Python has no command for declaring a variable.  A variable is created the moment you first assign a value to it.Variables do not need to be declared with any particular type, and can even change type after they have been set.


# Function to input two numbers and print their sum
def sum_two_numbers():
    # Input the first number
    num1 = float(input("Enter the first number: "))
    # Input the second number
    num2 = float(input("Enter the second number: "))
    
    # Calculate the sum
    sum = num1 + num2
    
    # Print the result
    print("The sum of the two numbers is:", sum)

# Call the function
sum_two_numbers()


# Function to input the side length of a square and print its area
def calculate_square_area():
    # Input the side length of the square
    side_length = float(input("Enter the side length of the square: "))
    
    # Calculate the area of the square
    area = side_length ** 2
    
    # Print the result
    print("The area of the square is:", area)

# Call the function
calculate_square_area()

# Function to input two floating-point numbers and print their average
def calculate_average():
    # Input the first floating-point number
    num1 = float(input("Enter the first floating-point number: "))
    # Input the second floating-point number
    num2 = float(input("Enter the second floating-point number: "))
    
    # Calculate the average
    average = (num1 + num2) / 2
    
    # Print the result
    print("The average of the two numbers is:", average)

# Call the function
calculate_average()


# Function to input two numbers and compare them
def compare_numbers():
    # Input the first number
    a = float(input("Enter the first number (a): "))
    # Input the second number
    b = float(input("Enter the second number (b): "))
    
    # Compare the numbers and print the result
    if a >= b:
        print("True")
    else:
        print("False")

# Call the function
compare_numbers()
