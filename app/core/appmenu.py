from tkinter import *
from tkinter import filedialog
from threading import Thread



class TkMenu:
    menu_widgets = {}
    def __init__(self,window) -> None:
        self.window = window
        self.menu_row = Menu(self.window)
        self.window.config(menu=self.menu_row)
        

    def add_menu(self,menu_name,underline=0) -> None:
        self.menu_widgets[menu_name] = Menu(self.menu_row, tearoff=0, bg="white", fg="black" )
        self.menu_row.add_cascade(label=menu_name, menu=self.menu_widgets[menu_name], underline=underline)
      
    def add_member(self,menu_name,label='',sec_label='' , underline = 0 , shortcut:str = None , command = '' , shortcut_command ='', state:str ='normal' ):
        self.menu_widgets[menu_name].add_command(label=label, command=command, accelerator=sec_label, underline=underline , state=state)
        if shortcut != None and  shortcut.strip() != "":
            self.add_keyboard_shortcut(shortcut = shortcut , comment = shortcut_command)

    def add_separator(self,menu_name):
        self.menu_widgets[menu_name].add_separator()

    def add_keyboard_shortcut(self, shortcut = '' , comment = ''):
        print('executed')
        self.window.bind_all(f"<{shortcut}>", comment)








    










class AppMenu:
    def __init__(self,root) -> None:
        self.root = root

        def do_something(clicked):
            print("Menu item clicked :: " , clicked)
        def do_something_EL(e,clicked):
            print("Menu item clicked :: " , clicked)
        app_menu = TkMenu(self.root)

        menu_name = 'File'
        app_menu.add_menu(menu_name, underline=0)
        app_menu.add_member(menu_name, label='New',     sec_label='Ctrl + N', underline=0, command=lambda : do_something(menu_name+' >> '+ 'New') , shortcut='Control-n' , shortcut_command=lambda e: do_something_EL(e,menu_name+' >> '+ 'New') )
        app_menu.add_member(menu_name, label='Open',    sec_label='Ctrl + O', underline=0, command= self.browse_images , shortcut='Control-o' , shortcut_command= lambda e: self.browse_images_EL(e))
        app_menu.add_member(menu_name, label='Save',    sec_label='Ctrl + S', underline=0, command=lambda : do_something(menu_name+' >> '+ 'Open'))
        app_menu.add_member(menu_name, label='Save as',    sec_label='Ctrl + Shift + S', underline=0, command=lambda : do_something(menu_name+' >> '+ 'Open'))
        app_menu.add_separator(menu_name)
        app_menu.add_member(menu_name, label='History', sec_label='Ctrl + H', underline=0, command=lambda : do_something(menu_name+' >> '+ 'History'))
        app_menu.add_member(menu_name, label='Exit',    sec_label='Ctrl + O', underline=0, command=lambda : do_something(menu_name+' >> '+ 'Exit'))

        menu_name = 'Edit'
        app_menu.add_menu(menu_name, underline=0)
        app_menu.add_member(menu_name, label='Copy',  sec_label='Ctrl + C', underline=0, command=lambda : do_something(menu_name+' >> '+ 'Copy'))
        app_menu.add_member(menu_name, label='Cut',   sec_label='Ctrl + X', underline=0, command=lambda : do_something(menu_name+' >> '+ 'Cut'))
        app_menu.add_member(menu_name, label='Paste', sec_label='Ctrl + P', underline=0, command=lambda : do_something(menu_name+' >> '+ 'Paste'))

        menu_name = 'View'
        app_menu.add_menu(menu_name, underline=0)
        app_menu.add_member(menu_name, label='Copy',  sec_label='Ctrl + C', underline=0, command=lambda : do_something(menu_name+' >> '+ 'Copy'))
        app_menu.add_member(menu_name, label='Cut',   sec_label='Ctrl + X', underline=0, command=lambda : do_something(menu_name+' >> '+ 'Cut'))
        app_menu.add_member(menu_name, label='Paste', sec_label='Ctrl + P', underline=0, command=lambda : do_something(menu_name+' >> '+ 'Paste'))

        menu_name = 'Effect'
        app_menu.add_menu(menu_name, underline=5)
        app_menu.add_member(menu_name, label='Effect 1', sec_label='Ctrl + E + 1', underline=7, command=lambda : do_something(menu_name+' >> '+ 'Effect 1'))
        app_menu.add_member(menu_name, label='Effect 2', sec_label='Ctrl + O', underline=7, command=lambda : do_something(menu_name+' >> '+ 'Effect 2'))
        app_menu.add_member(menu_name, label='Effect 3', sec_label='Ctrl + O', underline=7, command=lambda : do_something(menu_name+' >> '+ 'Effect 3'))

        menu_name = 'Licence'
        app_menu.add_menu(menu_name, underline=5)
        app_menu.add_member(menu_name, label='Activated', sec_label='395660-01B840-10B950-24FB40-297FF0-02B350-271C05-4FCAE6', underline=7, command=lambda : do_something(menu_name+' >> '+ 'Activated') , state='disabled')
        # app_menu.add_member(menu_name, label='AZXF-JHVC6-GFDCX-IJHHG', sec_label='Ctrl + O', underline=7, command=lambda : do_something(menu_name+' >> '+ 'Trial'))
        # app_menu.add_member(menu_name, label='Add new', sec_label='Ctrl + O', underline=7, command=lambda : do_something(menu_name+' >> '+ 'Add new'))

        menu_name = 'Help'
        app_menu.add_menu(menu_name, underline=5)
        app_menu.add_member(menu_name, label='Shortcuts', sec_label='Ctrl + O', underline=7, command=lambda : do_something(menu_name+' >> '+ 'Shortcuts'))
        app_menu.add_member(menu_name, label='Documentations', sec_label='Ctrl + O', underline=7, command=lambda : do_something(menu_name+' >> '+ 'Documentations'))
        
        menu_name = 'About'
        app_menu.add_menu(menu_name, underline=5)
        app_menu.add_member(menu_name, label='Owener', sec_label='Ctrl + O', underline=7, command=lambda : do_something(menu_name+' >> '+ 'Owener'))
        app_menu.add_member(menu_name, label='Others', sec_label='Ctrl + O', underline=7, command=lambda : do_something(menu_name+' >> '+ 'Others'))




    def pass_timeline(self,timeline_fun):
        self.timeline_fun = timeline_fun
    
    def load_images_into_timeline(self):
        self.timeline_fun(self.selected_image_files)

    def browse_images_EL(self,e):
        self.browse_images()

    def browse_images(self):
        filetypes = [
            ("JPEG files", "*.jpg"),
            # ("JPEG files", "*.jepg"),
            ("PNG files", "*.png"),
            # ("Bitmap files", "*.bmp"),
            # ("GIF files", "*.gif"),
            # ("TIFF files", "*.tiff"),
            # ("WebP files", "*.webp"),
            # ("ICO files", "*.ico"),
            # ("PPM files", "*.ppm"),
            # ("SVG files", "*.svg"),
            ("All files", "*.*")
        ]
        files = filedialog.askopenfilenames(
            title="Select image files",
            filetypes=filetypes,
            initialdir = '.',
        )
        
        # Filter out non-image files
        self.selected_image_files = [file for file in files if file.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.webp', '.ico', '.ppm', '.svg'))]


        if self.selected_image_files:
            Thread(target=self.load_images_into_timeline).start()
        else:
            None







if __name__ == '__main__':
    root = Tk()
    root.mainloop()