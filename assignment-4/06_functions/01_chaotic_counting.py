import random

like_hood = 0.3

def done():
     if random.random() < like_hood:
        return True
     else:
        return False


def count():
    for number in range(1, 11):
       if done():
            return 
    print(number, end=' ')

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    count()
    print("\nDone counting!")
if __name__ == "__main__":
    main()  