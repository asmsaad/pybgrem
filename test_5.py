import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class CanvasWithImage(tk.Canvas):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_enabled = False
        self.grid_size_mm = 10
        self.current_image = None
        self.original_image = None
        self.image_ref = None
        self.bind("<Button-2>", self.pan_image)
        self.bind("<MouseWheel>", self.zoom_image)

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.original_image = Image.open(file_path)
            self.show_image()

    def show_image(self):
        if self.original_image:
            self.current_image = ImageTk.PhotoImage(self.original_image)
            self.create_image(self.winfo_width() / 2, self.winfo_height() / 2, anchor=tk.CENTER, image=self.current_image)

    def zoom_image(self, event):
        if self.original_image:
            scale = 1.2 if event.delta > 0 else 0.8
            self.scale(tk.ALL, event.x, event.y, scale, scale)

    def pan_image(self, event):
        if self.original_image:
            self.scan_mark(event.x, event.y)
            self.bind("<B2-Motion>", lambda e: self.scan_dragto(e.x, e.y, gain=1))

    def toggle_grid(self):
        self.grid_enabled = not self.grid_enabled
        self.delete("grid")
        if self.grid_enabled:
            width = self.winfo_width()
            height = self.winfo_height()
            for i in range(0, width, int(self.grid_size_mm * self.original_image.width / self.original_image.size[0])):
                self.create_line(i, 0, i, height, width=1, tags="grid")
            for j in range(0, height, int(self.grid_size_mm * self.original_image.height / self.original_image.size[1])):
                self.create_line(0, j, width, j, width=1, tags="grid")
            self.create_rectangle(width / 2 - 2, height / 2 - 2, width / 2 + 2, height / 2 + 2, fill="black", tags="grid")
            self.add_grid_labels()

    def add_grid_labels(self):
        width = self.winfo_width()
        height = self.winfo_height()
        for i in range(0, width, int(self.grid_size_mm * self.original_image.width / self.original_image.size[0])):
            self.create_text(i, 10, text=str(round(i / (self.original_image.width / self.original_image.size[0]) * self.grid_size_mm, 1)) + "mm", anchor=tk.NW, tags="grid")
        for j in range(0, height, int(self.grid_size_mm * self.original_image.height / self.original_image.size[1])):
            self.create_text(10, j, text=str(round(j / (self.original_image.height / self.original_image.size[1]) * self.grid_size_mm, 1)) + "mm", anchor=tk.NW, tags="grid")

    def fit_content(self):
        if self.original_image:
            self.delete(tk.ALL)
            self.show_image()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Image Viewer")

        self.canvas = CanvasWithImage(self)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        load_button = tk.Button(self, text="Load Image", command=self.canvas.load_image)
        load_button.pack(side=tk.TOP)

        grid_button = tk.Button(self, text="Toggle Grid", command=self.canvas.toggle_grid)
        grid_button.pack(side=tk.TOP)

        fit_button = tk.Button(self, text="Fit Content", command=self.canvas.fit_content)
        fit_button.pack(side=tk.TOP)

if __name__ == "__main__":
    app = App()
    app.mainloop()
