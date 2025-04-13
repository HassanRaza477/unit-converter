

def main():
    fruits = {
        "apple": 2.5,
        "banana": 1.5,
        "orange": 3.0,
        "grape": 4.0,
        "kiwi": 5.0,
        "mango": 6.0,
    }
    total_price = 0

    print("Welcome to the Pop-Up Shop!")
    for fruit, price in fruits.items():
        quantity = int(input(f"How many {fruit}s would you like to buy? "))
        total_price = quantity * price
        print(f"Total price for {quantity} {fruit}(s): ${total_price:.2f}")
if __name__ == "__main__":
    main()