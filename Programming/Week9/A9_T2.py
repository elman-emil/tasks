import sys

exit_code_input = input("Insert exit code (0–255): ")

try:
    exit_code = int(exit_code_input)
except ValueError:
    print("Error: Exit code must be an integer.")
    sys.exit(1)

if exit_code < 0 or exit_code > 255:
    print("Error: Exit code must be between 0 and 255.")
    sys.exit(1)

print("Exiting program with exit code:", exit_code)
sys.exit(exit_code)
