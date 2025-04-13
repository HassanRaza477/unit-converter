
def main():
    num1 = int(input("Please enter an integer to be divided: "))
    num2 = int(input("Please enter an integer to divide by:"))
    remainder = num1 % num2
    quotient = num1 // num2
    print(f"The quotient of {num1} divided by {num2} is {quotient}, and the remainder is {remainder}.")
if __name__ == "__main__":
    main()
