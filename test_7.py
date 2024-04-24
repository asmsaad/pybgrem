import tkinter as tk

def show_text(event):
    canvas.itemconfig(text_id, state="normal")

def hide_text(event):
    canvas.itemconfig(text_id, state="hidden")

root = tk.Tk()
root.title("Show/Hide Text on Canvas")

canvas = tk.Canvas(root, width=200, height=100)
canvas.pack()

# Create the text item on canvas
text_id = canvas.create_text(100, 50, text="Hover over me!", font=("Arial", 12), state="hidden")

# Bind mouse enter and leave events to show and hide text
canvas.bind("<Enter>", show_text)
canvas.bind("<Leave>", hide_text)

root.mainloop()
