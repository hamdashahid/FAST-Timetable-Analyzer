# dict = {
#     'PF': {
#         'Monday Lec': {
#             'Room': [],
#             'Time': []
#             },
#         'Monday Labs': {
#             'Room': [],
#             'Time': []
#         } 
#     }       
# }

import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Scrollable Frame Example")
root.geometry("400x300")

# Create a canvas widget
canvas = tk.Canvas(root)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Add a vertical scrollbar linked to the canvas
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill="y")
canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame inside the canvas
scrollable_frame = ttk.Frame(canvas)

# Add the frame to the canvas window (using `window` attribute)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# Configure the frame to expand with the canvas
scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Add some content to the frame
for i in range(50):
    tk.Label(scrollable_frame, text=f"Label {i+1}").pack()

# Function to handle mouse scroll within the canvas
def on_mouse_wheel(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

canvas.bind_all("<MouseWheel>", on_mouse_wheel)  # Bind mouse wheel for Windows/Mac

# Run the main loop
root.mainloop()
