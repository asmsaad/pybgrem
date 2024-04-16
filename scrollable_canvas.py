import tkinter as tk

def bind_mousewheel(event):
    canvas.bind_all("<MouseWheel>", on_mousewheel)

def unbind_mousewheel(event):
    canvas.unbind_all("<MouseWheel>")

def on_mousewheel(event):
    if event.delta < 0:
        canvas.xview_scroll(1, "units")
    else:
        canvas.xview_scroll(-1, "units")

def configure_inner_frame(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

root = tk.Tk()
root.geometry("400x200")
root.title("Scrollable Canvas Example")

canvas = tk.Canvas(root, bg="white")
scrollbar = tk.Scrollbar(root, orient="horizontal", command=canvas.xview)
canvas.config(xscrollcommand=scrollbar.set)

scrollbar.pack(side="bottom", fill="x")
canvas.pack(side="left", fill="both", expand=True)

canvas.bind("<Enter>", bind_mousewheel)
canvas.bind("<Leave>", unbind_mousewheel)

# inner_frame = tk.Frame(canvas, bg="white")
# canvas.create_window((0, 0), window=inner_frame, anchor="nw")

# inner_frame.bind("<Configure>", configure_inner_frame)

# Adding some widgets to test scrolling
for i in range(20):
    # label = tk.Label(inner_frame, text=f"Label {i}", padx=10, pady=5, bg="lightgray")
    # label.grid(row=1, column=i, padx=5, pady=5)
    inner_frame = tk.Frame(canvas, bg= "black" if i%2 == 0 else "white")
    canvas.create_window((i*50, 0), window=inner_frame, anchor="nw")
    inner_frame.bind("<Configure>", configure_inner_frame)

root.mainloop()
