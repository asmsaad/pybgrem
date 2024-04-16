# import tkinter as tk
# from tkinter import scrolledtext


# aggrements='''
# SOFTWARE LICENSE AGREEMENT

# This Software License Agreement ("Agreement") is entered into by and between [Your Company Name], a company organized and existing under the laws of [Your Country/State], with its principal place of business at [Your Address] ("Licensor"), and the user of the software ("Licensee").

# 1. LICENSE GRANT

# Subject to the terms and conditions of this Agreement, Licensor hereby grants Licensee a [non-exclusive, non-transferable, revocable] license to use the software ("Software") provided by Licensor, including any updates and modifications, solely for Licensee's internal business purposes.

# 2. RESTRICTIONS

# Licensee shall not:
# - Modify, adapt, or create derivative works of the Software.
# - Reverse engineer, decompile, or disassemble the Software.
# - Remove or alter any copyright, trademark, or other proprietary notices from the Software.
# - Rent, lease, sublicense, or otherwise transfer the Software to any third party.

# 3. OWNERSHIP

# Licensor retains all right, title, and interest in and to the Software, including all intellectual property rights therein. This Agreement does not grant Licensee any ownership rights in the Software.

# 4. SUPPORT AND MAINTENANCE

# Licensor may, at its sole discretion, provide support and maintenance services for the Software. Licensee acknowledges that any such services are provided on an "as-is" basis, and Licensor makes no warranties or representations regarding the availability or quality of such services.

# 5. DISCLAIMER OF WARRANTIES

# THE SOFTWARE IS PROVIDED "AS IS," WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT. IN NO EVENT SHALL LICENSOR BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT, OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# 6. TERMINATION

# This Agreement shall remain in effect until terminated by either party. Licensor may terminate this Agreement immediately upon written notice if Licensee breaches any term or condition of this Agreement. Upon termination, Licensee shall cease all use of the Software and destroy all copies thereof.

# 7. MISCELLANEOUS

# This Agreement constitutes the entire agreement between the parties concerning the subject matter hereof and supersedes all prior agreements and understandings, whether written or oral, relating to such subject matter. This Agreement may be amended only by a written instrument signed by both parties. This Agreement shall be governed by and construed in accordance with the laws of [Your Jurisdiction]. Any dispute arising under or in connection with this Agreement shall be subject to the exclusive jurisdiction of the courts located in [Your Jurisdiction].

# IN WITNESS WHEREOF, the parties hereto have executed this Agreement as of the Effective Date.

# [Your Company Name]

# By: _______________________
# Name: _____________________
# Title: ______________________
# Date: ______________________

# Licensee

# By: _______________________
# Name: _____________________
# Title: ______________________
# Date: ______________________

# '''
# def agree_checkbox_state():
#     if agree_checkbox_var.get():
#         agree_button.config(state=tk.NORMAL)
#     else:
#         agree_button.config(state=tk.DISABLED)

# def agree_button_click():
#     # Add your logic here for what happens when the user clicks "I Agree"
#     root.destroy()

# def check_scroll(*args):
#     # Get the current scrollbar position
#     scrollbar_position = agree_checkbox.get()[0]

#     # Get the total number of lines in the Text widget
#     total_lines = int(terms_text.index('end').split('.')[0])

#     # Calculate the current scrolled line number
#     current_line_number = int(total_lines * scrollbar_position)

#     # Print the current scrolled line number
#     print("Current scrolled line number:", current_line_number)

# # Create main window
# root = tk.Tk()
# root.title("User Agreement")

# # Create scrolled text for terms and conditions
# terms_text = scrolledtext.ScrolledText(root, width=150, height=10, wrap=tk.WORD, font=('Roboto', 10))
# terms_text.insert(tk.INSERT, aggrements)
# terms_text.grid(row=0, column=0, padx=0, pady=10, columnspan=2)

# # Create checkbox for agreeing to terms
# agree_checkbox_var = tk.BooleanVar()
# agree_checkbox = tk.Checkbutton(root, text="I agree to the terms and conditions", variable=agree_checkbox_var,
#                                  command=agree_checkbox_state)
# agree_checkbox.grid(row=1, column=0, padx=10, pady=10)

# # Create button to confirm agreement
# agree_button = tk.Button(root, text="I Agree", state=tk.DISABLED, command=agree_button_click)
# agree_button.grid(row=1, column=1, padx=10, pady=10)

# # # Add scrollbar
# # scrollbar = tk.Scrollbar(root, command=terms_text.yview)
# # scrollbar.grid(row=0, column=1, sticky='ns')
# # terms_text.config(yscrollcommand=scrollbar.set)

# # Bind check_scroll function to the <Configure> event of the ScrolledText widget
# terms_text.bind("<Configure>", check_scroll)

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




import os
from PIL import Image, ImageDraw, ImageFont







class CenterAlignTextImage:
    def __init__(self,text,fontsize=13*10,font_loc=os.path.abspath("app/res/font/roboto/Roboto-Light.ttf"),fg='black',bg='orange' , dim = (60*10, 28*10 )):
        self.bg = bg
        self.dim  = dim 

        img_circle = self.base_image()
        img_number = self.get_number_img(text,fg=fg,fontsize=fontsize,font_loc=font_loc)
        self.overlay_images(img_circle, img_number)

    #todo making circle image
    def base_image(self):
        width, height = self.dim  # Adjust according to your needs
        image = Image.new("RGBA", (width, height) , None if self.bg == None else self.bg)
        return image

    #todo making nuber image
    def get_number_img(self,text,fg='white',fontsize=130,font_loc=''):
        canvas = Image.new('RGBA', (1000,1000))
        draw = ImageDraw.Draw(canvas)
        font = ImageFont.truetype(font_loc,fontsize)
        draw.text((0, 0), text, font=font, fill=fg)
        bbox = canvas.getbbox()
        cropped_image = canvas.crop(bbox)
        # cropped_image.show()
        return cropped_image

    def center_secondary_rectangle(self,base_width, base_height, secondary_width, secondary_height):
        base_center_x = base_width // 2
        base_center_y = base_height // 2
        secondary_x = base_center_x - (secondary_width // 2)
        secondary_y = base_center_y - (secondary_height // 2)
        return (secondary_x, secondary_y)

    def overlay_images(self,base_image, overlay_image):
        self.result_image = base_image.copy()
        self.result_image.paste(overlay_image, self.center_secondary_rectangle(base_image.size[0], base_image.size[1], overlay_image.size[0], overlay_image.size[1],), overlay_image)
        return self.result_image
    
    def get_img(self):
        return self.result_image


CenterAlignTextImage('Original').get_img().resize((60, 28), Image.LANCZOS).rotate(90, expand=True).show()
CenterAlignTextImage('Modified').get_img().resize((60, 28), Image.LANCZOS).show()