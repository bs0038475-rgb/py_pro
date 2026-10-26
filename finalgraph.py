import random
import tkinter as tk

# --- 1. Your Math Class ---
class DynamicExponentialList:
    def __init__(self, length_growth_rate, initial_length=10):
        self.length_growth_rate = length_growth_rate
        self.current_length = 0
        self.values = []
        self.expand(amount=initial_length)

    def expand(self, amount=None):
        if amount is None: amount = self.length_growth_rate
        start_index = self.current_length
        self.current_length += amount
        for i in range(start_index, self.current_length):
            self.values.append(2**(i + 1))

    def generate_coordinates(self):
        x_coords = self.values
        y_coords = self.values.copy()
        random.shuffle(y_coords)
        return list(zip(x_coords, y_coords))

# Generate a 6-item sequence for the graph
my_list = DynamicExponentialList(length_growth_rate=2, initial_length=6)
coords = my_list.generate_coordinates()

# --- 2. The Tkinter Graphing Code ---
# Create the pop-up window
root = tk.Tk()
root.title("Tkinter Math Graph")

# Create a white canvas (800x500 pixels)
canvas_w = 800
canvas_h = 500
canvas = tk.Canvas(root, width=canvas_w, height=canvas_h, bg="white")
canvas.pack(padx=20, pady=20)

# Find the largest X and Y values so we can scale the dots to fit the window
max_x = max([point[0] for point in coords])
max_y = max([point[1] for point in coords])

# Loop through our (X, Y) pairs and draw them
dot_radius = 6

for x, y in coords:
    # Scale math coordinates to fit inside the 800x500 pixel window (with 40px padding)
    pixel_x = (x / max_x) * (canvas_w - 80) + 40
    
    # Tkinter's Y-axis starts at the TOP of the screen (0) and goes down.
    # We subtract from canvas_h to flip it so the graph is right-side up.
    pixel_y = canvas_h - ((y / max_y) * (canvas_h - 80) + 40)
    
    # Draw a blue circle at those exact pixels
    canvas.create_oval(
        pixel_x - dot_radius, pixel_y - dot_radius, 
        pixel_x + dot_radius, pixel_y + dot_radius, 
        fill="royalblue", outline="black"
    )
    
    # Draw the text label just above the dot
    canvas.create_text(
        pixel_x, pixel_y - 15, 
        text=f"({x}, {y})", fill="black", font=("Arial", 10, "bold")
    )

# Run the application and show the window
root.mainloop()