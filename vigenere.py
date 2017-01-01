from helpers import alphabet_position, rotate_character

# each letter in the keyword is a codenumber for each letter in the message
def encrypt(message, keyword):
    scrambled_text = ''
    letter_in_keyword = 0 # so I don't have to increment at the same pace as i (i.e. spaces between words)
    for i in range(len(message)): # looks through each letter of the message
        if message[i].isalpha():
            scrambled_text += rotate_character(message[i], alphabet_position(keyword[letter_in_keyword % len(keyword)]))
            letter_in_keyword += 1
        else:
            scrambled_text += message[i]
    return scrambled_text

# everything cool happens here
def main():
    a_message = input("Type a message: ")
    a_keyword = input("Type a keyword: ")
    print(encrypt(a_message, a_keyword))

# this calls the main function above
if __name__ == '__main__':
    main()
