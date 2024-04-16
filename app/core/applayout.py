from tkinter import *
from threading import Thread
from app.core.window import WindowConfiguration
from app.core.appvectors import *
from app.core.appmenu import *
from app.core.appeffects import ImageHoverEffect
from app.core.appcanvas import ResizableCanvas
from app.core.apptimeline import AppTimeline
from app.core.appsettings import *
from app.core.appmenu import AppMenu
from app.core.appbgrem import *





class InfoBar:
    def __init__(self,root) -> None:
        self.base_frame = Canvas(root, background='#f0f0f0',height=TIMELINE_INFO_BAR_HEIGHT ,border=0,borderwidth=0,highlightthickness=0,bd=0)
        self.base_frame.pack(expand=True,fill=X)

        self.progress_frame = Frame(self.base_frame, background='#f0f0f0',height=TIMELINE_INFO_BAR_HEIGHT ,border=0,borderwidth=0,highlightthickness=0,bd=0)
        # self.progress_frame.pack(side=RIGHT)

        # self.initiate_progressbar(210,progress=0)
        # self.update_progressbar(50)

    
    def show_progressbar(self):
        self.progress_frame.pack(side=RIGHT)
    def hide_progressbar(self):
        self.progress_frame.pack_forget()



    def initiate_progressbar(self,total,title = 'Importing selected image',progress=0):
        self.individual_process_time = ['0']
        
        self.total = total
        self.bar_width = 200
        self.bar_height= TIMELINE_INFO_BAR_HEIGHT-10

        

        self.progress_title = Label(self.progress_frame, text=title, background='#f0f0f0', foreground='#dad7cd' ,padx=10 ,font=INFO_BAR_FONT, border=0, borderwidth=0, highlightthickness=0)
        self.progress_title.pack(side=LEFT)

        progress_image =  APP_VECT.get_progressbar(progress, width = self.bar_width, height = self.bar_height)
        self.progress_bar = Label(self.progress_frame, image=progress_image , background='#f0f0f0' , activebackground='#f0f0f0' , height=TIMELINE_INFO_BAR_HEIGHT, width=self.bar_width ,pady=3 , border=0, borderwidth=0, highlightthickness=0)
        self.progress_bar.image = progress_image
        self.progress_bar.pack(side=LEFT)

        self.progress_count = Label(self.progress_frame, text=f'[ {str(progress).rjust(len(str(self.total))," ")} / {self.total} ]', background='#f0f0f0', foreground='#dad7cd',font=INFO_BAR_FONT , padx=10, border=0, borderwidth=0, highlightthickness=0)
        self.progress_count.pack(side=LEFT)

        self.estimeted_time = Label(self.progress_frame, text=f'00:00:00', background='#f0f0f0', foreground='#dad7cd',font=INFO_BAR_FONT , padx=10, border=0, borderwidth=0, highlightthickness=0)
        self.estimeted_time.pack(side=LEFT)

    def update_progressbar(self,progress):

        self.progress = (self.bar_width/self.total) * progress
        print(self.progress)
        

        progress_image =  APP_VECT.get_progressbar(self.progress, width = self.bar_width, height = self.bar_height)
        self.progress_bar['image'] = progress_image
        self.progress_bar.image = progress_image

        self.progress_count['text'] = f'[ {str(progress).rjust(len(str(self.total))," ")} / {self.total} ]'
        self.estimeted_time['text'] = self.convert_to_time_format(56000)



    def convert_to_time_format(self, milliseconds):
        # Calculate time components
        milliseconds_  = milliseconds%1000
        seconds = int((milliseconds / 1000) % 60)
        minutes = int((milliseconds / (1000 * 60)) % 60)
        hours = int((milliseconds / (1000 * 60 * 60)) % 24)
        days = int(milliseconds / (1000 * 60 * 60 * 24))

        # Format the time components
        time_components = {}
        # if days > 0:
        time_components['days'] = "{:02d}d".format(days)
        # if hours > 0:
        time_components['hours'] = "{:02d}h".format(hours)
        # if minutes > 0:
        time_components['minutes'] = "{:02d}m".format(minutes)
        # if seconds > 0:
        time_components['seconds'] = "{:02d}s".format(seconds)
        # if milliseconds > 0:
        time_components['milliseconds'] = "{:03d}ms".format(milliseconds_)


        if time_components['hours'][:2] == '00' and time_components['days'][:2]  == '00':
            del time_components['hours']
            del time_components['days']
        elif time_components['hours'][:2]  != '00' and time_components['days'][:2]  == '00':
            del time_components['days']



        
        # Join and return the formatted time
        formatted_time = ' : '.join([str(time_components[each_time_param]) for each_time_param in time_components])
        return formatted_time





class AppMenuIcon:
    tools_widgets = {}
    tools={
         "File":{"New":'', "Import image":'', "Import folder": "" , "Import video": "" , "Save": "",  "Save as": ""},
         "Edit":{"Copy":'', "Cut":'', "Paste": "" , "Undo": "" , "Redo": ""},
         "Run":{"Single Run":'', "Batch Run":''},
    }
    def __init__(self,root) -> None:
        self.root = root

        self.base_frame = Frame(self.root,background='#f0f0f0',height=24 ,border=0,borderwidth=0,highlightthickness=0,bd=0)
        self.base_frame.pack(expand=True,fill=X)

        self.set()


    def set(self):
        self.menu_bar_start_img = APP_VECT.get('start_tool_menu',(24,24))
        for index, each_section in enumerate(self.tools):
            self.tools_widgets[each_section] = {}
            Label(self.base_frame,padx=0 if index == 0 else 3,pady=2 , background='#f0f0f0').pack(side=LEFT)
            self.tools_widgets[each_section]['menu_bar_lbl'] = Label(self.base_frame,background='#f0f0f0',height=24,width=10,border=0,borderwidth=0,highlightthickness=0)
            self.tools_widgets[each_section]['menu_bar_lbl']['image'] = self.menu_bar_start_img
            self.tools_widgets[each_section]['menu_bar_lbl'].image = self.menu_bar_start_img
            self.tools_widgets[each_section]['menu_bar_lbl'].pack(side=LEFT)
            # Label(self.base_frame,padx=1,pady=2).pack(side=LEFT)

            for each_tool in self.tools[each_section]:
                self.tools_widgets[each_section][each_tool] = {}
                self.tools_widgets[each_section][each_tool]['image'] = {'default': APP_VECT.get(each_tool,(24,24)) , 'hover': APP_VECT.get(each_tool+'_hover',(24,24))}
                self.tools_widgets[each_section][each_tool]['button'] = Button(self.base_frame,background='#f0f0f0',activebackground='#f0f0f0',height=24,width=28,border=0,borderwidth=0,highlightthickness=0)
                self.tools_widgets[each_section][each_tool]['button']['image'] = self.tools_widgets[each_section][each_tool]['image']['default']
                self.tools_widgets[each_section][each_tool]['button'].image = self.tools_widgets[each_section][each_tool]['image']['default']
                self.tools_widgets[each_section][each_tool]['button'].pack(side=LEFT)
                ImageHoverEffect(self.tools_widgets[each_section][each_tool]['button'], (self.tools_widgets[each_section][each_tool]['image']['default'], self.tools_widgets[each_section][each_tool]['image']['hover'] ) )



              
         
        


class AppCanvas:
        def __init__(self,root) -> None:
            self.root = root

            #201c1c
            self.base_frame = ResizableCanvas(self.root,background='white' ,border=0,borderwidth=0,highlightthickness=0,bd=0)
            self.base_frame.pack(fill=BOTH, expand=True)

            

        def update_imgae(self,image:object = None ):
            self.base_frame.draw_image(image=image)







class App:
    def __init__(self) -> None:
        self.configure_window()

    def configure_window(self) -> None:
        self.root = Tk()

        self.window = WindowConfiguration(self.root)
        self.window.geometry(500, 500)
        self.window.resizable(min=(500, 500), max=(700, 700))
        self.window.center_window()
        self.window.app_title('BG Remover')
        self.window.app_icon(APP_VECT.get('appicon', 'min'))

        # todo app menu
        self.appmenu = AppMenu(self.root)

        #todo app menu icon
        self.appmenuicon = AppMenuIcon(self.root)

        #todo app Canvas
        self.appcanvas = AppCanvas(self.root)
        

        #todo app Timeline
        self.apptimeline = AppTimeline(self.root)
        self.apptimeline.get_canvas(self.appcanvas)
        self.apptimeline.set_toolbar()

        #todo pass timeline to app Menu
        self.appmenu.pass_timeline(self.apptimeline.scrollable_timeline)
 
        
        

        
        #todo InfoBar
        self.infobar = InfoBar(self.root)
        self.apptimeline.get_infobar(self.infobar)
        

        self.root.bind("<Configure>", self.on_canvas_resize)
        self.root.mainloop()

    
    def on_canvas_resize(self,event):
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()

        self.appcanvas.base_frame.config(height=window_height-24-TIMELINE_HEIGHT)

        # print("Canvas Width:", window_width)
        # print("Canvas Height:", window_height)


if __name__ == '__manin__':
    App()
