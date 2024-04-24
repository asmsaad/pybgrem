from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from threading import Thread



class CanvasGif:
    stop_animation = True

    def __init__(self,file,gif_canvas) -> None:
        self.gif_canvas = gif_canvas
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
        # self.gif_canvas.configure(image=image)

        # image = PhotoImage(file=image_path)
        # Get the width and height of the canvas
        canvas_width = self.gif_canvas.winfo_width()
        canvas_height = self.gif_canvas.winfo_height()
        # Calculate the center coordinates of the canvas
        center_x = canvas_width // 2
        center_y = canvas_height // 2
        # Create the image on the canvas at the center coordinates
        self.gif_canvas.create_image(center_x, center_y, anchor=CENTER, image=image)
        # Keep a reference to the image to prevent it from being garbage collected
        self.gif_canvas.image = image





        current_frame = current_frame + 1
        if current_frame == self.total_frames :
            current_frame = 0
        # time.sleep(0.05)
        if self.stop_animation != True: 
            self.gif_canvas.after(60, lambda: self.animation(current_frame))
        # else:
        #     if self.download_btn == True:
        #         image = PhotoImage(file="gui/res/icons/download_hover_18x18.png")
        #         self.gif_canvas.configure(image=image)
        #         self.gif_canvas.image = image

            

    def stop(self):
        self.stop_animation = True







class Tooltip:
    def __init__(self, widget, text):
        # print('***',widget,text)
        self.widget = widget
        self.text = text
        self.tooltip = None
        # self.widget['command'] = self.a
        # self.widget.bind("<Enter>", self.enter)
        # self.widget.bind("<Leave>", self.leave)
    
    def a(self):
        print("^^")
        
    def enter(self):
        self.leave_active = False

        def own_appear(val=0):
            if self.leave_active == True: return

            if val == 3:
                print('--->Entry')
                x, y, _, _ = self.widget.bbox("insert")
                x += self.widget.winfo_rootx() + 10
                y += self.widget.winfo_rooty() + 25
                
                self.tooltip = Toplevel(self.widget)
                self.tooltip.wm_overrideredirect(True)
                self.tooltip.wm_geometry(f"+{x}+{y}")
                # self.tooltip.lift()
                # self.tooltip.focus_force()
                self.tooltip.attributes("-topmost", True)
                
                label = ttk.Label(self.tooltip, text=self.text, background="#ffffe0", relief="solid", borderwidth=1, font=("TkDefaultFont", 8))
                label.pack(ipadx=1)

                own_destroy()


            else:

                val += 1
                self.widget.after(500,own_appear, val)

        

        def own_destroy(val=0):
            if self.leave_active == True: return

            if val == 8:
                self.tooltip.destroy()
                # self.tooltip = None
            val += 1
            self.widget.after(500,own_destroy, val)

        

        own_appear()

    def leave(self):
        self.leave_active = True
        print('--->Leave')
        try: 
            self.tooltip.destroy()
        except:
            print('not destrowy')
    
        # if self.tooltip != None:
        #     self.tooltip.destroy()            
        #     self.tooltip = None





if __name__ == '__main__':
    root = Tk()

    root.mainloop()




