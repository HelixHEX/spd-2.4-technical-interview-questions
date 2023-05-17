# Given a string of digits 2 to 9 a user has pressed on a T9 “old school” telephone keypad, return a list of all letter combinations they could have been trying to type on the keypad.
# Example execution 1:  t9_letters("23")  ⇒  ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
# Example execution 2:  t9_letters("4663")  ⇒  ["gmmd", …, "gone", …, "good", …, "home", …, "hood", …, "ioof"]

def t9_letters(digits):
    # Initialize the keypad
    keypad = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']}
    # Initialize the result
    result = []
    # Loop through the digits
    for digit in digits:
        # Initialize the letters
        letters = keypad[digit]
        # Initialize the new result
        new_result = []
        # Loop through the letters
        for letter in letters:
            # Check if the result is empty
            if len(result) == 0:
                # Append the letter
                new_result.append(letter)
            # Otherwise
            else:
                # Loop through the result
                for item in result:
                    # Append the letter
                    new_result.append(item + letter)
        # Update the result
        result = new_result
    # Return the result
    return result

print(t9_letters("23"))