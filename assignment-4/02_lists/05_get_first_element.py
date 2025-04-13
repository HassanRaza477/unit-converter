
# def Get_First_Element(lst):
#    print('The first element of the list is:', lst[0])

# def get_list():
#     user_list = []
#     n = int(input('Enter the number of elements in the list: '))
#     for i in range(n):
#         user_input = input('Enter the element: ')
#         user_list.append(user_input)
#     return user_list
# def main():
#     user_list = get_list()
#     Get_First_Element(user_list)
# if __name__ == '__main__':
#     main()

def get_first_element(lst):

    print(lst[0])


def get_lst():
    lst = []
    elem: str = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_lst()
    get_first_element(lst)


if __name__ == '__main__':
    main()

