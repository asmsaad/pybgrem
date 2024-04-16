# # todo canvas 2 perfevct
# import tkinter as tk
# from PIL import Image, ImageTk

# global origin_GLOBAL
# origin_GLOBAL = None
# def create_zoomable_canvas(master, diameter, *args, **kwargs):
#     canvas = tk.Canvas(master, *args, **kwargs)
#     canvas.diameter = diameter
#     canvas.scale_factor = 1.0

#     # origX = canvas.xview()[0]
#     # origY = canvas.yview()[0]
#     # print('(origX,origY)', (origX,origY))

#     bbox = canvas.bbox("all")
#     print(bbox)



#     def center_image():
#         canvas_width = canvas.winfo_width()
#         canvas_height = canvas.winfo_height()
#         image_width = image.width()
#         image_height = image.height()

#         # Calculate coordinates to place the image at the center
#         x = (canvas_width - image_width) / 2
#         y = (canvas_height - image_height) / 2

#         canvas.coords(image, x, y)  # Update image position








#     def zoom(event):
#         if event.delta > 0:
#             if canvas.scale_factor < 1 : canvas.scale_factor = 1  
#             canvas.scale_factor *= 1.01
#         else:
#             if canvas.scale_factor > 1 : canvas.scale_factor = 1  
#             canvas.scale_factor /= 1.01

#         # Apply zoom restrictions
#         if canvas.scale_factor < 0.5:
#             canvas.scale_factor = 0.5
#         elif canvas.scale_factor > 5.0:
#             canvas.scale_factor = 5.0

#         old_width = canvas.winfo_width()
#         old_height = canvas.winfo_height()

#         canvas.scale("all", 0, 0, canvas.scale_factor, canvas.scale_factor)

#         new_width = canvas.winfo_width()
#         new_height = canvas.winfo_height()

#         # Calculate translation to keep the canvas centered
#         dx = (new_width - old_width) / 2
#         dy = (new_height - old_height) / 2

#         canvas.move("all", dx, dy)

#     def pan_start(event):
#         canvas.scan_mark(event.x, event.y)

#     def pan_move(event):
#         canvas.scan_dragto(event.x, event.y, gain=1)

#     def draw_grid():
#         for i in range(0, diameter + 1, 10):
#             canvas.create_line(i, 0, i, diameter, fill="gray")
#             canvas.create_line(0, i, diameter, i, fill="gray")

#     def draw_center_lines():
#         canvas.create_line(0, diameter // 2, diameter, diameter // 2, fill="black", width=2)
#         canvas.create_line(diameter // 2, 0, diameter // 2, diameter, fill="black", width=2)

#     def go_to_center(event):
#         # canvas.xview_moveto(0.5)
#         # canvas.yview_moveto(0.5)
#         global origin_GLOBAL
#         x, y = origin_GLOBAL
#         canvas.yview_moveto(x)
#         canvas.xview_moveto(y)

#     def zoom_100(event):
#         # # canvas.scale_factor = 1.0
#         # canvas.config(height=500, width=50)
#         # canvas.scale("all", 0, 0, 2, 2)
#         canvas.xview_moveto(origX)
#         canvas.yview_moveto(origY)

#         # print('current_scal_factor :' , canvas.scale_factor)
#         # bbox = canvas.bbox("all")
#         # print(bbox)
#         # canvas['scrollregion'] = (-30,-30,1500,1500)
#         # bbox = canvas.bbox("all")
#         # print(bbox)

#         # canvas.scale('all', 0, 0, 1+canvas.scale_factor, 1+canvas.scale_factor)  # Reset scaling to 1
#         # canvas.xview_moveto(0)  # Reset horizontal pan
#         # canvas.yview_moveto(0)  # Reset vertical pan


#     def on_configure(event):
#         canvas.itemconfig("all", width=event.width / diameter)
#         if canvas.image:
#             canvas.delete(canvas.image)
#             canvas.image = tk.PhotoImage(file="sam.png")
#             canvas.create_image(diameter / 2, diameter / 2, image=canvas.image)


#     canvas.bind("<MouseWheel>", zoom)
#     canvas.bind("<Button-2>", pan_start)
#     canvas.bind("<B2-Motion>", pan_move)
#     canvas.bind("<Configure>", on_configure)

#     draw_grid()
#     draw_center_lines()

#     master.bind("<Control-c>", lambda event: go_to_center(event))
#     master.bind("<Control-f>", lambda event: zoom_100(event))

#     global origin_GLOBAL
#     origin_GLOBAL = canvas.xview()[0], canvas.yview()[0]


#     # #Load an image in the script
#     # img= ImageTk.PhotoImage(Image.open("sam.png"))

#     # #Add image to the Canvas Items
#     # canvas.create_image(10,10,anchor='nw',image=img)

#     # image = tk.PhotoImage(file='sam.png')
#     # canvas.create_image(0, 0, image=image, anchor=tk.CENTER)
#     # # center_image()

#     return canvas

# def main():
#     diameter = 2000

#     root = tk.Tk()
#     root.title("Zoomable Canvas")

#     canvas = create_zoomable_canvas(root, diameter, width=diameter, height=diameter, bg="white")
#     canvas.pack(fill="both", expand=True)

#     #Load an image in the script
#     # img= ImageTk.PhotoImage(Image.open("sam.png"))
#     # #Add image to the Canvas Items
#     # canvas.create_image(10,10,anchor='nw',image=img)


#     def fun():
#         canvas.scale_factor = 1
#         canvas.scale("all", 0, 0, 2, 2)

#     a = tk.Button(root, text='center', command=fun)
#     a.pack()

#     root.mainloop()

# if __name__ == "__main__":
#     main()




import tkinter as tk

def create_zoomable_canvas(master, diameter, image_path=None, *args, **kwargs):
    canvas = tk.Canvas(master, *args, **kwargs)
    canvas.diameter = diameter
    canvas.scale_factor = 1.0
    canvas.image = None

    if image_path:
        image = tk.PhotoImage(file=image_path)
        canvas.image = image
        canvas.create_image(diameter / 2, diameter / 2, image=image)

    def zoom(event):
        if event.delta > 0:
            canvas.scale_factor *= 1.1
        else:
            canvas.scale_factor /= 1.1

        # Apply zoom restrictions
        if canvas.scale_factor < 0.5:
            canvas.scale_factor = 0.5
        elif canvas.scale_factor > 5.0:
            canvas.scale_factor = 5.0

        old_width = canvas.winfo_width()
        old_height = canvas.winfo_height()

        canvas.scale("all", 0, 0, canvas.scale_factor, canvas.scale_factor)

        new_width = canvas.winfo_width()
        new_height = canvas.winfo_height()

        # Calculate translation to keep the canvas centered
        dx = (new_width - old_width) / 2
        dy = (new_height - old_height) / 2

        canvas.move("all", dx, dy)

    def pan_start(event):
        canvas.scan_mark(event.x, event.y)

    def pan_move(event):
        canvas.scan_dragto(event.x, event.y, gain=1)

    def draw_grid():
        for i in range(0, diameter + 1, 10):
            canvas.create_line(i, 0, i, diameter, fill="gray")
            canvas.create_line(0, i, diameter, i, fill="gray")

    def draw_center_lines():
        canvas.create_line(0, diameter // 2, diameter, diameter // 2, fill="black", width=2)
        canvas.create_line(diameter // 2, 0, diameter // 2, diameter, fill="black", width=2)

    def go_to_center():
        canvas.xview_moveto(0.5)
        canvas.yview_moveto(0.5)

    def zoom_100():
        canvas.scale_factor = 1.0
        canvas.scale("all", 0, 0, 1, 1)

    def on_configure(event):
        canvas.itemconfig("all", width=500 / diameter)
        if canvas.image:
            canvas.delete(canvas.image)
            canvas.image = tk.PhotoImage(file=image_path)
            canvas.create_image(diameter / 2, diameter / 2, image=canvas.image)

    canvas.bind("<MouseWheel>", zoom)
    canvas.bind("<Button-2>", pan_start)
    canvas.bind("<B2-Motion>", pan_move)
    canvas.bind("<Configure>", on_configure)

    draw_grid()
    draw_center_lines()

    master.bind("<Control-c>", lambda event: go_to_center())
    master.bind("<Control-0>", lambda event: zoom_100())

    return canvas

def main():
    diameter = int(input("Enter the diameter of the canvas: "))
    image_path = input("Enter the path to the image (leave blank for no image): ")

    root = tk.Tk()
    root.title("Zoomable Canvas")

    canvas = create_zoomable_canvas(root, diameter, image_path=image_path, bg="white")
    canvas.pack(fill="both", expand=True)

    root.mainloop()

if __name__ == "__main__":
    main()
