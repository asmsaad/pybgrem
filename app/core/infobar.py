from tkinter import *

from app.core.appsettings import *
from app.core.appvectors import *









class InfoBar:
    def __init__(self,root) -> None:
        self.base_frame = Canvas(root, background='red',height=TIMELINE_INFO_BAR_HEIGHT ,border=0,borderwidth=0,highlightthickness=0,bd=0)
        self.base_frame.pack(expand=True,fill=X)

        #f0f0f0
        self.progress_frame = Frame(self.base_frame, background='red',height=TIMELINE_INFO_BAR_HEIGHT ,border=0,borderwidth=0,highlightthickness=0,bd=0)
        # self.progress_frame.pack(side=RIGHT)

        # self.initiate_progressbar(210,progress=0)
        # self.update_progressbar(50)

    
    def show_progressbar(self):
        self.progress_frame.pack(side=RIGHT)
    def hide_progressbar(self):
        self.progress_frame.pack_forget()



    def initiate_progressbar(self,total,title = 'Importing selected image',progress=0):


        for child in self.progress_frame.winfo_children():
            child.destroy()

        self.individual_process_time = ['0']
        
        self.total = total
        self.bar_width = 200
        self.bar_height= TIMELINE_INFO_BAR_HEIGHT-10

        print(f'::: {str(progress)} {str(total)} :::')

        self.progress_title = Label(self.progress_frame, text=title, background='#f0f0f0', foreground='#474554' ,padx=10 ,font=INFO_BAR_FONT, border=0, borderwidth=0, highlightthickness=0)
        self.progress_title.pack(side=LEFT)

        progress_image =  APP_VECT.get_progressbar(progress, width = self.bar_width, height = self.bar_height)
        self.progress_bar = Label(self.progress_frame, image=progress_image , background='#f0f0f0' , activebackground='#f0f0f0' , height=TIMELINE_INFO_BAR_HEIGHT, width=self.bar_width ,pady=3 , border=0, borderwidth=0, highlightthickness=0)
        self.progress_bar.image = progress_image
        self.progress_bar.pack(side=LEFT,ipady=3)

        self.progress_count = Label(self.progress_frame, text=f'[ {str(progress).rjust(len(str(self.total))," ")} / {self.total} ]', background='#f0f0f0', foreground='#474554',font=INFO_BAR_FONT , padx=10, border=0, borderwidth=0, highlightthickness=0)
        self.progress_count.pack(side=LEFT)

        self.estimeted_time = Label(self.progress_frame, text=f'00m:00s:000ms', background='#f0f0f0', foreground='#474554',font=INFO_BAR_FONT , padx=10, border=0, borderwidth=0, highlightthickness=0)
        # self.estimeted_time.pack(side=LEFT)

    def update_progressbar(self,progress):

        self.progress = (self.bar_width/self.total) * progress
        

        print(progress,self.total)
        print('***>>>',self.progress, self.bar_width, self.bar_height)
        

        progress_image =  APP_VECT.get_progressbar(self.progress, width = self.bar_width, height = self.bar_height)
        
        self.progress_bar['image'] = progress_image
        self.progress_bar.image = progress_image

        self.progress_count['text'] = f'[ {str(progress).rjust(len(str(self.total))," ")} / {self.total} ]'
        self.estimeted_time['text'] = self.convert_to_time_format(56000)

        self.progress_frame.update_idletasks()



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



