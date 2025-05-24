Affirmation = "I am capable of doing anything I put my mind to."
print("Welcome to the Wholesome Machine!")

def main():
    print("This machine will give you a wholesome affirmation.")
    while True:
        user_input = input("Type  affirmation: ")
        if user_input == Affirmation:
           print("That's a great affirmation!")
           print("Keep believing in yourself!")
           break
        else:
              print("That's not the right affirmation.")
              print("Try again!")
        continue
if __name__ == "__main__":
    main()
