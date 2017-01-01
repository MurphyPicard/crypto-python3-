# takes a name or names and prints a sentence
def get_initials(fullname):
    initials = []
    for name in fullname.split():
        initials.append(name[0].capitalize())
    answer = "".join(initials)
    # print("The initials of " + fullname + " are", answer)
    return answer

# everything is in here
def main():

    a_name = input("Type a name please: ")

    return get_initials(a_name)

# this calls the main function
if __name__ == '__main__': # tells python to run the main function
    main()
