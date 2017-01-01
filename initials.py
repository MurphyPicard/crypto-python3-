def get_initials(fullname):
    initials = []
    for name in fullname.split():
        initials.append(name[0].capitalize())
    answer = "".join(initials)
    print("The initials of " + fullname + " are", answer)

a_name = input("Type a name please: ")

print(get_initials(a_name))
