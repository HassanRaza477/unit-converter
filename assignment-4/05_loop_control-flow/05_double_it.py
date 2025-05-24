def main():
    user_number = int(input("Enter a number: "))
    while user_number < 100:
        user_number *= 2
        print(user_number, end=" ")
    print("\nDone!")
if __name__ == "__main__":
    main()