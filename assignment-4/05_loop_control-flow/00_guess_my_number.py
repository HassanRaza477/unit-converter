import random

def main():
    secret_number = random.randint(1, 100)

    print("Welcome to the Guess My Number game!")

    print("I have selected a number between 1 and 100.")

    guess = int(input("Take a guess: "))
    while guess != secret_number:
        if guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")
        guess = int(input("Take another guess: "))
        print("The secret number was:", secret_number)
        break
if __name__ == "__main__":
    main()
