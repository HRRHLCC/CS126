import sys

def is_palindrome(chars):
    if len(chars) <= 1:
        return True
    if chars[0] != chars[-1]:
        return False
    return is_palindrome(chars[1:-1])


if len(sys.argv) != 2:
    print("input: Lab3c.py <word>")
else:
    input_str = sys.argv[1].lower().replace(" ", "")
    char_list = list(input_str)

    if is_palindrome(char_list):
        print("Palindrome")
    else:
        print("Not Palindrome")