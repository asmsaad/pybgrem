from tkinter import *
from tkinter import ttk

def change_text():
    menubar.entryconfigure(0, label="New Label")

root = Tk()

menubar = Menu(root)
menu = Menu(menubar, tearoff=0)
menu.add_command(label="Original Label", command=change_text)
menubar.add_cascade(label="Menu", menu=menu)

# Adding another menu item directly to the menubar
menubar.add_command(label="Another Menu Item")

root.config(menu=menubar)


menubar = Menu(root)
menu = Menu(menubar, tearoff=0)

menu.add_command(label="one", command=change_text)
menubar.add_cascade(label="two", menu=menu)

# Adding another menu item directly to the menubar
menubar.add_command(label="Five")


root.config(menu=menubar)




root.mainloop()







#todo scroll 001
# import tkinter as tk
# from tkinter import scrolledtext
# from tkinter import messagebox

# def on_scroll(e):
    
#     # Get the current position of the scrollbar
#     scroll_position = text_widget.yview()[1]
#     print(scroll_position)

#     # If scrollbar is at the bottom (scroll_position == 1), show popup warning
#     if scroll_position == 1:
#         messagebox.showwarning("Warning", "You are at the end of the text!")

# root = Tk()
# root.title("Scrollable Text with Popup Warning")

# text_widget = scrolledtext.ScrolledText(root, wrap=tk.WORD)
# text_widget.pack(expand=True, fill=tk.BOTH)
# text_widget.insert(tk.INSERT, aggrements)

# # Bind the scrollbar's movement to the on_scroll function


# root.mainloop()







# import tkinter as tk
# import winsound

# def open_warning_window():
#     # Create top-level window
#     warning_window = tk.Toplevel(root)
#     warning_window.title("Warning!")
#     warning_window.geometry("300x100")
#     warning_window.resizable(False, False)
    
#     # Display warning message
#     warning_label = tk.Label(warning_window, text="Warning: Top-level window is open!", font=("Helvetica", 12))
#     warning_label.pack(pady=10)
    
#     # Play warning sound
#     winsound.Beep(1000, 500)  # Adjust frequency and duration as needed

#     # Grab focus to the top-level window (prevent interaction with the base window)
#     warning_window.grab_set()

#     # Release focus from the top-level window when it's closed
#     # warning_window.protocol("WM_DELETE_WINDOW", lambda: release_focus(warning_window))

# def release_focus(window):
#     # Release focus from the top-level window
#     window.grab_release()

# # Create main window
# root = tk.Tk()
# root.title("Base Window")

# # Create button to open top-level window
# warning_button = tk.Button(root, text="Open Warning Window", command=open_warning_window)
# warning_button.pack(pady=20)

# root.mainloop()




    # #todo 
    # [1] make background color picker after removing bg

    # [1] add image as background

    # [1]iamge brigtness / contrast / zoom in zoom out / pan / move /filters / crops/ undo redo/

    # [4] remember last opend folder

    # [5] Should allow to save with different size at save time, by percentage %, by Hight & Width or by pixel
    
    # [6] When saved, the original will be there and new folder will be automatically created for the processed images.
    
    # [7] Software name and logo
    # -> Name and logo will be thge where?
    
    # [8] License control to allow trial

    # [9] version, or set time frame (exp, 1year, 2 years etc.), or no time limit. Also to be able to add logo or name to the license (I have an example of this with codes)
    # -> for now  add the licence key other wise 3 days trailes periosd 

    # [10] License agreement document (I will provide this document). I should be able to change this at any time so in-case of correction or modification the  software does not need to be recompile.
    # -> Showing everytime when started the app




# def convert_to_time_format(milliseconds):
#     # Calculate time components
#     milliseconds_  = milliseconds%1000
#     seconds = int((milliseconds / 1000) % 60)
#     minutes = int((milliseconds / (1000 * 60)) % 60)
#     hours = int((milliseconds / (1000 * 60 * 60)) % 24)
#     days = int(milliseconds / (1000 * 60 * 60 * 24))

#     # Format the time components
#     time_components = {}
#     # if days > 0:
#     time_components['days'] = "{:02d}d".format(days)
#     # if hours > 0:
#     time_components['hours'] = "{:02d}h".format(hours)
#     # if minutes > 0:
#     time_components['minutes'] = "{:02d}m".format(minutes)
#     # if seconds > 0:
#     time_components['seconds'] = "{:02d}s".format(seconds)
#     # if milliseconds > 0:
#     time_components['milliseconds'] = "{:03d}m".format(milliseconds_)


#     if time_components['hours'][:2] == '00' and time_components['days'][:2]  == '00':
#         del time_components['hours']
#         del time_components['days']
#     elif time_components['hours'][:2]  != '00' and time_components['days'][:2]  == '00':
#         del time_components['days']



    
#     # Join and return the formatted time
#     formatted_time = ' : '.join([str(time_components[each_time_param]) for each_time_param in time_components])
#     return formatted_time

# # Example usage
# milliseconds = 1000 * 60 * 60  +1  # Replace with your milliseconds
# formatted_time = convert_to_time_format(milliseconds)
# print("Formatted Time:", formatted_time)




# import os
# from PIL import Image, ImageDraw, ImageFont







# class CenterAlignTextImage:
#     def __init__(self,text,fontsize=13*10,font_loc=os.path.abspath("app/res/font/roboto/Roboto-Light.ttf"),fg='black',bg='orange' , dim = (60*10, 28*10 )):
#         self.bg = bg
#         self.dim  = dim 

#         img_circle = self.base_image()
#         img_number = self.get_number_img(text,fg=fg,fontsize=fontsize,font_loc=font_loc)
#         self.overlay_images(img_circle, img_number)

#     #todo making circle image
#     def base_image(self):
#         width, height = self.dim  # Adjust according to your needs
#         image = Image.new("RGBA", (width, height) , None if self.bg == None else self.bg)
#         return image

#     #todo making nuber image
#     def get_number_img(self,text,fg='white',fontsize=130,font_loc=''):
#         canvas = Image.new('RGBA', (1000,1000))
#         draw = ImageDraw.Draw(canvas)
#         font = ImageFont.truetype(font_loc,fontsize)
#         draw.text((0, 0), text, font=font, fill=fg)
#         bbox = canvas.getbbox()
#         cropped_image = canvas.crop(bbox)
#         # cropped_image.show()
#         return cropped_image

#     def center_secondary_rectangle(self,base_width, base_height, secondary_width, secondary_height):
#         base_center_x = base_width // 2
#         base_center_y = base_height // 2
#         secondary_x = base_center_x - (secondary_width // 2)
#         secondary_y = base_center_y - (secondary_height // 2)
#         return (secondary_x, secondary_y)

#     def overlay_images(self,base_image, overlay_image):
#         self.result_image = base_image.copy()
#         self.result_image.paste(overlay_image, self.center_secondary_rectangle(base_image.size[0], base_image.size[1], overlay_image.size[0], overlay_image.size[1],), overlay_image)
#         return self.result_image
    
#     def get_img(self):
#         return self.result_image


# CenterAlignTextImage('Original').get_img().resize((60, 28), Image.LANCZOS).rotate(90, expand=True).show()
# CenterAlignTextImage('Modified').get_img().resize((60, 28), Image.LANCZOS).show()


# #todo pdf 

# import tkinter as tk
# from tkinter import filedialog, messagebox
# from pdf2image import convert_from_path

# class PDFViewer:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("PDF Viewer")
        
#         self.canvas = tk.Canvas(self.master)
#         self.canvas.pack(fill=tk.BOTH, expand=True)

#         self.load_button = tk.Button(self.master, text="Open PDF", command=self.open_pdf)
#         self.load_button.pack()

#     def open_pdf(self):
#         file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
#         if file_path:
#             try:
#                 images = convert_from_path(file_path)
#                 for image in images:
#                     self.display_image(image)
#             except Exception as e:
#                 messagebox.showerror("Error", f"An error occurred: {e}")

#     def display_image(self, image):
#         photo = tk.PhotoImage(master=self.canvas, image=image)
#         self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
#         self.canvas.image = photo

# # Create the main window
# root = tk.Tk()
# app = PDFViewer(root)
# root.mainloop()






# import numpy as np

# def generate_exponential_list(start_range, end_range, point_number):
#     # Calculate the base for the exponential growth
#     base = (end_range / start_range) ** (1 / (point_number - 1))
    
#     # Generate the list of exponentially increasing values
#     exponential_list = [int(start_range * (base ** i)) for i in range(point_number)]
    
#     return exponential_list

# # Example usage:
# start_range = 80
# end_range = 250
# point_number = 10

# exponential_values = generate_exponential_list(start_range, end_range, point_number)
# # print("Exponential values:", exponential_values)

