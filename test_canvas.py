# # todo canvas 2 perfevct
import tkinter as tk
from PIL import Image, ImageTk

global origin_GLOBAL
origin_GLOBAL = None
def create_zoomable_canvas(master, diameter, *args, **kwargs):
    canvas = tk.Canvas(master, *args, **kwargs)
    canvas.diameter = diameter
    canvas.scale_factor = 1.0
    

    # origX = canvas.xview()[0]
    # origY = canvas.yview()[0]
    # print('(origX,origY)', (origX,origY))

    bbox = canvas.bbox("all")
    print(bbox)


    # def load_image():
    #     image = Image.open("sam.png")  # Change "your_image.jpg" to the path of your image
    #     width, height = image.size

    #     # Resize the image to fit within the canvas
    #     if width > 500 or height > 500:
    #         ratio = min(500 / width, 500 / height)
    #         width = int(width * ratio)
    #         height = int(height * ratio)
    #         image = image.resize((width, height), Image.LANCZOS)

    #     canvas.orig_img = ImageTk.PhotoImage(image)
    #     canvas.image_ref = canvas.create_image(
    #         0, 0, image=canvas.orig_img, anchor="nw"
    #     )
    #     # canvas.scale_image_ref(width / 2, height / 2)

    def zoom(event):
        print(canvas.scale_factor , end = '\t')
        if event.delta > 0:
            if canvas.scale_factor < 1 : canvas.scale_factor = 1  
            canvas.scale_factor *= 1.01
            print("In" , end = '\t')
        else:
            if canvas.scale_factor > 1 : canvas.scale_factor = 1  
            canvas.scale_factor /= 1.01
            print("Out" , end = '\t')

        print(canvas.scale_factor)

        # Apply zoom restrictions
        if canvas.scale_factor < 0.95:
            canvas.scale_factor = 0.95

        elif canvas.scale_factor > 1.15:
            canvas.scale_factor = 1.15

        # old_width = canvas.winfo_width()
        # old_height = canvas.winfo_height()

        canvas.scale("all", 0, 0, canvas.scale_factor, canvas.scale_factor)

        # new_width = canvas.winfo_width()
        # new_height = canvas.winfo_height()

        # # Calculate translation to keep the canvas centered
        # dx = (new_width - old_width) / 2
        # dy = (new_height - old_height) / 2

        # canvas.move("all", dx, dy)

    def pan_start(event):
        canvas.scan_mark(event.x, event.y)

    def pan_move(event):
        canvas.scan_dragto(event.x, event.y, gain=1)

    def draw_grid():
        # load_image()
        for i in range(0, diameter + 1, 10):
            canvas.create_line(i, 0, i, diameter, fill="gray")
            canvas.create_line(0, i, diameter, i, fill="gray")

    def draw_center_lines():
        canvas.create_line(0, diameter // 2, diameter, diameter // 2, fill="black", width=2)
        canvas.create_line(diameter // 2, 0, diameter // 2, diameter, fill="black", width=2)


        #test
        # canvas.image_ref = canvas.create_image(0, 0, image=canvas.orig_img, anchor="nw")


    def go_to_center(event):
        # canvas.xview_moveto(0.5)
        # canvas.yview_moveto(0.5)
        # global origin_GLOBAL
        # x, y = origin_GLOBAL
        # canvas.yview_moveto(x)
        # canvas.xview_moveto(y)
        ...

    def zoom_100(event):
        # # canvas.scale_factor = 1.0
        # canvas.config(height=500, width=50)
        # canvas.scale("all", 0, 0, 2, 2)
        # canvas.xview_moveto(origX)
        # canvas.yview_moveto(origY)

        # print('current_scal_factor :' , canvas.scale_factor)
        # bbox = canvas.bbox("all")
        # print(bbox)
        # canvas['scrollregion'] = (-30,-30,1500,1500)
        # bbox = canvas.bbox("all")
        # print(bbox)

        # canvas.scale('all', 0, 0, 1+canvas.scale_factor, 1+canvas.scale_factor)  # Reset scaling to 1
        # canvas.xview_moveto(0)  # Reset horizontal pan
        # canvas.yview_moveto(0)  # Reset vertical pan
        ...

    canvas.bind("<MouseWheel>", zoom)
    canvas.bind("<Button-2>", pan_start)
    canvas.bind("<B2-Motion>", pan_move)

    draw_grid()
    draw_center_lines()
    # load_image()


    master.bind("<Control-c>", lambda event: go_to_center(event))
    master.bind("<Control-f>", lambda event: zoom_100(event))

    # global origin_GLOBAL
    # origin_GLOBAL = canvas.xview()[0], canvas.yview()[0]

    return canvas




















def main():
    diameter = 500

    root = tk.Tk()
    root.title("Zoomable Canvas")

    canvas = create_zoomable_canvas(root, diameter, width=diameter, height=diameter, bg="white")
    canvas.pack(fill="both", expand=True)



    def load_image():
        image = Image.open("sam.png")  # Change "your_image.jpg" to the path of your image
        width, height = image.size

        # Resize the image to fit within the canvas
        if width > 500 or height > 500:
            ratio = min(500 / width, 500 / height)
            width = int(width * ratio)
            height = int(height * ratio)
            image = image.resize((width, height), Image.LANCZOS)

        canvas.orig_img = ImageTk.PhotoImage(image)
        canvas.image_ref = canvas.create_image(
            0, 0, image=canvas.orig_img, anchor="nw"
        )
        # canvas.scale_image_ref(width / 2, height / 2)


    # load_image()

    def fun():
        canvas.scale_factor = 1
        canvas.scale("all", 0, 0, 2, 2)

    a = tk.Button(root, text='center', command=fun)
    a.pack()

    root.mainloop()

if __name__ == "__main__":
    main()