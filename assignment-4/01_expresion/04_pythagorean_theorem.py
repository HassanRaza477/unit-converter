import math

# Pythagorean theorem

def pythagorean_theorem():
    ab = float(input("Enter the length of side AB: "))
    ac = float(input("Enter the length of side AC: "))
    bc = math.sqrt(ab**2 + ac**2)
    print(f"The length of side BC is: {bc:.2f}")
    
if __name__ == "__main__":
    pythagorean_theorem()