def find_average(num1,num2):
    return (num1 + num2) / 2

def main():
    number1 = int(input("Enter a First number: "))
    number2 = int(input("Enter Second number: ")) 
    average = find_average(number1, number2)
    print("The average of", number1, "and", number2, "is", average)
if __name__ == "__main__":
    main()