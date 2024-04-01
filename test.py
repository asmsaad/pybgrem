import tkinter as tk

def print_menu_option(option):
    print(option)

def create_submenu(menu, submenu_name, options):
    submenu = tk.Menu(menu, tearoff=0)
    for option in options:
        submenu.add_command(label=option, command=lambda opt=option: print_menu_option(opt))
    menu.add_cascade(label=" " + submenu_name, menu=submenu)

def main():
    root = tk.Tk()
    root.title("Menubar Example")

    menubar = tk.Menu(root)

    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="Open", command=lambda: print_menu_option("New") , state="disabled")
    file_menu.add_separator()
    file_menu.add_command(label="Image", command=lambda: print_menu_option("New"))
    file_menu.add_command(label="Folder", command=lambda: print_menu_option("Open"))
    file_menu.add_command(label="Video", command=lambda: print_menu_option("Save"))
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label=" File", menu=file_menu)

    edit_menu = tk.Menu(menubar, tearoff=0)
    edit_menu.add_command(label="Cut", command=lambda: print_menu_option("Cut"))
    edit_menu.add_command(label="Copy", command=lambda: print_menu_option("Copy"))
    edit_menu.add_command(label="Paste", command=lambda: print_menu_option("Paste"))
    menubar.add_cascade(label=" Edit", menu=edit_menu)

    options_menu = tk.Menu(menubar, tearoff=0)
    create_submenu(options_menu, "Options 1", ["Option 1.1", "Option 1.2", "Option 1.3"])
    create_submenu(options_menu, "Options 2", ["Option 2.1", "Option 2.2", "Option 2.3"])
    menubar.add_cascade(label=" Options", menu=options_menu)

    root.config(menu=menubar)
    root.mainloop()

if __name__ == "__main__":
    main()
