def file_operations(file_path, search_word=None, search_line=None, replace_word=None, start_line=None, end_line=None):
    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            content = file.readlines()

        # Initialize counters for upper and lower case letters
        upper_case_count = 0
        lower_case_count = 0

        # Calculate upper-case and lower-case letter counts
        for line in content:
            for char in line:
                if char.isupper():
                    upper_case_count += 1
                elif char.islower():
                    lower_case_count += 1

        # Output for letter counts
        print(f"Upper-case letters: {upper_case_count}")
        print(f"Lower-case letters: {lower_case_count}")

        # If search_word and search_line are provided, search for the word in a specific line
        if search_word and search_line is not None:
            line = content[search_line - 1]  # -1 to adjust for zero-indexed list
            if search_word in line:
                print(f"Word '{search_word}' found in line {search_line}")
            else:
                print(f"Word '{search_word}' not found in line {search_line}")

        # If search_word, start_line, and end_line are provided, search in a range of lines
        if search_word and start_line is not None and end_line is not None:
            found = False
            for i in range(start_line - 1, end_line):  # Adjust for zero-indexed list
                if search_word in content[i]:
                    print(f"Word '{search_word}' found in line {i + 1}")
                    found = True
            if not found:
                print(f"Word '{search_word}' not found in the range of lines {start_line} to {end_line}")

        # If replace_word is provided, replace it in the file content
        if replace_word:
            with open(file_path, 'w') as file:
                for line in content:
                    file.write(line.replace(search_word, replace_word))
            print(f"Replaced '{search_word}' with '{replace_word}' in the file.")

    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage:
file_path = 'example.txt'  # Specify the path to your file

# 1. Calculate upper and lower case letters
file_operations(file_path)

# 2. Search a word in a particular line (e.g., line 3)
file_operations(file_path, search_word="python", search_line=3)

# 3. Search a word in a range of lines (e.g., lines 2 to 5)
file_operations(file_path, search_word="python", start_line=2, end_line=5)

# 4. Replace a word in the file
file_operations(file_path, search_word="old_word", replace_word="new_word")
