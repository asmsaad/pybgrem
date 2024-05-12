from tkinter import *
from threading import Thread

from datetime import datetime,timedelta
import shutil,os,getpass

from app.core.window import WindowConfiguration
from app.core.appvectors import *
from app.core.appmenu import *

from app.core.appcanvas import ResizableCanvas
from app.core.apptimeline import AppTimeline
from app.core.appsettings import *
from app.core.appmenu import AppMenu
from app.core.appbgrem import *
from app.core.tksupport import *
from app.core.core import *
from app.core.useragreement import *
from app.core.active import LicenceActivation
from app.core.infobar import InfoBar
from app.core.toolsbar import AppMenuIcon






              
         
        


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
        # self.window.geometry(500, 500)
        self.window.adjust_geomety_basedon_screen_size()
        self.window.resizable(min=(500, 500))
        self.window.center_window()
        self.window.app_title('BG Remover')
        self.window.app_icon(APP_VECT.get('appicon', 'min'))


        

        # todo app menu
        self.appmenu = AppMenu(self.root)

        self.top_toolsbar_frame = Frame(self.root,background='#fbfbfb',height=TOOLBAR_HEIGHT ,border=0,borderwidth=0,highlightthickness=0,bd=0)
        self.top_toolsbar_frame.pack(fill=X,expand=True)
        
        

        #todo app menu icon
        self.appmenuicon = AppMenuIcon(self.root)
        self.appmenuicon.pass_save_files(APP_SAVE_FILES) #!Pass to class
        self.appmenuicon.pass_import_files(APP_IMPORT_FILES) #!Pass to class
        

        #todo app Canvas
        self.appcanvas = AppCanvas(self.root)
        

        #todo app Timeline
        self.apptimeline = AppTimeline(self.root)
        self.apptimeline.get_canvas(self.appcanvas)
        self.apptimeline.set_toolbar()
        self.apptimeline.get_btn_control(self.running_ongoing_action) #! Pass to class
        self.apptimeline.get_apptoolsbar(self.appmenuicon) #!Pass to class

        self.appmenuicon.pass_timeline(self.apptimeline) #!Pass to class



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

        

        self.appmenuicon.set(self.top_toolsbar_frame)
        self.appmenuicon.set(self.apptimeline.navtools_frmae) #* Toolsbar at timeline


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

        self.appcanvas.base_frame.config(height=window_height-TOOLBAR_HEIGHT-TIMELINE_HEIGHT+3)

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
