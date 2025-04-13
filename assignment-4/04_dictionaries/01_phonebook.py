
def phone_numbers():
    phonebook = {}
    while True:
        name = input("Enter a name : ")
        if name == "":
            break
        phone = input("Enter  aphone number: ")
        phonebook[name] = phone

    for name, phone in phonebook.items():
        print(f"{name}: {phone}")
if __name__ == "__main__":
    phone_numbers()