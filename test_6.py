import tkinter as tk
from tkinter import ttk

class ZoomPanCanvas(tk.Canvas):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_line_width = 1
        self.bold_grid_line_width = 2
        self.zoom_scale = 1.0
        self.pan_x = 0
        self.pan_y = 0
        self.draw_grid()

    def draw_grid(self):
        self.delete("gridline")
        width = self.winfo_width()
        height = self.winfo_height()

        for x in range(-width, width, 20):
            if x % 100 == 0:  # Check if it's a major grid line
                self.create_line(x - self.pan_x, -height, x - self.pan_x, height, width=self.bold_grid_line_width, tags="gridline")
            else:
                self.create_line(x - self.pan_x, -height, x - self.pan_x, height, width=self.grid_line_width, tags="gridline")

        for y in range(-height, height, 20):
            if y % 100 == 0:  # Check if it's a major grid line
                self.create_line(-width, y - self.pan_y, width, y - self.pan_y, width=self.bold_grid_line_width, tags="gridline")
            else:
                self.create_line(-width, y - self.pan_y, width, y - self.pan_y, width=self.grid_line_width, tags="gridline")

    def zoom(self, factor):
        self.zoom_scale *= factor
        self.scale('all', 0, 0, factor, factor)
        self.draw_grid()

    def reset_zoom_pan(self):
        self.zoom_scale = 1.0
        self.pan_x = 0
        self.pan_y = 0
        self.delete("all")
        self.draw_grid()

    def pan(self, dx, dy):
        self.pan_x += dx
        self.pan_y += dy
        self.scan_dragto(dx, dy, gain=1)
        self.draw_grid()

    def get_scale_and_position(self):
        return self.zoom_scale, self.pan_x, self.pan_y

    def apply_custom_scale_and_position(self, scale, x, y):
        self.zoom_scale = scale
        self.pan_x = x
        self.pan_y = y
        self.scale('all', 0, 0, scale, scale)
        self.scan_mark(0, 0)
        self.scan_dragto(x, y, gain=1)
        self.draw_grid()

def main():
    root = tk.Tk()
    root.geometry("600x400")

    canvas = ZoomPanCanvas(root, bg="white")
    canvas.pack(fill=tk.BOTH, expand=True)

    def reset_zoom_pan():
        canvas.reset_zoom_pan()

    def zoom_in():
        canvas.zoom(1.2)

    def zoom_out():
        canvas.zoom(0.8)

    def get_scale_and_position():
        scale, x, y = canvas.get_scale_and_position()
        print(f"Current Scale: {scale}, Pan X: {x}, Pan Y: {y}")

    def apply_custom_scale_and_position():
        scale = float(scale_entry.get())
        x = int(x_entry.get())
        y = int(y_entry.get())
        canvas.apply_custom_scale_and_position(scale, x, y)

    reset_button = ttk.Button(root, text="Reset Zoom/Pan", command=reset_zoom_pan)
    reset_button.pack(side=tk.LEFT, padx=10)
    zoom_in_button = ttk.Button(root, text="Zoom In", command=zoom_in)
    zoom_in_button.pack(side=tk.LEFT, padx=10)
    zoom_out_button = ttk.Button(root, text="Zoom Out", command=zoom_out)
    zoom_out_button.pack(side=tk.LEFT, padx=10)
    get_scale_position_button = ttk.Button(root, text="Get Scale/Position", command=get_scale_and_position)
    get_scale_position_button.pack(side=tk.LEFT, padx=10)

    scale_label = ttk.Label(root, text="Scale:")
    scale_label.pack(side=tk.LEFT, padx=10)
    scale_entry = ttk.Entry(root)
    scale_entry.pack(side=tk.LEFT)

    x_label = ttk.Label(root, text="X:")
    x_label.pack(side=tk.LEFT, padx=10)
    x_entry = ttk.Entry(root)
    x_entry.pack(side=tk.LEFT)

    y_label = ttk.Label(root, text="Y:")
    y_label.pack(side=tk.LEFT, padx=10)
    y_entry = ttk.Entry(root)
    y_entry.pack(side=tk.LEFT)

    apply_button = ttk.Button(root, text="Apply", command=apply_custom_scale_and_position)
    apply_button.pack(side=tk.LEFT, padx=10)

    root.mainloop()

if __name__ == "__main__":
    main()
