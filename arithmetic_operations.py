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
        
from arithmetic_operations import perform_operation

def main():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()