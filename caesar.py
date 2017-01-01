from helpers import alphabet_position, rotate_character

# takes a string and rotates each letter and returns an encrypted string
def encrypt(text, rot):
    scrambled_text = ""
    for letter in text:
        scrambled_text += rotate_character(letter, rot)
    return scrambled_text

a_message = input("Type a message: ")
a_number = int(input("Rotate by: "))

print(encrypt(a_message, a_number))
