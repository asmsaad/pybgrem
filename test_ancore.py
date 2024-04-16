import tkinter as tk
from tkinter import ttk

class ScrollableFrame(tk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


def scroll_to_button(button):
    canvas = button.master.master.master.canvas
    canvas_height = canvas.winfo_height()
    button_height = button.winfo_height()
    y = button.winfo_y() - (canvas_height - button_height) / 2
    canvas.yview_moveto(y / canvas_height)

def main():
    root = tk.Tk()
    root.title("Scrollable Frame Example")
    root.geometry("600x400")

    left_frame = tk.Frame(root)
    left_frame.pack(side="left", fill="both", expand=True)

    listbox = tk.Listbox(left_frame)
    for i in range(1, 101):
        listbox.insert("end", i)
    listbox.pack(side="left", fill="y")

    right_frame = ScrollableFrame(root)
    right_frame.pack(side="right", fill="both", expand=True)

    buttons = []
    for i in range(1, 101):
        button = tk.Button(right_frame.scrollable_frame, text=str(i), width=10, height=5)
        button.grid(row=(i-1)//10, column=(i-1)%10)
        buttons.append(button)

    def on_listbox_select(event):
        selection = event.widget.curselection()
        if selection:
            index = int(selection[0])
            button = buttons[index]
            scroll_to_button(button)

    listbox.bind("<<ListboxSelect>>", on_listbox_select)

    root.mainloop()

if __name__ == "__main__":
    main()
