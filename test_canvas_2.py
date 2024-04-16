import tkinter as tk
from PIL import Image, ImageTk

class ImageCanvas:
    def __init__(self, master=None, **kwargs):
        self.master = master
        self.canvas = tk.Canvas(master, **kwargs)
        self.image = None
        self.canvas.bind("<Configure>", self.on_configure)

    def on_configure(self, event):
        self.draw_image()

    def draw_image(self):
        if self.image:
            self.canvas.delete("all")  # Clear canvas
            w, h = self.canvas.winfo_width(), self.canvas.winfo_height()
            border = 50
            image_w = self.image.width()
            image_h = self.image.height()
            scale = min((w - 2 * border) / image_w, (h - 2 * border) / image_h)
            image_w, image_h = int(image_w * scale), int(image_h * scale)
            x = (w - image_w) // 2
            y = (h - image_h) // 2
            self.canvas.create_image(x, y, anchor=tk.NW, image=self.image, tags="image")
            self.draw_grid(w, h, border)

    def draw_grid(self, width, height, border):
        step = 20  # Grid spacing
        bold_width = 2
        for x in range(border, width - border, step):
            if x == (width - border - border) // 2:
                self.canvas.create_line(x, border, x, height - border, width=bold_width)
            else:
                self.canvas.create_line(x, border, x, height - border)
        for y in range(border, height - border, step):
            if y == (height - border - border) // 2:
                self.canvas.create_line(border, y, width - border, y, width=bold_width)
            else:
                self.canvas.create_line(border, y, width - border, y)

class App:
    def __init__(self, master):
        self.master = master
        self.canvas = ImageCanvas(master, bg="white", highlightthickness=0)
        self.canvas.canvas.pack(expand=True, fill=tk.BOTH)
        self.load_image("sharamoni.png")

    def load_image(self, filename):
        image = Image.open(filename)
        self.canvas.image = ImageTk.PhotoImage(image)
        self.canvas.draw_image()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Image Canvas with Grid")
    app = App(root)
    root.mainloop()
