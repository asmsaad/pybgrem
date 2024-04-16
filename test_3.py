import tkinter as tk
from PIL import Image, ImageTk

class ZoomableCanvas(tk.Canvas):
    def __init__(self, parent, **kwargs):
        tk.Canvas.__init__(self, parent, **kwargs)
        self.bind("<Configure>", self.configure_event)
        self.bind("<ButtonPress-3>", self.scroll_start)
        self.bind("<B3-Motion>", self.scroll_move)
        self.bind("<MouseWheel>", self.zoom)
        # self.bind("<Button-5>", self.zoom_out)
        # self.bind("<Button-4>", self.zoom_in)
        self.image = None
        self.image_ref = None
        self.orig_img = None
        self.scale = 1.0
        self.offset_x = 0
        self.offset_y = 0
        self.middle_line_width = 3
        self.draw_grid()

    def configure_event(self, event):
        self.configure(scrollregion=self.bbox("all"))

    def scroll_start(self, event):
        self.scan_mark(event.x, event.y)

    def scroll_move(self, event):
        self.scan_dragto(event.x, event.y, gain=1)

    def zoom(self, event):
        print(self.bbox())
        if event.delta > 0:
            # if self.scale < 1 : self.scale = 1  
            # self.scale *= 1.01
            print('[In]', end=' ')
            scale_factor = 1.1
            x = self.canvasx(event.x)
            y = self.canvasy(event.y)
            self.scale *= scale_factor
            self.scale = min(10.0, max(0.1, self.scale))  # Limit scale factor
            self.scale_canvas(self.scale, x, y)
            print(self.scale , x , y )
        
        else:
            # if self.scale > 1 : self.scale = 1  
            # self.scale /= 1.01
            print('[Out]', end=' ')
            scale_factor = 0.9
            x = self.canvasx(event.x)
            y = self.canvasy(event.y)
            self.scale *= scale_factor
            self.scale = min(10.0, max(0.1, self.scale))  # Limit scale factor
            self.scale_canvas(self.scale, x, y)
            print(self.scale , x , y )




        # self.scale("all", 0, 0, self.scale, self.scale)


    def zoom_in(self, event):
        self.zoom(event)

    def zoom_out(self, event):
        scale_factor = 0.9
        x = self.canvasx(event.x)
        y = self.canvasy(event.y)
        self.scale *= scale_factor
        self.scale = min(10.0, max(0.1, self.scale))  # Limit scale factor
        self.scale_canvas(self.scale, x, y)

    def scale_canvas(self, scale, x, y):
        self.scale = scale
        self.delete(self.image_ref)
        self.image_ref = self.create_image(
            self.offset_x, self.offset_y, image=self.orig_img, anchor="nw"
        )
        self.scale_image_ref(x, y)

    def scale_image_ref(self, x, y):
        self.scale = min(10.0, max(0.1, self.scale))  # Limit scale factor
        self.scale_x = self.scale_y = self.scale
        self.offset_x = x - self.scale_x * (x - self.offset_x)
        self.offset_y = y - self.scale_y * (y - self.offset_y)
        self.delete(self.image_ref)
        self.image_ref = self.create_image(
            self.offset_x, self.offset_y, image=self.orig_img, anchor="nw"
        )

    def draw_grid(self):
        width = self.winfo_reqwidth()
        height = self.winfo_reqheight()

        # Draw vertical lines
        for i in range(0, width, 20):
            if i == width / 2:
                self.create_line(i, 0, i, height, width=self.middle_line_width)
            else:
                self.create_line(i, 0, i, height)

        # Draw horizontal lines
        for i in range(0, height, 20):
            if i == height / 2:
                self.create_line(0, i, width, i, width=self.middle_line_width)
            else:
                self.create_line(0, i, width, i)


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Zoomable Canvas")
        self.geometry("500x500")

        self.canvas = ZoomableCanvas(self, bg="white", width=500, height=500)
        self.canvas.pack(fill=tk.BOTH, expand=tk.YES)

        self.load_image()

    def load_image(self):
        image = Image.open("sam.png")  # Change "your_image.jpg" to the path of your image
        width, height = image.size

        # Resize the image to fit within the canvas
        if width > 500 or height > 500:
            ratio = min(500 / width, 500 / height)
            width = int(width * ratio)
            height = int(height * ratio)
            image = image.resize((width, height), Image.LANCZOS)

        self.canvas.orig_img = ImageTk.PhotoImage(image)
        self.canvas.image_ref = self.canvas.create_image(
            0, 0, image=self.canvas.orig_img, anchor="nw"
        )
        self.canvas.scale_image_ref(width / 2, height / 2)


if __name__ == "__main__":
    app = App()
    app.mainloop()
