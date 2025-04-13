
def count():
    number_count = {}
    while True:
        user = input("Enter a number: ")
        if user == "":
            break
        number = int(user)
        if number in number_count:
            number_count[number] += 1
        else:
            number_count[number] = 1
    
    for num, count in number_count.items():
        print(f"{num}: {count}")
if __name__ == "__main__":
    count() 
