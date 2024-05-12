from tkinter import *

from app.core.appsettings import *
from app.core.appvectors import *
# from app.core.core import *
from app.core.appeffects import ImageHoverEffect
from app.core.tksupport import *


class AppMenuIcon:
    tools_bar_number = []
    tools_widgets = {}
    
    def __init__(self,root) -> None:
        self.root = root

        self.tool_define()



        


        #f0f0f0


        # self.set()


    def tool_define(self):
        self.tools={
                "File":{
                    "New": {'dispaly-text': None,'command': None, 'state' : 'disable'}, 
                    "Import images":{'dispaly-text': None,'command': lambda : self.APP_IMPORT_FILES.selectfiles(type='image') , 'state' : 'normal'}, 
                    "Import folder": {'dispaly-text': None,'command': lambda :  self.APP_IMPORT_FILES.folder(), 'state' : 'normal'}, 
                    "Import video": {'dispaly-text': None,'command': lambda :  self.APP_IMPORT_FILES.selectfiles(type='video'), 'state' : 'normal'},  
                    "Save": {'dispaly-text': None,'command': lambda : self.APP_SAVE_FILES.save_at_default_folder_Thread(), 'state' : 'normal'}, 
                    "Save as": {'dispaly-text': None,'command': None, 'state' : 'normal'}, 
                },
                "Edit":{
                    "Copy":{'dispaly-text': None,'command': None , 'state' : 'disable'}, 
                    "Cut":{'dispaly-text': None,'command': None, 'state' : 'disable'}, 
                    "Paste": {'dispaly-text': None,'command': None, 'state' : 'disable'} , 
                    # "Undo": {'dispaly-text': None,'command': None, 'state' : 'normal'} , 
                    # "Redo": {'d ispaly-text': None,'command': None, 'state' : 'normal'},
                    },
                 "Run":{
                    #  "Single Run":{'dispaly-text': None,'command': None, 'state' : 'disable'} , 
                     "Batch Run": {'dispaly-text': None,'command': lambda : self.TIMELINE.on_click_batch_run_btn() , 'state' : 'normal'} , 
                     },
            }
        

        self.tools1={
                "File":[
                    "New",
                    "Import images",
                    "Import folder",
                    "Import video",
                    "Save",
                    "Save as",
                    ],
                "Edit":[
                    "Copy",
                    "Cut",
                    "Paste",
                    "Undo",
                    "Redo",
                    ],
                "Run":[
                     "Single Run",
                     "Batch Run",
                     ],
            }

    def pass_import_files(self,APP_IMPORT_FILES):
        self.APP_IMPORT_FILES = APP_IMPORT_FILES
    def pass_save_files(self,APP_SAVE_FILES):
        self.APP_SAVE_FILES = APP_SAVE_FILES
    def pass_timeline(self,TIMELINE):
        self.TIMELINE = TIMELINE
        



    def set(self,root_frame):
        toolbar_num = len(self.tools_bar_number) + 1
        # if toolbar_num == 1: base_frame = self.root

        self.tools_bar_number.append(toolbar_num)
        
        base_frame = Frame(root_frame,background='#fbfbfb',height=TOOLBAR_HEIGHT ,border=0,borderwidth=0,highlightthickness=0,bd=0)
        base_frame.pack(fill=X,anchor=W)

        self.tools_widgets[toolbar_num] = {}
        
        self.menu_bar_start_img = APP_VECT.get('start_tool_menu', (28,28))
        for index, each_section in enumerate(self.tools):
            self.tools_widgets[toolbar_num][each_section] = {}
            Label(base_frame,padx=0 if index == 0 else 3,pady=2 , background='#fbfbfb').pack(side=LEFT)
            self.tools_widgets[toolbar_num][each_section]['menu_bar_lbl'] = Label(base_frame,background='#fbfbfb',height=30,width=5,border=0,borderwidth=0,highlightthickness=0)
            self.tools_widgets[toolbar_num][each_section]['menu_bar_lbl']['image'] = self.menu_bar_start_img
            self.tools_widgets[toolbar_num][each_section]['menu_bar_lbl'].image = self.menu_bar_start_img
            self.tools_widgets[toolbar_num][each_section]['menu_bar_lbl'].pack(side=LEFT)
            # Label(base_frame,padx=1,pady=2).pack(side=LEFT)

            for each_tool in self.tools[each_section]:
                self.tools_widgets[toolbar_num][each_section][each_tool] = {}
                self.tools_widgets[toolbar_num][each_section][each_tool]['state'] = self.tools[each_section][each_tool]['state']
                self.tools_widgets[toolbar_num][each_section][each_tool]['image'] = {'default': APP_VECT.get(each_tool,(28,28)) , 'hover': APP_VECT.get(each_tool+'_hover',(28,28)) , 'disabled': APP_VECT.get(each_tool+'_disabled',(28,28))}
                self.tools_widgets[toolbar_num][each_section][each_tool]['button'] = Button(base_frame,background='#fbfbfb',activebackground='#fbfbfb',height=28,width=36,border=0,borderwidth=0,highlightthickness=0)
                self.tools_widgets[toolbar_num][each_section][each_tool]['button']['image'] = self.tools_widgets[toolbar_num][each_section][each_tool]['image']['default']
                self.tools_widgets[toolbar_num][each_section][each_tool]['button'].image = self.tools_widgets[toolbar_num][each_section][each_tool]['image']['default']
                self.tools_widgets[toolbar_num][each_section][each_tool]['button'].pack(side=LEFT, anchor=NW)
                
                self.tools_widgets[toolbar_num][each_section][each_tool]['tooltip'] = Tooltip(self.tools_widgets[toolbar_num][each_section][each_tool]['button'],each_tool)
                self.tools_widgets[toolbar_num][each_section][each_tool]['hovereffect'] = ImageHoverEffect(self.tools_widgets[toolbar_num][each_section][each_tool]['button'], (self.tools_widgets[toolbar_num][each_section][each_tool]['image']['default'], self.tools_widgets[toolbar_num][each_section][each_tool]['image']['hover'] ) , tooltip = self.tools_widgets[toolbar_num][each_section][each_tool]['tooltip'])
                
                if self.tools_widgets[toolbar_num][each_section][each_tool]['state'] == 'disable':
                    self.tools_widgets[toolbar_num][each_section][each_tool]['hovereffect'].update_without_effect(default_img=self.tools_widgets[toolbar_num][each_section][each_tool]['image']['disabled'],hover_img=self.tools_widgets[toolbar_num][each_section][each_tool]['image']['disabled'])
                    self.tools_widgets[toolbar_num][each_section][each_tool]['button']['relief'] = SUNKEN
                    # flat, groove, raised, ridge, solid, or sunken
                else:
                    self.tools_widgets[toolbar_num][each_section][each_tool]['button']['command'] = self.tools[each_section][each_tool]['command']
                
                 




    def make_batch_run__stop(self):
        each_section='Run'
        each_tool= 'Batch Run'
        for toolbar_num in self.tools_bar_number:
            self.tools_widgets[toolbar_num][each_section][each_tool]['image'] = {'default': APP_VECT.get(each_tool+'_',(28,28)) , 'hover': APP_VECT.get(each_tool+'_hover_',(28,28)) , 'disabled': APP_VECT.get(each_tool+'_disabled_',(28,28))}
            self.tools_widgets[toolbar_num][each_section][each_tool]['hovereffect'].update(default_img=self.tools_widgets[toolbar_num][each_section][each_tool]['image']['default'],hover_img=self.tools_widgets[toolbar_num][each_section][each_tool]['image']['hover'])
            self.tools_widgets[toolbar_num][each_section][each_tool]['button']['command'] = lambda : self.TIMELINE.terminate_batch_run()
        print(':'*5,'Making Batch Run to Stop')
        ...
    def make_stop_batch__run(self):
        each_section='Run'
        each_tool= 'Batch Run'
        for toolbar_num in self.tools_bar_number:
            self.tools_widgets[toolbar_num][each_section][each_tool]['image'] = {'default': APP_VECT.get(each_tool,(28,28)) , 'hover': APP_VECT.get(each_tool+'_hover',(28,28)) , 'disabled': APP_VECT.get(each_tool+'_disabled',(28,28))}
            self.tools_widgets[toolbar_num][each_section][each_tool]['hovereffect'].update(default_img=self.tools_widgets[toolbar_num][each_section][each_tool]['image']['default'],hover_img=self.tools_widgets[toolbar_num][each_section][each_tool]['image']['hover'])
            self.tools_widgets[toolbar_num][each_section][each_tool]['button']['command'] = lambda : self.TIMELINE.on_click_batch_run_btn()
        print(':'*5,'Making Stop Batch Run to Batch Run')
    

    def disable_on_run(self, disable_menu):
        for toolbar_num in self.tools_bar_number:
            for each_section in disable_menu:
                for each_tool in disable_menu[each_section]:
                    # self.tools_widgets[toolbar_num][each_section][each_tool]['button']['command'] = ''
                    self.tools_widgets[toolbar_num][each_section][each_tool]['button']['relief'] = SUNKEN
                    self.tools_widgets[toolbar_num][each_section][each_tool]['hovereffect'].update(default_img=self.tools_widgets[toolbar_num][each_section][each_tool]['image']['disabled'],hover_img=self.tools_widgets[toolbar_num][each_section][each_tool]['image']['disabled'])
                    self.tools_widgets[toolbar_num][each_section][each_tool]['button']['command'] = ''


    def disable_enable_after_run(self, disable_menu):
        for toolbar_num in self.tools_bar_number:
            for each_section in disable_menu:
                for each_tool in disable_menu[each_section]:
                    # self.tools_widgets[toolbar_num][each_section][each_tool]['button']['command'] = self.tools[each_section][each_tool]['command']
                    self.tools_widgets[toolbar_num][each_section][each_tool]['button']['relief'] = RAISED
                    self.tools_widgets[toolbar_num][each_section][each_tool]['hovereffect'].update(default_img=self.tools_widgets[toolbar_num][each_section][each_tool]['image']['default'],hover_img=self.tools_widgets[toolbar_num][each_section][each_tool]['image']['hover'])
                    self.tools_widgets[toolbar_num][each_section][each_tool]['button']['command'] = self.tools[each_section][each_tool]['command']



