from tkinter import *
from threading import Thread

from datetime import datetime,timedelta
import shutil,os,getpass

from app.core.window import WindowConfiguration
from app.core.appvectors import *
from app.core.appmenu import *
from app.core.appeffects import ImageHoverEffect
from app.core.appcanvas import ResizableCanvas
from app.core.apptimeline import AppTimeline
from app.core.appsettings import *
from app.core.appmenu import AppMenu
from app.core.appbgrem import *
from app.core.tksupport import *
from app.core.core import *
from app.core.useragreement import *
from app.core.active import LicenceActivation






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





class AppMenuIcon:
    tools_widgets = {}
    
    def __init__(self,root) -> None:
        self.root = root



        






        self.base_frame = Frame(self.root,background='#f0f0f0',height=24 ,border=0,borderwidth=0,highlightthickness=0,bd=0)
        self.base_frame.pack(expand=True,fill=X)

        # self.set()


    def tool_define(self):
        self.tools={
                "File":{
                    "New": {'dispaly-text': None,'command': None, 'state' : 'disable'}, 
                    "Import images":{'dispaly-text': None,'command': lambda : self.APP_IMPORT_FILES.selectfiles(type='image') , 'state' : 'normal'}, 
                    "Import folder": {'dispaly-text': None,'command': lambda :  self.APP_IMPORT_FILES.folder(), 'state' : 'normal'}, 
                    "Import video": {'dispaly-text': None,'command': lambda :  self.APP_IMPORT_FILES.selectfiles(type='video'), 'state' : 'normal'},  
                    "Save": {'dispaly-text': None,'command': lambda : self.APP_SAVE_FILES.save_at_default_folder_Thread(), 'state' : 'normal'}, 
                    "Save as": {'dispaly-text': None,'command': None, 'state' : 'disable'}, 
                },
                "Edit":{
                    "Copy":{'dispaly-text': None,'command': None , 'state' : 'disable'}, 
                    "Cut":{'dispaly-text': None,'command': None, 'state' : 'disable'}, 
                    "Paste": {'dispaly-text': None,'command': None, 'state' : 'disable'} , 
                    "Undo": {'dispaly-text': None,'command': None, 'state' : 'disable'} , 
                    "Redo": {'dispaly-text': None,'command': None, 'state' : 'disable'},
                    },
                #  "Run":{"Single Run":'', "Batch Run":''},
            }

    def pass_import_files(self,APP_IMPORT_FILES):
        self.APP_IMPORT_FILES = APP_IMPORT_FILES
    def pass_save_files(self,APP_SAVE_FILES):
        self.APP_SAVE_FILES = APP_SAVE_FILES



    def set(self):
        self.tool_define()

        
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
                self.tools_widgets[each_section][each_tool]['button'] = Button(self.base_frame,background='#f0f0f0',activebackground='#f0f0f0',height=24,width=28,border=0,borderwidth=0,highlightthickness=0, state=self.tools[each_section][each_tool]['state'])
                self.tools_widgets[each_section][each_tool]['button']['image'] = self.tools_widgets[each_section][each_tool]['image']['default']
                self.tools_widgets[each_section][each_tool]['button'].image = self.tools_widgets[each_section][each_tool]['image']['default']
                self.tools_widgets[each_section][each_tool]['button'].pack(side=LEFT)
                # Tooltip(self.tools_widgets[each_section][each_tool]['button'],each_tool)
                self.tools_widgets[each_section][each_tool]['tooltip'] = Tooltip(self.tools_widgets[each_section][each_tool]['button'],each_tool)
                ImageHoverEffect(self.tools_widgets[each_section][each_tool]['button'], (self.tools_widgets[each_section][each_tool]['image']['default'], self.tools_widgets[each_section][each_tool]['image']['hover'] ) , tooltip = self.tools_widgets[each_section][each_tool]['tooltip'])

                self.tools_widgets[each_section][each_tool]['button']['command'] = self.tools[each_section][each_tool]['command']
                
                # Tooltip(self.tools_widgets[each_section][each_tool]['button'],each_tool)


                # if each_section == 'File':
                #     if each_tool == 'Import image':
                #         self.tools_widgets[each_section][each_tool]['button']['command'] = lambda : self.APP_IMPORT_FILES.selectfiles(type='image')
                #         ...
                #     if each_tool == 'Import folder':
                #         self.tools_widgets[each_section][each_tool]['button']['command'] = lambda :  self.APP_IMPORT_FILES.folder()
                #         ...
                #     if each_tool == 'Import video':
                #         self.tools_widgets[each_section][each_tool]['button']['command'] = lambda :  self.APP_IMPORT_FILES.selectfiles(type='video')
                #         ...
                #     if each_tool == 'Save':
                #         self.tools_widgets[each_section][each_tool]['button']['command'] = lambda :  self.APP_SAVE_FILES.save_at_default_folder_Thread()
                #         ...
                #     if each_tool == 'Save as':
                #         ...

    def disable_on_run(self, disable_menu):
        for each_section in disable_menu:
            for each_tool in disable_menu[each_section]:
                self.tools_widgets[each_section][each_tool]['button']['command'] = ''
                self.tools_widgets[each_section][each_tool]['button']['state'] = DISABLED


    def disable_enable_after_run(self, disable_menu):
        for each_section in disable_menu:
            for each_tool in disable_menu[each_section]:
                self.tools_widgets[each_section][each_tool]['button']['command'] = self.tools[each_section][each_tool]['command']
                self.tools_widgets[each_section][each_tool]['button']['state'] = NORMAL




              
         
        


class AppCanvas:
        def __init__(self,root) -> None:
            self.root = root

            #201c1c
            self.base_frame = ResizableCanvas(self.root,background='white' ,border=0,borderwidth=0,highlightthickness=0,bd=0)
            self.base_frame.pack(fill=BOTH, expand=True)

            

        def update_imgae(self,image:object = None ):
            self.base_frame.draw_image(image=image)







class App:
    def __init__(self, root) -> None:
        self.root = root
        self.configure_window()

    def configure_window(self) -> None:
        

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
        self.appmenuicon.pass_save_files(APP_SAVE_FILES) #!Pass to class
        self.appmenuicon.pass_import_files(APP_IMPORT_FILES) #!Pass to class
        self.appmenuicon.set()

        #todo app Canvas
        self.appcanvas = AppCanvas(self.root)
        

        #todo app Timeline
        self.apptimeline = AppTimeline(self.root)
        self.apptimeline.get_canvas(self.appcanvas)
        self.apptimeline.set_toolbar()
        self.apptimeline.get_btn_control(self.running_ongoing_action) #! Pass to class


        #todo licence
        licenseactivation = LicenceActivation(self.root)
        licenseactivation.get_menu_class(self.appmenu)


        #todo pass timeline to app Menu
        APP_IMPORT_FILES.pass_timeline(self.apptimeline.scrollable_timeline)
        self.appmenu.pass_import_files(APP_IMPORT_FILES) #!Pass to class
        self.appmenu.pass_licence_checker(licenseactivation) #!Pass to class
        self.apptimeline.pass_save_files(APP_SAVE_FILES) #!Pass to class
        
 
        
        


        
        #todo InfoBar
        self.infobar = InfoBar(self.root)
        #*pass to classes
        self.apptimeline.get_infobar(self.infobar)
        APP_SAVE_FILES.pass_infobar(self.infobar) #!passing infobar to save

        



        #! Disabled For a time being...
        # # messagebox.askquestion("Confirm","Are you sure?")
        # useragreementwindow = UserAgreementWindow(self.root,aggrement_text= aggrements) #! for testing turend commented
        # #? add database to get data and verify
        # if not os.path.exists('app/core/licence.json'):
        #     self.create_licence_log_file()
        #     useragreementwindow.show_first_time_trail_message = True #! for testing turend commented
        # else:
        #     licence_checking_file = open('app/core/licence.json')
        #     licence_data = json.load(licence_checking_file)
        #     #update days with respect to licence key
        #     if licence_data['key'] == "":
        #         if compare_dates(add_five_days(licence_data['first']), str(datetime.now())):
        #             self.appmenu.update_activation_date(f"{days_left(add_five_days(licence_data['first']),str(datetime.now()))} days left")
        #         else:
        #             self.appmenu.update_activation_date(f"Expired")
        #             # licence popup

                

        #     else:
        #         licenseactivation.reconstract_licence(licence_data['key'])
        #     #Make forever loop to check the licence date
        #     # def check_licence


        #     #if licence expair3ed only available licence activation window


        #* Update Trail Time on Every 5 minutes

        

        def test(val=0):


            if val == 3:
                add_dependency()
            else:
                val += 1
                self.root.after(100,test,val)

        test()

        self.root.bind("<Configure>", self.on_canvas_resize)
        



    def running_ongoing_action(self,type='ongoing',previous_menu_settings=None):
        print('.....', type)
        disable_menu = {
            "File" : [ 'Import images'  , 'Import folder' , 'Save'],
            "Effects" : ['Effect 1'],
        }
        if type == 'ongoing':
            # disable_on_run
            disable_menu_ = copy.deepcopy(disable_menu)
            del disable_menu_['Effects']
            self.appmenuicon.disable_on_run(disable_menu_)
        
            #From File Menu
            # return self.appmenu.disable_on_run(disable_menu)
            return disable_menu_

            #From Tool Menu
        else:
            # self.appmenu.disable_enable_after_run(disable_menu,previous_menu_settings)

            # disable_on_run
            disable_menu_ = copy.deepcopy(disable_menu)
            del disable_menu_['Effects']
            print(disable_menu_)
            self.appmenuicon.disable_enable_after_run(disable_menu_)






            ...

            

    def create_licence_log_file(self):
        with open('app/core/licence.json','w') as RF:
            RF.write(json.dumps({
                    "first" : str(datetime.now()),
                    "last": "",
                    "key": "",
                    "last video loc": ".",
                    "last image loc": ".",
                    "last folder loc": ".",
                }, indent= 4))
        RF.close()
    
    def on_canvas_resize(self,event):
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()

        self.appcanvas.base_frame.config(height=window_height-24-TIMELINE_HEIGHT)

        # print("Canvas Width:", window_width)
        # print("Canvas Height:", window_height)


def add_five_days(input_datetime):
    print('[0]')
    # Convert input string to datetime object
    input_datetime = datetime.strptime(input_datetime, '%Y-%m-%d %H:%M:%S.%f')
    # Add three days
    result_datetime = input_datetime + timedelta(days=5)
    # Format and print the result
    print(result_datetime.strftime('%Y-%m-%d %H:%M:%S.%f'))

    return  result_datetime



def compare_dates(datetime1, datetime2):
    print('[1]')
    # Convert input strings to datetime objects
    datetime1 = datetime.strptime(str(datetime1), '%Y-%m-%d %H:%M:%S.%f')
    datetime2 = datetime.strptime(str(datetime2), '%Y-%m-%d %H:%M:%S.%f')
    # Compare the dates
    print(datetime1, datetime2)
    if datetime1 >= datetime2:
        print("Okay")
        return True
    else:
        print("Expired")
        return False
    
def days_left(datetime1, datetime2):
    print('[2]')
    # Convert input strings to datetime objects
    datetime1 = datetime.strptime(str(datetime1), '%Y-%m-%d %H:%M:%S.%f')
    datetime2 = datetime.strptime(str(datetime2), '%Y-%m-%d %H:%M:%S.%f')
    print(datetime1, datetime2)
    # Check if datetime1 is less than or equal to datetime2
    if datetime1 < datetime2:
        print("False")
        return False
    # Calculate the difference in days
    difference = datetime1 - datetime2
    print(difference.days)
    return difference.days



def copy_folder(source_folder, destination_folder):
    try:
        # Copy the entire folder recursively
        shutil.copytree(source_folder, destination_folder)
        print("Folder copied successfully.")
    except Exception as e:
        print("Error:", e)

def add_dependency():
    destination_folder = os.path.abspath(f"C:/Users/{getpass.getuser()}/.u2net")
    if not os.path.exists(destination_folder):
        source_folder = os.path.abspath(".u2net")

        print(source_folder)
        print(destination_folder)
        print('start_copying ...')
        copy_folder(source_folder, destination_folder)
        print('stop_copying ...')
    

if __name__ == '__manin__':
    root = Tk()
    def a(val = 0 ):
        

        if val == 3:
            App(root)
        else:
            val+= 1
            root.after(10,a,val)

    a()
    root.mainloop()



#add batch run operation
#add singel run operation
# add save operation >> open a window always on top
#add save as operation >> open a window always on top
# add user aggrement operation 
#add licence activation change operation
# make licence activator 
# licence generator app


# New canvas to remove all existing job and aloww save/ save as operation
