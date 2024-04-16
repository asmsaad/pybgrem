# import tkinter as tk

# def print_menu_option(option):
#     print(option)

# def create_submenu(menu, submenu_name, options):
#     submenu = Menu(menu, tearoff=0)
#     for option in options:
#         submenu.add_command(label=option, command=lambda opt=option: print_menu_option(opt))
#     menu.add_cascade(label=" " + submenu_name, menu=submenu)

# def main():
#     root = Tk()
#     root.title("Menubar Example")

#     menubar = Menu(root)

#     file_menu = Menu(menubar, tearoff=0)
#     file_menu.add_command(label="Open", command=lambda: print_menu_option("New") , state="disabled")
#     file_menu.add_separator()
#     file_menu.add_command(label="Image", command=lambda: print_menu_option("New"))
#     file_menu.add_command(label="Folder", command=lambda: print_menu_option("Open"))
#     file_menu.add_command(label="Video", command=lambda: print_menu_option("Save"))
#     file_menu.add_separator()
#     file_menu.add_command(label="Exit", command=root.quit)
#     menubar.add_cascade(label=" File", menu=file_menu)

#     edit_menu = Menu(menubar, tearoff=0)
#     edit_menu.add_command(label="Cut", command=lambda: print_menu_option("Cut"))
#     edit_menu.add_command(label="Copy", command=lambda: print_menu_option("Copy"))
#     edit_menu.add_command(label="Paste", command=lambda: print_menu_option("Paste"))
#     menubar.add_cascade(label=" Edit", menu=edit_menu)

#     options_menu = Menu(menubar, tearoff=0)
#     create_submenu(options_menu, "Options 1", ["Option 1.1", "Option 1.2", "Option 1.3"])
#     create_submenu(options_menu, "Options 2", ["Option 2.1", "Option 2.2", "Option 2.3"])
#     menubar.add_cascade(label=" Options", menu=options_menu)

#     root.config(menu=menubar)
#     root.mainloop()

# if __name__ == "__main__":
#     main()





# #todo workabel 
# from tkinter import *

# def do_something():
#     print("Menu item clicked")

# root = Tk()

# # Create a menu bar
# menubar = Menu(root, bg="black", fg="white" )

# # Create a file menu
# file_menu = Menu(menubar, tearoff=0, bg="white", fg="black" )
# file_menu.add_command(label="New", command=do_something, accelerator="Ctrl+N" , )
# file_menu.add_command(label="Open", command=do_something, accelerator="Ctrl+O")
# file_menu.add_command(label="Save", command=do_something, accelerator="Ctrl+S")
# file_menu.add_separator()
# file_menu.add_command(label="media", command=do_something, accelerator="D:\DODO_PAPA\Manim\media")
# file_menu.add_separator()
# file_menu.add_command(label="Exit", command=root.quit)
# menubar.add_cascade(label="File", menu=file_menu, underline=0)

# #Edit Menu
# edit_menu = Menu(menubar, tearoff=0, bg="white", fg="black")
# edit_menu.add_command(label="Cut", command=do_something, accelerator="Ctrl+X")
# edit_menu.add_command(label="Copy", command=do_something, accelerator="Ctrl+C")
# edit_menu.add_command(label="Paste", command=do_something, accelerator="Ctrl+V")
# menubar.add_cascade(label="Edit", menu=edit_menu, underline=0)


# #Effects Menu
# edit_menu = Menu(menubar, tearoff=0, bg="white", fg="black")
# edit_menu.add_command(label="Cut", command=do_something, accelerator="Ctrl+X")
# edit_menu.add_command(label="Copy", command=do_something, accelerator="Ctrl+C")
# edit_menu.add_command(label="Paste", command=do_something, accelerator="Ctrl+V")
# menubar.add_cascade(label="Effects", menu=edit_menu, underline=0)


# #Help Menu
# edit_menu = Menu(menubar, tearoff=0, bg="white", fg="black")
# edit_menu.add_command(label="Cut", command=do_something, accelerator="Ctrl+X")
# edit_menu.add_command(label="Copy", command=do_something, accelerator="Ctrl+C")
# edit_menu.add_command(label="Paste", command=do_something, accelerator="Ctrl+V")
# menubar.add_cascade(label="Help", menu=edit_menu, underline=0)

# #Help Menu
# edit_menu = Menu(menubar, tearoff=0, bg="white", fg="black")
# edit_menu.add_command(label="Cut", command=do_something, accelerator="Ctrl+X")
# edit_menu.add_command(label="Copy", command=do_something, accelerator="Ctrl+C")
# edit_menu.add_command(label="Paste", command=do_something, accelerator="Ctrl+V")
# menubar.add_cascade(label="License", menu=edit_menu, underline=0)

# #Help Menu
# edit_menu = Menu(menubar, tearoff=0, bg="white", fg="black")
# edit_menu.add_command(label="Cut", command=do_something, accelerator="Ctrl+X")
# edit_menu.add_command(label="Copy", command=do_something, accelerator="Ctrl+C")
# edit_menu.add_command(label="Paste", command=do_something, accelerator="Ctrl+V")
# menubar.add_cascade(label="About", menu=edit_menu, underline=0)


# # Set underline shortcuts
# root.option_add('*tearOff', False)
# root.bind_all("<Control-n>", lambda event: do_something())
# root.bind_all("<Control-o>", lambda event: do_something())
# root.bind_all("<Control-s>", lambda event: do_something())
# root.bind_all("<Control-x>", lambda event: do_something())
# root.bind_all("<Control-c>", lambda event: do_something())
# root.bind_all("<Control-v>", lambda event: do_something())

# # def open_file_menu(event=None):
# #     menubar.activate(1)  # Activate the second menu item, which is "Edit"
# #     menubar.entrycget(1, "menu").post(0, 0)  # Open the menu
# #     # edit_menu.activate(2)  # Activate the first menu item, which is "File"
# #     # menubar.entrycget(0, "menu").post(0,0)  # Open the menu

# # # Bind the keyboard shortcut (Alt + F) to open the file menu
# # root.bind_all("<Alt-F>", open_file_menu)


# def open_file_menu(event=None):
#     menubar.activate(0)  # Activate the first menu item, which is "File"
#     menubar.entrycget(0, "menu").post(0, 0)  # Open the menu

# # def open_edit_menu(event=None):
# #     menubar.activate(1)  # Activate the second menu item, which is "Edit"
# #     menubar.entrycget(1, "menu").post(0, 0)  # Open the menu

# #     file_submenu.activate(0)  # Activate the first submenu item
# #     file_submenu.entrycget(0, "menu").post(0, 0)  # Open the submenu


# root.bind_all("<Alt-F>", open_file_menu)  # Bind Alt + F to open File menu
# # root.bind_all("<Alt-E>", open_edit_menu)  # Bind Alt + E to open Edit menu


# # Display the menu bar
# root.config(menu=menubar)

# root.mainloop()








# from tkinter import *

# def do_something(opt=None):
#     print("Menu item clicked",opt)

# root = Tk()

# def create_submenu(menu, submenu_name, options):
#     submenu = Menu(menu, tearoff=0)
#     for option in options:
#         submenu.add_command(label=option, command=lambda opt=option: do_something(opt))
#     menu.add_cascade(label=" " + submenu_name, menu=submenu)

# # Create a menu bar
# menubar = Menu(root, bg="white", fg="black")

# # Create a file menu
# file_menu = Menu(menubar, tearoff=0, bg="white", fg="black")
# file_menu.add_command(label="New", command=do_something, accelerator="Ctrl+N", underline=0)
# # file_menu.add_command(label="Open", command=do_something, accelerator="Ctrl+O", underline=0)
# submenu = Menu(file_menu, tearoff=0)
# submenu.add_command(label="Image", command=do_something, accelerator="Ctrl+O+I", underline=0)
# submenu.add_command(label="Folder", command=do_something, accelerator="Ctrl+O+F", underline=0)
# submenu.add_separator()
# submenu.add_command(label="Video", command=do_something, accelerator="Ctrl+O+V", underline=0)
# # file_menu.add_cascade(label="Open", menu=submenu)
# file_menu.add_cascade(label="Open", command=do_something, accelerator="Ctrl+O", underline=0 , menu=submenu)
# # create_submenu(file_menu, "Options 1", ["Image", "Image Folder", "Video"])
# file_menu.add_command(label="Save", command=do_something, accelerator="Ctrl+S", underline=0)
# file_menu.add_separator()
# file_menu.add_command(label="Exit", command=root.quit, underline=1)  # Underline "E" in "Exit"
# menubar.add_cascade(label="File", menu=file_menu)

# # Create an edit menu
# edit_menu = Menu(menubar, tearoff=0, bg="white", fg="black")
# edit_menu.add_command(label="Cut", command=do_something, accelerator="Ctrl+X", underline=0)
# edit_menu.add_command(label="Copy", command=do_something, accelerator="Ctrl+C", underline=0)
# edit_menu.add_command(label="Paste", command=do_something, accelerator="Ctrl+V", underline=0)
# menubar.add_cascade(label="Edit", menu=edit_menu)

# # Set underline shortcuts
# root.option_add('*tearOff', False)
# root.bind_all("<Control-n>", lambda event: do_something())
# root.bind_all("<Control-o>", lambda event: do_something())
# root.bind_all("<Control-s>", lambda event: do_something())
# root.bind_all("<Control-x>", lambda event: do_something())
# root.bind_all("<Control-c>", lambda event: do_something())
# root.bind_all("<Control-v>", lambda event: do_something())

# # Display the menu bar
# root.config(menu=menubar)

# root.mainloop()

# #todo

# import tkinter as tk

# def open_file_menu(event=None):
#     menubar.activate(0)  # Activate the first menu item, which is "File"
#     menubar.entrycget(0, "menu").post(0, 0)  # Open the menu

# root = tk.Tk()

# # Create a menu bar
# menubar = tk.Menu(root)

# # Create a file menu
# file_menu = tk.Menu(menubar, tearoff=0)
# file_menu.add_command(label="New")
# file_menu.add_command(label="Open")
# file_menu.add_command(label="Save")
# file_menu.add_separator()
# file_menu.add_command(label="Exit", command=root.quit)
# menubar.add_cascade(label="File", menu=file_menu)

# # Display the menu bar
# root.config(menu=menubar)


# root.mainloop()


# # todo 
# Bind the keyboard shortcut (Alt + F) to open the file menu
# root.bind_all("<Alt-F>", open_file_menu)





#todo canvas workable
# import tkinter as tk
# from tkinter import ttk

# class ZoomableCanvas(tk.Canvas):
#     def __init__(self, master, diameter, *args, **kwargs):
#         super().__init__(master, *args, **kwargs)
#         self.diameter = diameter
#         self.scale_factor = 1.0
#         self.bind_events()
#         self.draw_grid()
#         self.draw_center_lines()

#     def bind_events(self):
#         self.bind("<MouseWheel>", self.zoom)
#         self.bind("<Button-2>", self.pan_start)
#         self.bind("<B2-Motion>", self.pan_move)
    
#     def draw_grid(self):
#         for i in range(0, self.diameter + 1, 10):
#             self.create_line(i, 0, i, self.diameter, fill="gray")
#             self.create_line(0, i, self.diameter, i, fill="gray")

#     def draw_center_lines(self):
#         self.create_line(0, self.diameter // 2, self.diameter, self.diameter // 2, fill="black", width=2)
#         self.create_line(self.diameter // 2, 0, self.diameter // 2, self.diameter, fill="black", width=2)

#     def zoom(self, event):
        
#         if event.delta > 0:   
#             if self.scale_factor < 1 : self.scale_factor = 1         
#             self.scale_factor *= 1.001
#             print('[1]',event.delta, self.scale_factor)
#         else:
#             if self.scale_factor > 1 : self.scale_factor = 1
#             self.scale_factor /= 1.001
#             print('[2]',event.delta, self.scale_factor)

#         # Apply zoom restrictions
#         if self.scale_factor < 0.5:
#             self.scale_factor = 0.5
#         elif self.scale_factor > 5.0:
#             self.scale_factor = 5.0

#         self.scale("all", 0, 0, self.scale_factor, self.scale_factor)

#     def pan_start(self, event):
#         self.scan_mark(event.x, event.y)

#     def pan_move(self, event):
#         self.scan_dragto(event.x, event.y, gain=1)

#     def go_to_center(self):
#         self.xview_moveto(0.5)
#         self.yview_moveto(0.5)

#     def zoom_100(self):
#         self.scale_factor = 1.0
#         self.scale("all", 0, 0, 1, 1)

# def main():
#     diameter = int(input("Enter the diameter of the canvas: "))

#     root = tk.Tk()
#     root.title("Zoomable Canvas")

#     canvas = ZoomableCanvas(root, diameter, width=diameter, height=diameter, bg="white")
#     canvas.pack(fill="both", expand=True)

#     root.bind("<Control-c>", lambda event: canvas.go_to_center())
#     root.bind("<Control-0>", lambda event: canvas.zoom_100())

#     root.mainloop()

# if __name__ == "__main__":
#     main()



# # # todo canvas 2 perfevct
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


#     def load_image():
#         image = Image.open("sam.png")  # Change "your_image.jpg" to the path of your image
#         width, height = image.size

#         # Resize the image to fit within the canvas
#         if width > 500 or height > 500:
#             ratio = min(500 / width, 500 / height)
#             width = int(width * ratio)
#             height = int(height * ratio)
#             image = image.resize((width, height), Image.LANCZOS)

#         canvas.orig_img = ImageTk.PhotoImage(image)
#         canvas.image_ref = canvas.create_image(
#             0, 0, image=canvas.orig_img, anchor="nw"
#         )
#         # canvas.scale_image_ref(width / 2, height / 2)

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


#         #test
#         canvas.image_ref = canvas.create_image(0, 0, image=canvas.orig_img, anchor="nw")


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

#     canvas.bind("<MouseWheel>", zoom)
#     canvas.bind("<Button-2>", pan_start)
#     canvas.bind("<B2-Motion>", pan_move)

#     draw_grid()
#     draw_center_lines()
#     # load_image()


#     master.bind("<Control-c>", lambda event: go_to_center(event))
#     master.bind("<Control-f>", lambda event: zoom_100(event))

#     global origin_GLOBAL
#     origin_GLOBAL = canvas.xview()[0], canvas.yview()[0]

#     return canvas




















# def main():
#     diameter = 500

#     root = tk.Tk()
#     root.title("Zoomable Canvas")

#     canvas = create_zoomable_canvas(root, diameter, width=diameter, height=diameter, bg="white")
#     canvas.pack(fill="both", expand=True)



#     def load_image():
#         image = Image.open("sam.png")  # Change "your_image.jpg" to the path of your image
#         width, height = image.size

#         # Resize the image to fit within the canvas
#         if width > 500 or height > 500:
#             ratio = min(500 / width, 500 / height)
#             width = int(width * ratio)
#             height = int(height * ratio)
#             image = image.resize((width, height), Image.LANCZOS)

#         canvas.orig_img = ImageTk.PhotoImage(image)
#         canvas.image_ref = canvas.create_image(
#             0, 0, image=canvas.orig_img, anchor="nw"
#         )
#         # canvas.scale_image_ref(width / 2, height / 2)


#     load_image()

#     def fun():
#         canvas.scale_factor = 1
#         canvas.scale("all", 0, 0, 2, 2)

#     a = tk.Button(root, text='center', command=fun)
#     a.pack()

#     root.mainloop()

# if __name__ == "__main__":
#     main()



# # #todo best workabele test 

# import tkinter as tk
# import tkinter.ttk as ttk


# class GriddedMazeCanvas(tk.Canvas):

#     def almost_centered(self, cols, rows):

#         width = int(self['width'])
#         height = int(self['height'])
#         cell_dim = self.settings['cell_dim']
#         rows = rows % height
#         cols = cols % width

#         w = cols * cell_dim
#         h = rows * cell_dim

#         if self.zoom < 0:
#             raise ValueError('zoom is negative:', self.zoom)

#         zoom = self.zoom // 2 + 1
#         if self.drawn() and 1 != zoom:
#             w *= zoom
#             h *= zoom

#         h_shift = (width - w) // 2
#         v_shift = (height - h) // 2

#         return [h_shift, v_shift,
#                 h_shift + w, v_shift + h]

#     def __init__(self, *args, **kwargs):
#         if 'settings' not in kwargs:
#             raise ValueError("'settings' not passed.")
#         settings = kwargs['settings']
#         del kwargs['settings']

#         super().__init__(*args, **kwargs)

#         self.config(highlightthickness=0)

#         self.settings = settings
#         self.bind_events()

#     def draw_maze(self, cols, rows):

#         self.cols = cols
#         self.rows = rows

#         if self.not_drawn():
#             self.cells = {}
#             self.cell_dim = self.settings['cell_dim']
#             self.border_thickness = self.settings['border_thickness']
#             self.zoom = 0

#         self.delete(tk.ALL)

#         maze, coords = self._draw_maze(cols, rows, fix=False)
#         lines = self._draw_grid(coords)

#         return maze, lines

#     def _draw_maze(self, cols, rows, fix=True):
#         data = self.settings

#         to_max = data['to_max']
#         border_thickness = data['border_thickness']
#         poligon_color = data['poligon_color']
#         poligon_border_color = data['poligon_border_color']

#         coords = self.almost_centered(cols, rows)

#         if fix:
#             # Fix for the disappearing NW borders
#             if to_max == cols:
#                 coords[0] += 1
#             if to_max == rows:
#                 coords[1] += 1

#         maze = self.create_rectangle(*coords,
#                                      fill=poligon_color,
#                                      outline=poligon_border_color,
#                                      width=border_thickness,
#                                      tag='maze')
#         return maze, coords

#     def _draw_grid(self, coords):
#         data = self.settings
#         poligon_border_color = data['poligon_border_color']
#         cell_dim = data['cell_dim']

#         if coords is None:
#             if self.not_drawn():
#                 raise ValueError('The maze is still uninitialized.')
#             x1, y1, x2, y2 = self.almost_centered(self.cols, self.rows)
#         else:
#             x1, y1, x2, y2 = coords

#         if self.drawn() and 0 != self.zoom:
#             if self.zoom < 0:
#                 self.zoom = 0
#                 print('no zooming at negative values.')
#             else:
#                 zoom = self.zoom // 2 + 1
#                 cell_dim *= zoom

#         lines = []

#         for i, x in enumerate(range(x1, x2, cell_dim)):
#             line = self.create_line(x, y1, x, y2,
#                                     fill=poligon_border_color,
#                                     tags=('grid', 'grid_hl_{}'.format(i)))
#             lines.append(line)

#         for i, y in enumerate(range(y1, y2, cell_dim)):
#             line = self.create_line(x1, y, x2, y,
#                                     fill=poligon_border_color,
#                                     tags=('grid', 'grid_vl_{}'.format(i)))
#             lines.append(line)

#         return lines

#     def drawn(self):
#         return hasattr(self, 'cells')

#     def not_drawn(self):
#         return not self.drawn()

#     def bind_events(self):
#         self.bind("<MouseWheel>", self.onZoomInOut)  # For mouse wheel scrolling
#         # self.bind('<Button-4>', self.onZoomIn)
#         # self.bind('<Button-5>', self.onZoomOut)

#         self.bind('<ButtonPress-1>', self.onScrollStart)
#         self.bind('<B1-Motion>', self.onScrollMove)
#         self.tag_bind('maze', '<ButtonPress-3>', self.onMouseRight)

    


#     def onScrollStart(self, event):
#         print(event.x, event.y, self.canvasx(event.x), self.canvasy(event.y))
#         self.scan_mark(event.x, event.y)

#     def onMouseRight(self, event):
#         col, row = self.get_pos(event)
#         print('zoom, col, row:', self.zoom, col, row)

#     def onScrollMove(self, event):
#         delta = event.x, event.y
#         self.scan_dragto(*delta, gain=1)


#     def onZoomInOut(self,event):
#         if event.delta > 0:
#             self.onZoomIn(event)
#             print("In" , end = '\t')
#         else:
#             self.onZoomOut(event)
#             print("Out" , end = '\t')



#     def onZoomIn(self, event):
#         if self.not_drawn():
#             return

#         max_zoom = 16

#         self.zoom += 1
#         if self.zoom > max_zoom:
#             print("Can't go beyond", max_zoom)
#             self.zoom = max_zoom
#             return

#         print('Zooming in.', event.num, event.x, event.y, self.zoom)
#         self.draw_maze(self.cols, self.rows)

#     def onZoomOut(self, event):
#         if self.not_drawn():
#             return

#         self.zoom -= 1
#         if self.zoom < 0:
#             print("Can't go below zero.")
#             self.zoom = 0
#             return

#         print('Zooming out.', event.num, event.x, event.y, self.zoom)
#         self.draw_maze(self.cols, self.rows)

#     def get_pos(self, event):
#         x, y = event.x, event.y
#         cols, rows = self.cols, self.rows
#         cell_dim, zoom = self.cell_dim, self.zoom
#         x1, y1, x2, y2 = self.almost_centered(cols, rows)

#         if not (x1 <= x <= x2 and y1 <= y <= y2):
#             print('Here we are out of bounds.')
#             return None, None

#         scale = (zoom // 2 + 1) * cell_dim

#         col = (x - x1) // scale
#         row = (y - y1) // scale

#         return col, row


# # class CanvasButton(ttk.Button):

# #     def freeze_origin(self):
# #         if not hasattr(self, 'origin'):
# #             canvas = self.canvas
# #             self.origin = canvas.xview()[0], canvas.yview()[0]

# #     def reset(self):
# #         print('---')
# #         canvas = self.canvas
# #         x, y = self.origin
# #         canvas.yview_moveto(x)
# #         canvas.xview_moveto(y)

# #     def __init__(self, *args, **kwargs):
# #         if not 'canvas' in kwargs:
# #             raise ValueError("'canvas' not passed.")
# #         canvas = kwargs['canvas']
# #         del kwargs['canvas']

# #         super().__init__(*args, **kwargs)
# #         self.config(command=self.reset)

# #         self.canvas = canvas


# root = tk.Tk()

# settings = {'cell_dim': 3,
#             'to_max': 200,
#             'border_thickness': 1,
#             'poligon_color': '#F7F37E',
#             'poligon_border_color': '#AC5D33'}

# frame = ttk.Frame(root)
# canvas = GriddedMazeCanvas(frame,
#                            settings=settings,
#                            width=640,
#                            height=480)
# # button = CanvasButton(frame, text='Reset', canvas=canvas)
# # button.freeze_origin()

# canvas.draw_maze(20, 10)

# canvas.grid(row=0, column=0, sticky=tk.NSEW)
# # button.grid(row=1, column=0, sticky=tk.EW)
# frame.rowconfigure(0, weight=1)
# frame.grid()

# root.mainloop()





#todo modified

import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk

# global XX
# XX = 1.0
background_image = ImageTk.PhotoImage(Image.open(f"sam.png"))
# XX_W, XX_H = background_image.size


def almost_centered(canvas, cols, rows):
    width = int(canvas['width'])
    height = int(canvas['height'])
    cell_dim = canvas.settings['cell_dim']
    rows = rows % height
    cols = cols % width

    w = cols * cell_dim
    h = rows * cell_dim

    if canvas.zoom < 0:
        raise ValueError('zoom is negative:', canvas.zoom)

    zoom = canvas.zoom // 2 + 1
    if canvas.drawn() and 1 != zoom:
        w *= zoom
        h *= zoom

    h_shift = (width - w) // 2
    v_shift = (height - h) // 2

    return [h_shift, v_shift, h_shift + w, v_shift + h]

def draw_maze(canvas, cols, rows):
    canvas.cols = cols
    canvas.rows = rows

    if canvas.not_drawn():
        canvas.cells = {}
        canvas.cell_dim = canvas.settings['cell_dim']
        canvas.border_thickness = canvas.settings['border_thickness']
        canvas.zoom = 0

    canvas.delete(tk.ALL)

    maze, coords = _draw_maze(canvas, cols, rows, fix=False)
    lines = _draw_grid(canvas, coords)

    return maze, lines

def _draw_maze(canvas, cols, rows, fix=True):
    data = canvas.settings

    to_max = data['to_max']
    border_thickness = data['border_thickness']
    poligon_color = data['poligon_color']
    poligon_border_color = data['poligon_border_color']

    coords = almost_centered(canvas, cols, rows)

    if fix:
        # Fix for the disappearing NW borders
        if to_max == cols:
            coords[0] += 1
        if to_max == rows:
            coords[1] += 1

    maze = canvas.create_rectangle(*coords,
                                   fill=poligon_color,
                                   outline=poligon_border_color,
                                   width=border_thickness,
                                   tag='maze')
    return maze, coords

def _draw_grid(canvas, coords):
    data = canvas.settings
    poligon_border_color = data['poligon_border_color']
    cell_dim = data['cell_dim']

    if coords is None:
        if canvas.not_drawn():
            raise ValueError('The maze is still uninitialized.')
        x1, y1, x2, y2 = almost_centered(canvas, canvas.cols, canvas.rows)
    else:
        x1, y1, x2, y2 = coords

    if canvas.drawn() and 0 != canvas.zoom:
        if canvas.zoom < 0:
            canvas.zoom = 0
            print('no zooming at negative values.')
        else:
            zoom = canvas.zoom // 2 + 1
            cell_dim *= zoom

    lines = []

    for i, x in enumerate(range(x1, x2, cell_dim)):
        line = canvas.create_line(x, y1, x, y2,
                                  fill=poligon_border_color,
                                  tags=('grid', 'grid_hl_{}'.format(i)))
        lines.append(line)

    for i, y in enumerate(range(y1, y2, cell_dim)):
        line = canvas.create_line(x1, y, x2, y,
                                  fill=poligon_border_color,
                                  tags=('grid', 'grid_vl_{}'.format(i)))
        lines.append(line)

    return lines

def drawn(canvas):
    return hasattr(canvas, 'cells')

def not_drawn(canvas):
    return not drawn(canvas)

def bind_events(canvas):
    canvas.bind("<MouseWheel>", lambda event: onZoomInOut(event, canvas))  # For mouse wheel scrolling
    canvas.bind('<ButtonPress-1>', lambda event: onScrollStart(event, canvas))
    canvas.tag_bind('maze', '<ButtonPress-3>', lambda event: onMouseRight(event, canvas))

def onScrollStart(event, canvas):
    print(event.x, event.y, canvas.canvasx(event.x), canvas.canvasy(event.y))
    canvas.scan_mark(event.x, event.y)

def onMouseRight(event, canvas):
    col, row = get_pos(event, canvas)
    print('zoom, col, row:', canvas.zoom, col, row)

def onZoomInOut(event, canvas):
    if event.delta > 0:
        # onZoomIn(event, canvas)
        canvas.create_image(0, 0, anchor='nw', image=background_image)
        canvas.image = background_image
        print("In", end='\t')
    else:
        # onZoomOut(event, canvas)
        canvas.create_image(0, -22, anchor='nw', image=background_image)
        canvas.image = background_image
        print("Out", end='\t')

def onZoomIn(event, canvas):
    if not_drawn(canvas):
        return

    max_zoom = 16

    canvas.zoom += 1
    if canvas.zoom > max_zoom:
        print("Can't go beyond", max_zoom)
        canvas.zoom = max_zoom
        return

    print('Zooming in.', event.num, event.x, event.y, canvas.zoom)
    draw_maze(canvas, canvas.cols, canvas.rows)

def onZoomOut(event, canvas):
    if not_drawn(canvas):
        return

    canvas.zoom -= 1
    if canvas.zoom < 0:
        print("Can't go below zero.")
        canvas.zoom = 0
        return

    print('Zooming out.', event.num, event.x, event.y, canvas.zoom)
    draw_maze(canvas, canvas.cols, canvas.rows)

def get_pos(event, canvas):
    x, y = event.x, event.y
    cols, rows = canvas.cols, canvas.rows
    cell_dim, zoom = canvas.cell_dim, canvas.zoom
    x1, y1, x2, y2 = almost_centered(canvas, cols, rows)

    if not (x1 <= x <= x2 and y1 <= y <= y2):
        print('Here we are out of bounds.')
        return None, None

    scale = (zoom // 2 + 1) * cell_dim

    col = (x - x1) // scale
    row = (y - y1) // scale

    return col, row

root = tk.Tk()

settings = {'cell_dim': 3,
            'to_max': 200,
            'border_thickness': 1,
            'poligon_color': '#F7F37E',
            'poligon_border_color': '#AC5D33'}

frame = ttk.Frame(root)
canvas = tk.Canvas(frame, width=640, height=480 , background='gray')
canvas.settings = settings
bind_events(canvas)

canvas.draw_maze = lambda cols, rows: draw_maze(canvas, cols, rows)
canvas.almost_centered = lambda cols, rows: almost_centered(canvas, cols, rows)
canvas.not_drawn = lambda: not_drawn(canvas)
canvas.drawn = lambda: drawn(canvas)
canvas.get_pos = lambda event: get_pos(event, canvas)
# canvas.zoom = 0

canvas.draw_maze(20, 10)

canvas.grid(row=0, column=0, sticky=tk.NSEW)
frame.rowconfigure(0, weight=1)
frame.grid()

canvas.zoom = 16
# canvas.update_idletasks()
# root.update_idletasks()

background_image = ImageTk.PhotoImage(Image.open(f"sam.png"))
canvas.create_image(0, -22, anchor='nw', image=background_image)
canvas.image = background_image


root.mainloop()
