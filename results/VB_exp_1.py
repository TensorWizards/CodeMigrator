class DataOperation:
    """
    Abstract base class for data operations.
    """
    def perform_operation(self, input_number: int) -> int:
        """
        Abstract method to perform an operation on an integer input.

        Args:
            input_number: The input integer.

        Returns:
            The result of the operation.
        """
        raise NotImplementedError("Subclasses must implement perform_operation method.")

class AdditionOperation(DataOperation):
    """
    Class to perform addition operation.
    """
    def perform_operation(self, input_number: int) -> int:
        """
        Adds 10 to the input integer.

        Args:
            input_number: The input integer.

        Returns:
            The result of the addition operation.
        """
        return input_number + 10

class SubtractionOperation(DataOperation):
    """
    Class to perform subtraction operation.
    """
    def perform_operation(self, input_number: int) -> int:
        """
        Subtracts 5 from the input integer.

        Args:
            input_number: The input integer.

        Returns:
            The result of the subtraction operation.
        """
        return input_number - 5

def update_database(operation_name: str, input_number: int, output_number: int) -> None:
    """
    Simulates updating a database with operation details.

    Args:
        operation_name: The name of the operation performed.
        input_number: The input integer.
        output_number: The output integer.
    """
    print(f"Updating database with: Operation={operation_name}, Input={input_number}, Output={output_number}")

def main():
    """
    Main function of the program.
    """
    print("Welcome to Data Operation Program!")

    try:
        operation_type = input("Enter operation type ('A' for addition, 'S' for subtraction): ").upper()
        input_number = int(input("Enter a number: "))

        if operation_type == 'A':
            operation = AdditionOperation()
        elif operation_type == 'S':
            operation = SubtractionOperation()
        else:
            raise ValueError("Invalid operation type.")

        output_number = operation.perform_operation(input_number)

        print(f"Result: {output_number}")

        update_database(operation_type, input_number, output_number)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()