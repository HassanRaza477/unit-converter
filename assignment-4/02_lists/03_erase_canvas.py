import tkinter as tk

# Canvas and grid settings
CELL_SIZE = 40         # Size of each square
GRID_ROWS = 10
GRID_COLS = 10
ERASER_SIZE = 60       # Size of the eraser box

# Create main window and canvas
root = tk.Tk()
root.title("Eraser Simulation")
canvas = tk.Canvas(root, width=GRID_COLS*CELL_SIZE, height=GRID_ROWS*CELL_SIZE, bg="white")
canvas.pack()

# Store each blue square in a list
cells = []

for row in range(GRID_ROWS):
    for col in range(GRID_COLS):
        x1 = col * CELL_SIZE
        y1 = row * CELL_SIZE
        x2 = x1 + CELL_SIZE
        y2 = y1 + CELL_SIZE
        rect = canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="black")
        cells.append((rect, x1, y1, x2, y2))  # Save position for collision checking

# Create eraser (movable white rectangle)
eraser = canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, outline="red", width=2)

# Function to move eraser and erase blue squares
def move_eraser(event):
    x, y = event.x, event.y
    canvas.coords(eraser, x, y, x + ERASER_SIZE, y + ERASER_SIZE)

    # Get eraser current coordinates
    ex1, ey1, ex2, ey2 = canvas.coords(eraser)

    for rect, x1, y1, x2, y2 in cells:
        # Check if eraser overlaps with a blue cell
        if ex1 < x2 and ex2 > x1 and ey1 < y2 and ey2 > y1:
            canvas.itemconfig(rect, fill="white")  # Erase cell

# Bind mouse motion to eraser movement
canvas.bind("<B1-Motion>", move_eraser)  # Move eraser when mouse button 1 is held

root.mainloop()
