
def Add_many_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
Number_List = [1, 2, 3, 4, 5,6,7,8,9,10]
print(Add_many_numbers(Number_List)) 
if __name__ == "__main__":
   Add_many_numbers(Number_List)
