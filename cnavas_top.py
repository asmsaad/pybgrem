# import tkinter as tk
# from PIL import Image, ImageTk

# class ImageStackerApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Image Stacker")

#         # Load images
#         self.image1 = Image.open("moon.png")
#         self.image2 = Image.open("sharamoni.png")

#         # Convert images to PhotoImage objects
#         self.photo_image1 = ImageTk.PhotoImage(self.image1)
#         self.photo_image2 = ImageTk.PhotoImage(self.image2)

#         # Create canvas
#         self.canvas = tk.Canvas(self.root, width=self.image1.width, height=self.image1.height)
#         self.canvas.pack()

#         # Display images on canvas
#         self.image1_id = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo_image1)
#         self.image2_id = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo_image2)

#         # Create scale for transparency
#         self.transparency_scale = tk.Scale(self.root, from_=0, to=1, resolution=0.01, orient=tk.HORIZONTAL, label="Transparency", command=self.adjust_transparency)
#         self.transparency_scale.pack()

#         # Create buttons
#         self.btn_image1_top = tk.Button(self.root, text="Image 1 on top", command=self.bring_image1_to_top)
#         self.btn_image1_top.pack(side=tk.LEFT, padx=5, pady=5)
#         self.btn_image2_top = tk.Button(self.root, text="Image 2 on top", command=self.bring_image2_to_top)
#         self.btn_image2_top.pack(side=tk.LEFT, padx=5, pady=5)

#         # Initial transparency value
#         self.transparency = 1

#     def adjust_transparency(self, value):
#         self.transparency = float(value)
#         self.image1 = Image.open("moon.png").convert("RGBA")
#         self.image1.putalpha(int(255 * self.transparency))
#         self.photo_image1 = ImageTk.PhotoImage(self.image1)
#         self.canvas.itemconfig(self.image1_id, image=self.photo_image1)

#     def bring_image1_to_top(self):
#         self.canvas.tag_raise(self.image1_id)

#     def bring_image2_to_top(self):
#         self.canvas.tag_raise(self.image2_id)

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = ImageStackerApp(root)
#     root.mainloop()


#todo 

import tkinter as tk
from PIL import Image, ImageTk, ImageEnhance

class ImageStackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Stacker")

        # Load images
        self.image1 = Image.open("moon.png").convert("RGBA")
        self.image2 = Image.open("sharamoni.png").convert("RGBA")

        # Create canvas
        self.canvas = tk.Canvas(self.root, width=self.image1.width, height=self.image1.height)
        self.canvas.pack()

        # Display images on canvas
        self.photo_image1 = ImageTk.PhotoImage(self.image1)
        self.photo_image2 = ImageTk.PhotoImage(self.image2)
        self.image1_id = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo_image1)
        self.image2_id = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo_image2)

        # Create scale for transparency
        self.transparency_scale = tk.Scale(self.root, from_=0, to=1, resolution=0.01, orient=tk.HORIZONTAL, label="Transparency", command=self.adjust_transparency)
        self.transparency_scale.pack()

        # Create buttons
        self.btn_image1_top = tk.Button(self.root, text="Image 1 on top", command=self.bring_image1_to_top)
        self.btn_image1_top.pack(side=tk.LEFT, padx=5, pady=5)
        self.btn_image2_top = tk.Button(self.root, text="Image 2 on top", command=self.bring_image2_to_top)
        self.btn_image2_top.pack(side=tk.LEFT, padx=5, pady=5)

        # Initial transparency value
        self.transparency = 1

    def adjust_transparency(self, value):
        self.transparency = float(value)
        self.image1 = Image.open("moon.png").convert("RGBA")
        self.image2 = Image.open("sharamoni.png").convert("RGBA")
        img1_alpha = Image.new("RGBA", self.image1.size, (255, 255, 255, int(255 * self.transparency)))
        self.image1 = Image.alpha_composite(self.image1, img1_alpha)
        self.photo_image1 = ImageTk.PhotoImage(self.image1)
        self.canvas.itemconfig(self.image1_id, image=self.photo_image1)

    def bring_image1_to_top(self):
        self.canvas.tag_raise(self.image1_id)

    def bring_image2_to_top(self):
        self.canvas.tag_raise(self.image2_id)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageStackerApp(root)
    root.mainloop()


# #todo transparent bg
# import tkinter as tk

# def draw_chess_table(canvas):
#     colors = ['#FFFFFF', '#CCCCCC']  # alternate colors for chessboard
#     for i in range(8):
#         for j in range(8):
#             color = colors[(i + j) % 2]
#             canvas.create_rectangle(i * 50, j * 50, (i + 1) * 50, (j + 1) * 50, fill=color)

# root = tk.Tk()
# root.title("Transparent Chess Table")

# # Load a transparent PNG image
# transparent_image = tk.PhotoImage(file="more.png")

# # Create a canvas with transparent background using the transparent image
# canvas = tk.Canvas(root, width=400, height=400, bg='black')
# canvas.create_image(200, 200, image=transparent_image)  # Center the transparent image
# canvas.pack()

# # Draw the chess table
# draw_chess_table(canvas)

# root.mainloop()

