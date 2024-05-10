# Import the COBOL module
import cobol

# Define the program ID
program_id = "HELLO"

# Define the procedure division
procedure_division = """
DISPLAY "HELLOWORLD".
STOP RUN.
"""

# Create a new COBOL program
program = cobol.Program(program_id, procedure_division)

# Execute the program
program.run()