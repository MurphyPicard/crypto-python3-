# I wrote these two functions in another file to stay DRY
from helpers import alphabet_position, rotate_character

# This is so the user can write a number in the command line
from sys import argv, exit

# takes a string and rotates each letter and returns an encrypted string
def encrypt(text, rot):
    scrambled_text = ""
    for letter in text:
        scrambled_text += rotate_character(letter, rot)
    return scrambled_text

# did the user put a number in the command line?
def user_input_is_valid(cl_args):
    if len(cl_args) == 2 and cl_args[1].isdigit(): # exactly 2 arguments needed
        return True
    print("Please enter a number in the command line like 'python3 caesar.py 23'")
    return False
    exit()

def main():
    user_input_is_valid(argv) # did they put a number in the command line?

    a_message = input("Type a message: ")
    # a_number = int(input("Rotate by: "))
    # instead of asking for a number, the user will type a number on the command line

    # argv[1] is the number the user types in the command line
    print(encrypt(a_message, int(argv[1])))

if __name__ == '__main__': # tells python to run the main function
    main()
