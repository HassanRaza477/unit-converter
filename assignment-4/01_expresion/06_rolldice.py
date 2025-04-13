import random

def roll_dice():
    die1: int = random.randint(1, 6)
    die2: int = random.randint(1, 6)
    total = die1 + die2
    print("\nRolling two dice with 6 sides each...\n")
    print(f"First die rolled: {die1}")
    print(f"second die rolled: {die2}")
    print(f"\nThe total of the two dice is: {total}\n")

if __name__ == "__main__":
    roll_dice()
