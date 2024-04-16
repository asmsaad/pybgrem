"""
╔══════════════════════════════════════════════════════════╗
║                       window.py                          ║
╚══════════════════════════════════════════════════════════╝
┌──────────────────────────────────────────────────────────┐
│                        Author                            │
├──────┬────────────────────┬───────┬──────────────────────┤
│ Name │ A S M Saad         │ Email │ asmsaad3@gmail.com   │
├──────┼────────────────────┼───────┼──────────────────────┤
│ Date │ April 1, 2023      │ Github│ asmsaad/mintrower    │
├──────┴────────────────────┴───────┴──────────────────────┤
│                       Description                        │
├──────────────────────────────────────────────────────────┤
│                                                          │
│                                                          │
└──────────────────────────────────────────────────────────┘
"""
from tkinter import *
from typing import Union
from app.core.colors import *


class DragWindow:
    def __init__(self, window, navigation_bar):
        self.iconify_window = None
        self.window = window
        self.navigation_bar = navigation_bar
        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0

        for each_widget in self.navigation_bar.winfo_children() + [self.navigation_bar]:
            if each_widget.winfo_class() != "Button":
                # print(each_widget.winfo_class(), each_widget.winfo_name())
                each_widget.bind("<Button-1>", self.on_drag_start)
                each_widget.bind("<ButtonRelease-1>", self.on_drag_stop)
                each_widget.bind("<B1-Motion>", self.on_drag_motion)

    def on_drag_start(self, event):
        self.offset_x = event.x
        self.offset_y = event.y
        self.dragging = True

    def on_drag_stop(self, event):
        self.dragging = False

    def on_drag_motion(self, event):
        if self.dragging:
            x = self.window.winfo_x() + event.x - self.offset_x
            y = self.window.winfo_y() + event.y - self.offset_y
            self.window.geometry("+{x}+{y}".format(x=x, y=y))


class NavigationBar:
    def __init__(self, window):
        self.window = window
        self.window.bind("<Configure>", self.allocate_window_area_EL)

        self.navigation_bar = Canvas(self.window, bg=Colors__.color()["navigation bar"]["bg"], border=0, borderwidth=0, highlightthickness=0)
        self.navigation_bar.pack(anchor=W)

        self.working_area = Canvas(self.window, bg=Colors__.color()["working space"]["bg"], border=0, borderwidth=0, highlightthickness=0)
        self.working_area.pack(anchor=W)

        self.allocate_window_area()


    def allocate_window_area(self):
        window_height = self.window.winfo_height()
        window_width = self.window.winfo_width()
        self.navigation_bar.config(height=30, width=window_width)
        self.working_area.config(height=window_height - 30, width=window_width)

    def allocate_window_area_EL(self, event):
        self.allocate_window_area()


    def window_parts(self):
        return self.navigation_bar, self.working_area


class WindowConfiguration:
    def __init__(self, window) -> None:
        self.window = window
        self.window.wm_attributes("-topmost", 1)

    def geometry(self, width, height, align='center') -> None:
        self.width = width
        self.height = height
        self.previous_window_width, self.previous_window_height  = self.width , self.height

        if align == "center":
            self.center_window(width=width, height=height)

    def resizable(self, status : Union[str, bool] = 'custom', min:tuple = None , max:tuple = None):
        self.min_window_dim , self.max_window_dim  = min, max

        if status.lower() == 'custom':            
            if min != None : self.window.minsize(self.min_window_dim[0], self.min_window_dim[1])
            if max != None : self.window.maxsize(self.max_window_dim[0], self.max_window_dim[1])
        else:
            self.window.resizable(status, status)
    

    def custom_navigation_bar(self):
        self.window.overrideredirect(True)

        navigation_bar_property = NavigationBar(self.window)
        self.navigation_bar, self.working_area = navigation_bar_property.window_parts()
        return self.navigation_bar, self.working_area

    def draggable(self):
        DragWindow(self.window, self.navigation_bar)

    def center_window(self, width: int = None, height: int = None) -> None:
        if width == None: width =  self.width
        if height == None: height = self.height

        ws = self.window.winfo_screenwidth()
        hs = self.window.winfo_screenheight()
        x = (ws / 2) - (width / 2)
        y = (hs / 2) - (height / 2)
        self.window.geometry('%dx%d+%d+%d' % (width, height, x, y))

    def app_icon(self, image: object) -> None:
        self.window.iconphoto(False, image)

    def app_title(self,title: str) -> None:
        self.window.title(title)


    





class TkTopLevel:
    def __init__(self,window,dimention=()):
        self.dimention =dimention
        self.window = window

    def create(self):
        self.toplevel_window = Toplevel(self.window)
        # Set the Toplevel window always on top
        self.toplevel_window.attributes("-topmost", True)
        # self.toplevel_window.grab_set()
        # self.toplevel_window.transient(self.window)
        # self.toplevel_window.grab_set()
        self.toplevel_window.wm_attributes("-topmost", 1)
        return self.toplevel_window

    def make_center_on_root_window(self):
        width, height = self.dimention  # (150,80)
        x = y = 0
        x, y, cx, cy = self.window.bbox("WIDGET")
        print(x, y, cx, cy)
        x += int(self.window.winfo_rootx() + (self.window.winfo_width() / 2) - (width / 2))
        y += int(self.window.winfo_rooty() + (self.window.winfo_height() / 2) - (height / 2))
        # toplevel.wm_overrideredirect(True)
        self.toplevel_window.geometry('%dx%d+%d+%d' % (width, height, x, y))
        print(self.window.winfo_rootx(), self.window.winfo_width(), self.toplevel_window.winfo_width())

        # self.toplevel_window.transient(self.window)
        # self.toplevel_window.grab_set()







# def resizeable_window(min_width, min_height, max_width=None, max_height=None):
#     def on_resize(event):
#         if max_width and event.width > max_width:
#             event.widget.geometry(f"{max_width}x{event.height}")
#         elif max_height and event.height > max_height:
#             event.widget.geometry(f"{event.width}x{max_height}")
#         elif event.width < min_width:
#             event.widget.geometry(f"{min_width}x{event.height}")
#         elif event.height < min_height:
#             event.widget.geometry(f"{event.width}x{min_height}")
#         else:
#             print(f"Width: {event.width}, Height: {event.height}")