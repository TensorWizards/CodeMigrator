import sqlite3

class TDataOperation:
    """Abstract base class for data operations."""

    def perform_operation(self, input_number: int) -> int:
        """Abstract method to be implemented by subclasses."""
        raise NotImplementedError("Subclasses must implement perform_operation method")

class TAdditionOperation(TDataOperation):
    """Performs addition operation."""

    def perform_operation(self, input_number: int) -> int:
        """Adds 10 to the input number."""
        return input_number + 10

class TSubtractionOperation(TDataOperation):
    """Performs subtraction operation."""

    def perform_operation(self, input_number: int) -> int:
        """Subtracts 5 from the input number."""
        return input_number - 5

class TDatabaseUpdater:
    """Handles database updates."""

    def update_database(self, operation_name: str, input_number: int, output_number: int):
        """Updates the database with operation details."""
        try:
            # Connect to the database (replace 'your_database.db' with your actual database file)
            conn = sqlite3.connect('your_database.db')
            cursor = conn.cursor()

            # Create the table if it doesn't exist
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS operations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    operation_name TEXT,
                    input_number INTEGER,
                    output_number INTEGER
                )
            ''')

            # Insert the operation details into the table
            cursor.execute('''
                INSERT INTO operations (operation_name, input_number, output_number)
                VALUES (?, ?, ?)
            ''', (operation_name, input_number, output_number))

            # Commit the changes
            conn.commit()

            print("Database updated successfully!")

        except sqlite3.Error as e:
            print(f"An error occurred while updating the database: {e}")

        finally:
            if conn:
                conn.close()

if __name__ == "__main__":
    print("Welcome to DataOperationWithDatabase!")

    try:
        operation_type = input("Enter operation type ('A' for addition, 'S' for subtraction): ").upper()
        input_number = int(input("Enter a number: "))

        if operation_type == 'A':
            operation = TAdditionOperation()
        elif operation_type == 'S':
            operation = TSubtractionOperation()
        else:
            raise ValueError("Invalid operation type")

        output_number = operation.perform_operation(input_number)
        print(f"Result: {output_number}")

        database_updater = TDatabaseUpdater()
        database_updater.update_database(operation_type, input_number, output_number)

    except Exception as e:
        print(f"An error occurred: {type(e).__name__}: {e}")