import tkinter as tk
from PIL import Image, ImageTk

class ResizableCanvas(tk.Canvas):
    def __init__(self, parent, *args, **kwargs):
        tk.Canvas.__init__(self, parent, *args, **kwargs)
        self.bind("<Configure>", self.on_resize)

    def on_resize(self, event):
        self.config(width=event.width, height=event.height)
        self.draw_image()

    def draw_image(self):
        self.delete("all")  # Clear previous image
        self.image = Image.open("sharamoni.png")  # Change "image.jpg" to your image file
        img_width, img_height = self.image.size
        canvas_width = self.winfo_width()
        canvas_height = self.winfo_height()

        if canvas_width / img_width < canvas_height / img_height:
            # Scale based on width
            scale_factor = canvas_width / img_width
        else:
            # Scale based on height
            scale_factor = canvas_height / img_height

        new_width = int(img_width * scale_factor)
        new_height = int(img_height * scale_factor)

        # Adjusting width and height to keep them within 50px
        if new_width > canvas_width - 50:
            new_width = canvas_width - 50
            new_height = int(new_width * img_height / img_width)
        elif new_height > canvas_height - 50:
            new_height = canvas_height - 50
            new_width = int(new_height * img_width / img_height)

        resized_img = self.image.resize((new_width, new_height), Image.LANCZOS)
        self.image_tk = ImageTk.PhotoImage(resized_img)

        x = (canvas_width - new_width) / 2
        y = (canvas_height - new_height) / 2

        self.create_image(x, y, anchor=tk.NW, image=self.image_tk)

root = tk.Tk()
root.title("Resizable Image Canvas")
root.geometry("600x400")

canvas = ResizableCanvas(root, bg="white", highlightthickness=0)
canvas.pack(fill=tk.BOTH, expand=True)

root.mainloop()
