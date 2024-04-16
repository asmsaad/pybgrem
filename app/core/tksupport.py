from tkinter import *
from PIL import Image, ImageTk
from threading import Thread
import time
from gui.support.appinfo import *
from gui.support.appvect import *







class AppWindow:
    app_geometry = app_dimensions
    
    
    def __init__(self,tool_window):
        self.tool_window = tool_window
        
    #Apply all configurations
    def configure(self):
        self.window_config()

    def window_config(self):
        #Center the window initially 
        self.center_window()

        self.tool_window.resizable(False, False)

        self.app_default_nav_bar()

        
        
    def center_window( self):
        screen_width = self.tool_window.winfo_screenwidth()
        screen_height = self.tool_window.winfo_screenheight()

        x_coordinate = (screen_width / 2) - (self.app_geometry['width'] / 2)
        y_coordinate = (screen_height / 2) - (self.app_geometry['height'] / 2)

        self.tool_window.geometry("%dx%d+%d+%d" % (self.app_geometry['width'], self.app_geometry['height'], x_coordinate, y_coordinate))


    def app_default_nav_bar(self):
        self.tool_window.title(APP_TITLE)
        self.tool_window.iconphoto(True, APP_ICONS_.get('app_logo'))







class TkGif:
    stop_animation = True

    def __init__(self,file,gif_label) -> None:
        self.gif_label = gif_label
        self.file = file
        
        self.info = Image.open(self.file)
        self.total_frames = self.info.n_frames  

        self.getting_all_frame()
        
        
    def getting_all_frame(self):
        self.photoimage_objects = []
        for i in range(self.total_frames):
            obj = PhotoImage(file=self.file, format=f"gif -index {i}")
            self.photoimage_objects.append(obj)

    def run(self):
        self.download_btn = False
        self.stop_animation = False
        Thread(target=(self.animation)).start()

    def animation(self,current_frame=0):
        # global loop
        # while True:
        # if self.stop_animation == True: break

        image = self.photoimage_objects[current_frame]
        self.gif_label.configure(image=image)
        current_frame = current_frame + 1
        if current_frame == self.total_frames :
            current_frame = 0
        # time.sleep(0.05)
        if self.stop_animation != True: 
            self.gif_label.after(60, lambda: self.animation(current_frame))
        else:
            if self.download_btn == True:
                image = PhotoImage(file="gui/res/icons/download_hover_18x18.png")
                self.gif_label.configure(image=image)
                self.gif_label.image = image

            

    def stop(self):
        self.stop_animation = True


    def exceptional_download_btn(self):
        self.download_btn = True

        # self.gif_label['bg']  = 'red'
        download_report_img = APP_ICONS_.get('download_hover',dimension=(18,18))
        
        self.gif_label.configure(image=download_report_img)
        # self.gif_label['image']  = download_report_img
        # self.gif_label.image = download_report_img






if __name__ == '__main__':
    root = Tk()

    root.mainloop()




