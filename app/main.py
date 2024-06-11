import sys
import re

def match_pattern(input_line, pattern):
    """
    Matches the input line against the given pattern.
    
    Args:
    input_line (str): The input string to search within.
    pattern (str): The regex pattern to search for.
    
    Returns:
    bool: True if the pattern is found in the input line, False otherwise.
    """
    # Compile the pattern into a regular expression object
    regex = re.compile(pattern)
    
    # Search for the pattern in the input line
    match = regex.search(input_line)
    
    # Return True if a match is found, False otherwise
    return match is not None

def main():
    """
    Main function to execute the grep-like search.
    """
    # Read the pattern from the command-line arguments
    pattern = sys.argv[2]
    # Read the input line from standard input and strip any leading/trailing whitespace
    input_line = sys.stdin.read().strip()

    # Check if the first argument is '-E'
    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)

    # Debugging log (visible when running tests)
    print("Logs from your program will appear here!")

    # Match the pattern against the input line and exit with the appropriate code
    if match_pattern(input_line, pattern):
        exit(0)  # Exit with code 0 if the pattern is found
    else:
        exit(1)  # Exit with code 1 if the pattern is not found

if __name__ == "__main__":
    main()