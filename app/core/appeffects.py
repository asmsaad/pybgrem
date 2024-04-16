from tkinter import *








class ImageHoverEffect:
    def __init__(self,widget_name:object,images:tuple) -> None:
        self.widget_name = widget_name
        self.default_img = images[0]
        self.hover_img = images[1]
        
        self.widget_name.bind('<Enter>' , self.on_mouse_enter_EL) 
        self.widget_name.bind('<Leave>' , self.on_mouse_leave_EL) 

    def update(self,default_img:object=None, hover_img:object=None) -> None:
        if default_img != None: 
            self.default_img = default_img
        if hover_img != None: 
            self.hover_img = hover_img

        self.on_mouse_enter()

        

    def on_mouse_enter_EL(self,e):
        print('Enter')
        self.on_mouse_enter()

    def on_mouse_enter(self):
        # self.widget_name['bg'] = 'orange'
        self.widget_name['image'] = self.hover_img
        self.widget_name.image = self.hover_img


    def on_mouse_leave_EL(self,e):
        print('Leave')
        self.on_mouse_leave()

    def on_mouse_leave(self):
        # self.widget_name['bg'] = 'yellow'
        self.widget_name['image'] = self.default_img
        self.widget_name.image = self.default_img


















if __name__ == '__manin__':
    root = Tk()
    root.update_idletasks()
    root.mainloop()