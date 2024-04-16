from tkinter import *

def scroll_canvas(dx):
    # canvas.xview_scroll(dx, "units")
    canvas.scan_mark(0, 0)  # Set the reference point at the top-left corner of the canvas
    canvas.scan_dragto(dx, 0, gain=1)  # Shift the canvas by dx pixels horizontally

def print_canvas_bbox():
    bbox = canvas.bbox("all")
    print("Total canvas occupied bbox:", bbox)

root = Tk()
root.title("Canvas with Shift Buttons")




# import tkinter as tk






canvas_frame = Frame(root)
canvas_frame.pack(fill=BOTH, expand=YES)

canvas = Canvas(canvas_frame, bg="white")
canvas.pack(fill=BOTH, expand=YES)

# scrollbar = Scrollbar(canvas_frame, orient=HORIZONTAL, command=canvas.xview)
# scrollbar.pack( fill=X)

# canvas.configure(yscrollcommand=scrollbar.set)

# hbar=Scrollbar(canvas,orient=HORIZONTAL)
# hbar.pack(side=BOTTOM,fill=X)
# hbar.config(command=canvas.xview)

# Add 100 buttons to the canvas
button_height = 30
current_start = 0
for i in range(10):
    # create_square_boxes(20, "Text1", "Text2")
    # button = Button(canvas, text=f"Button {i+1}")
    button = Canvas(canvas, bg='green' if i%2 == 0 else 'red', width=150, height=150,border=0,borderwidth=0,highlightthickness=0)
    # button.pack()
    canvas.create_window(current_start, 0, anchor='nw', window=button)
    current_start += 150

# Buttons to shift canvas
shift_left_button = Button(root, text="Shift Left", command=lambda: scroll_canvas(-150))
shift_left_button.pack(side=LEFT, padx=5, pady=5)

shift_right_button = Button(root, text="Shift Right", command=lambda: scroll_canvas(150))
shift_right_button.pack(side=LEFT, padx=5, pady=5)

# Button to print total canvas occupied bbox
print_bbox_button = Button(root, text="Print Canvas BBox", command=print_canvas_bbox)
print_bbox_button.pack(side=LEFT, padx=5, pady=5)

root.mainloop()






