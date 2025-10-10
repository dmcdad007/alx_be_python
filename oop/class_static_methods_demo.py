# class_static_methods_demo.py

class Calculator:
    """A simple calculator demonstrating class and static methods."""

    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Return the sum of two numbers.
        This method does not depend on class or instance attributes."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Return the product of two numbers.
        This method can access class-level attributes."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
