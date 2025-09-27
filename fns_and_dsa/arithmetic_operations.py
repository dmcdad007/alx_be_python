def perform_operation(num1: float, num2: float, operation: str):
    """
    Performs arithmetic operation based on the given parameters.
    
    Parameters:
        num1 (float): First number
        num2 (float): Second number
        operation (str): 'add', 'subtract', 'multiply', or 'divide'
    
    Returns:
        float | str: The result of the operation, or an error message
    """

    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 == 0:
                return "Error: Division by zero"
            return num1 / num2
        case _:
            return "Error: Invalid operation"
# Import function
from calculator import perform_operation  # if saved in calculator.py

# Example calls
print(perform_operation(10, 5, "add"))       # 15
print(perform_operation(10, 5, "subtract"))  # 5
print(perform_operation(10, 5, "multiply"))  # 50
print(perform_operation(10, 0, "divide"))    # Error: Division by zero
print(perform_operation(10, 5, "mod"))       # Error: Invalid operation
