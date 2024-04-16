from  tkinter import *
from PIL import Image, ImageTk

class ResizableCanvas(Canvas):
    image = None
    def __init__(self, parent, *args, **kwargs):
        Canvas.__init__(self, parent, *args, **kwargs)
        self.bind("<Configure>", self.on_resize)

    def on_resize(self, event):
        self.config(width=event.width, height=event.height)
        self.draw_image(image=self.image )
        
        # self.draw_grid()

    def draw_image(self,image = None):
        self.draw_grid()

        self.delete("image")  # Clear previous image
        if image != None : 
            self.image = image
            print('::>> ', self.image)
            # self.image = Image.open(image)  # Change "image.jpg" to your image file
            # self.image = Image.open("sharamoni.png")  # Change "image.jpg" to your image file

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

            self.create_image(x, y, anchor=NW, image=self.image_tk, tags="image")

        # self.draw_grid()

    def draw_grid(self):
        self.delete("grid")  # Clear previous grid
        canvas_width = self.winfo_width()
        canvas_height = self.winfo_height()

        # grid_size = min(canvas_width, canvas_height) // 100

        # # Draw horizontal lines
        # for i in range(0, canvas_height + grid_size, grid_size):
        #     self.create_line(0, i, canvas_width, i, tags="grid")

        # # Draw vertical lines
        # for j in range(0, canvas_width + grid_size, grid_size):
        #     self.create_line(j, 0, j, canvas_height, tags="grid")

        middle_width = canvas_width/2
        middle_width_negative = middle_width
        self.create_line(middle_width, 0, middle_width, canvas_height, tags="grid" , width= 2, fill='#4c4c4c', dash=(1,1))
        for i in range(int(middle_width)):
            middle_width += 20
            self.create_line(middle_width, 0, middle_width, canvas_height, tags="grid" , width= 1, fill='#cccccc', dash=(1,100,15))
            middle_width_negative -= 20
            self.create_line(middle_width_negative, 0, middle_width_negative, canvas_height, tags="grid" , width= 1, fill='#cccccc' , dash=(1,100,15))


        middle_height = canvas_height/2
        middle_height_negative = middle_height
        self.create_line(0, middle_height, canvas_width, middle_height, tags="grid" , width= 2 , fill='#4c4c4c', dash=(1,1))
        for i in range(int(middle_height)):
            middle_height += 20
            self.create_line(0, middle_height, canvas_width, middle_height, tags="grid" , width= 1, fill='#cccccc' , dash=(1,100,15))
            middle_height_negative -= 20
            self.create_line(0, middle_height_negative, canvas_width, middle_height_negative, tags="grid" , width= 1, fill='#cccccc' , dash=(1,100,15))






if __name__ == '__main__':
    root = Tk()
    root.title("Resizable Image Canvas with Grid")
    root.geometry("600x400")

    canvas = ResizableCanvas(root, bg="white", highlightthickness=0)
    canvas.pack(fill=BOTH, expand=True)

    root.mainloop()