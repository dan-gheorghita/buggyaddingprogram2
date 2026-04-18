# Prompt the user to enter the first number
print('Enter the first number to add:')
# Store the user's input as a string
first = input()

# Prompt the user to enter the second number
print('Enter the second number to add:')
# Store the user's input as a string
second = input()

# Prompt the user to enter the third number
print('Enter the third number to add:')
# Store the user's input as a string
third = input()

# Attempt to concatenate the three strings together to display the sum
# However, this will result in an incorrect sum because the inputs are added as strings, not numbers
print('The sum is ' + first + second + third)