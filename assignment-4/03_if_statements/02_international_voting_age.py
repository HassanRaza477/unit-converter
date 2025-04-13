# def voting():
#     age = int(input("Enter your age: "))
#     country = input("Enter your country: ").lower()
#     if country == "Peturksbouipo":
#         if age >= 16:
#             print("You can vote in the Peturksbouipo.")
#         else:
#             print("You cannot vote in the Peturksbouipo.")
#     elif country == "Stanlau":
#         if age >= 25:
#             print("You can vote in the Stanlau.")
#         else:
#             print("You cannot vote in the Stanlau.")
#     elif country == "Mayengua":
#         if age >= 48:
#             print("You can vote in the Mayengua.")
#         else:
#             print("You cannot vote in the Mayengua.")
# if __name__ == "__main__":
#     voting()
        
def main():
    age = int(input("Enter your age: "))

    if age >= 16:
        print("You can vote in Peturksbouipo where the voting age is 16.")
    else:
        print("You cannot vote in Peturksbouipo where the voting age is 16.")

    if age >= 25:
        print("You can vote in Stanlau where the voting age is 25.")
    else:
        print("You cannot vote in Stanlau where the voting age is 25.")

    if age >= 48:
        print("You can vote in Mayengua where the voting age is 48.")
    else:
        print("You cannot vote in Mayengua where the voting age is 48.")

if __name__ == "__main__":
    main()
