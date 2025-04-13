
def add_three_copies(list,data):
    for i in range(3):
        list.append(data)
def main():
    message = input('Enter a message: ')
    message_list = []
    print('List Before:', message)
    add_three_copies(message_list,message)
    print('List After:', message_list)
if __name__ == "__main__":
    main()

