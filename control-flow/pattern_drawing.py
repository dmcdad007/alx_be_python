# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# While loop for rows
while row < size:
    # For loop for columns
    for col in range(size):
        print("*", end="")  # print stars side by side
    print()  # move to next line after each row
    row += 1
