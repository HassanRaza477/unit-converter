
def main():
    values = []  # this is the list

    while True:
        user_input = input("Enter a value: ")  # this is the input string
        if user_input == "":
            break
        values.append(user_input)  # add user_input to list
        print("Current list:", values)

    print("Final list:", values)

if __name__ == "__main__":
    main()
