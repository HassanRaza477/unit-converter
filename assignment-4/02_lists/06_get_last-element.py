
def get_last_element(lst):
    print('The last element is:', lst[-1])
def main():
    user_list = []
    n = int(input('Enter the number of elements in the list: '))
    if n == 0:
        print("List is empty, no last element to show.")
        return  
    for i in range(n):
        element = input(f'Enter element {i + 1}: ')
        user_list.append(element)
    get_last_element(user_list)
if __name__ == "__main__":
    main()


