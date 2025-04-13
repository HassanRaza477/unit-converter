
max_lenght = 4

def shorten(lst):
    while len(lst) > max_lenght:
        remove = lst.pop()
        print(f"Removing {remove} from list")

def main():
    user_list = []
    n = int(input("Enter the number of elements in the list: "))
    for i in range(n):
        element = input(f"Enter element {i + 1}: ")
        user_list.append(element)
    print(f"Original list: {user_list}")
    shorten(user_list)
    print(f"Shortened list: {user_list}")

if __name__ == "__main__":
    main()

