
# Custom Grep Implementation

## Overview

This project is a custom implementation of the `grep` command-line tool, which is used for searching text using regular expressions (regex). The implementation supports a wide range of regex features, including character classes, anchors, quantifiers, alternation, and backreferences.

## Features

1. **Single Character Matching**
2. **Digit Character Class (`\d`)**
3. **Alphanumeric Character Class (`\w`)**
4. **Positive Character Groups (`[abc]`)**
5. **Negative Character Groups (`[^abc]`)**
6. **Start of String or Line Anchor (`^`)**
7. **End of String or Line Anchor (`$`)**
8. **One or More Quantifier (`+`)**
9. **Zero or One Quantifier (`?`)**
10. **Any Character (`.`)**
11. **Alternation (`|`)**
12. **Backreferences (`\1`, `\2`, etc.)**
13. **Multiple Backreferences**

## Usage

The program reads input from standard input and matches it against a given regex pattern. It exits with code `0` if the pattern is found and `1` if not.

### Example Commands

1. **Single Character Matching**:
   ```sh
   $ echo "apple" | ./your_grep.sh -E "a"
   ```

2. **Digit Character Class**:
   ```sh
   $ echo "apple123" | ./your_grep.sh -E "\d"
   ```

3. **Alphanumeric Character Class**:
   ```sh
   $ echo "alpha-num3ric" | ./your_grep.sh -E "\w"
   ```

4. **Positive Character Group**:
   ```sh
   $ echo "apple" | ./your_grep.sh -E "[abc]"
   ```

5. **Negative Character Group**:
   ```sh
   $ echo "dog" | ./your_grep.sh -E "[^abc]"
   ```

6. **Start of String Anchor (`^`)**:
   ```sh
   $ echo "log" | ./your_grep.sh -E "^log"
   ```

7. **End of String Anchor (`$`)**:
   ```sh
   $ echo "dog" | ./your_grep.sh -E "dog$"
   ```

8. **One or More Quantifier (`+`)**:
   ```sh
   $ echo "caats" | ./your_grep.sh -E "ca+ts"
   ```

9. **Zero or One Quantifier (`?`)**:
   ```sh
   $ echo "dogs" | ./your_grep.sh -E "dogs?"
   ```

10. **Any Character (`.`)**:
    ```sh
    $ echo "dog" | ./your_grep.sh -E "d.g"
    ```

11. **Alternation (`|`)**:
    ```sh
    $ echo "cat" | ./your_grep.sh -E "(cat|dog)"
    ```

12. **Backreferences**:
    ```sh
    $ echo "cat and cat" | ./your_grep.sh -E "(cat) and \1"
    ```

13. **Multiple Backreferences**:
    ```sh
    $ echo "3 red squares and 3 red circles" | ./your_grep.sh -E "(\d+) (\w+) squares and \1 \2 circles"
    ```

## Implementation Explanation

The implementation uses Python's `re` module to handle regular expressions. Here is an explanation of the key components:

1. **Imports**:
   - The `sys` module is used for reading command-line arguments and standard input.
   - The `re` module is used for handling regular expressions.

2. **`match_pattern` Function**:
   - **Arguments**:
     - `input_line`: The string to search within.
     - `pattern`: The regex pattern to search for.
   - **Returns**:
     - `True` if the pattern is found in the input line, `False` otherwise.
   - **Implementation**:
     - The pattern is compiled into a regular expression object using `re.compile`.
     - The `search` method of the regex object is used to search for the pattern in the input line.
     - The function returns `True` if a match is found, and `False` otherwise.

3. **`main` Function**:
   - Reads the pattern from the command-line arguments.
   - Reads the input line from standard input and strips any leading/trailing whitespace.
   - Checks if the first argument is `-E` and exits with an error message if not.
   - Logs a debugging message (visible when running tests).
   - Matches the pattern against the input line and exits with code `0` if the pattern is found, or `1` if not.

4. **Entry Point**:
   - The `main` function is called if the script is executed directly.

## Conclusion

This custom `grep` implementation supports a wide range of regex features, making it a powerful tool for text searching. By leveraging Python's `re` module, the implementation is both robust and efficient, capable of handling complex patterns and providing accurate results.

Feel free to explore and extend the functionality further as needed.



