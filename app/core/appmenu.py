from tkinter import *
from tkinter import filedialog
from threading import Thread
from app.core.core import ImportFiles
import copy,json


class TkMenu:
    menu_widgets = {}
    def __init__(self,window) -> None:
        self.window = window
        self.menu_row = Menu(self.window)
        self.window.config(menu=self.menu_row)
        

    def add_menu(self,menu_name,underline=0) -> None:
        self.menu_widgets[menu_name] = Menu(self.menu_row, tearoff=0, bg="white", fg="black" )
        self.menu_row.add_cascade(label=menu_name, menu=self.menu_widgets[menu_name], underline=underline)
      
    def add_member(self,menu_name,label='',sec_label='' , underline = 0 , shortcut:str = None , command = '' , shortcut_command ='', state:str ='normal' ):
        self.menu_widgets[menu_name].add_command(label=label, command=command, accelerator=sec_label, underline=underline , state=state)
        if shortcut != None and  shortcut.strip() != "":
            self.add_keyboard_shortcut(shortcut = shortcut , comment = shortcut_command)

    def add_separator(self,menu_name):
        self.menu_widgets[menu_name].add_separator()

    def add_keyboard_shortcut(self, shortcut = '' , comment = ''):
        # print('executed',shortcut)
        self.window.bind_all(f"<{shortcut}>", comment)








    






def do_something(clicked):
    print("Menu item clicked :: " , clicked)
def do_something_EL(e,clicked):
    print("Menu item clicked :: " , clicked)



class AppMenu:
    def __init__(self,root) -> None:

        self.is_running_trail = True
        self.activation_days_info  = '5 days left'
        self.root = root

        self.base_menu = {
            "File": {
                'New' : {
                    'label' : 'New',    
                    'sec_label' : 'Ctrl + N', 
                    'underline' : 0, 
                    'command' : lambda : do_something('File' +' >> '+ 'New') , 
                    'shortcut' : 'Control-n',  
                    'shortcut_command' : lambda e: do_something_EL(e,'File' +' >> '+ 'New'),
                    'state' : 'disable',
                },

                'Import images' : {
                    'label' : 'Import Images',    
                    'sec_label' : 'Ctrl + I', 
                    'underline' : 0, 
                    'command' : lambda : self.browse_images() , 
                    'shortcut' : 'Control-i',  
                    'shortcut_command' : lambda e: self.browse_images_EL(e),
                    'state' : 'normal',
                },

                'Import video' : {
                    'label' : 'Import Video',    
                    'sec_label' : 'Ctrl + V', 
                    'underline' : 0, 
                    'command' : lambda : self.browse_video() , 
                    'shortcut' : 'Control-v',  
                    'shortcut_command' : lambda e: self.browse_video_EL(e),
                    'state' : 'normal',
                },

                'Import folder' : {
                    'label' : 'Import Folder',    
                    'sec_label' : 'Ctrl + O', 
                    'underline' : 0, 
                    'command' : lambda : self.browse_folder() , 
                    'shortcut' : 'Control-o',  
                    'shortcut_command' : lambda e: self.browse_folder_EL(e),
                    'state' : 'normal',
                },

                'Save' : {
                    'label' : 'Save',    
                    'sec_label' : 'Ctrl + S', 
                    'underline' : 0, 
                    'command' : lambda : do_something('File' +' >> '+ 'Open') , 
                    'shortcut' : 'Control-s',  
                    'shortcut_command' : lambda e: self.browse_folder_EL(e), #!need to change
                    'state' : 'normal',
                },

                'Save as' : {
                    'label' : 'Save as',    
                    'sec_label' : 'Ctrl + Shift + S', 
                    'underline' : 0, 
                    'command' : lambda : do_something('File' +' >> '+ 'Open') , 
                    'shortcut' : 'Control-s',  
                    'shortcut_command' : lambda e: self.browse_folder_EL(e), #!need to change
                    'state' : 'disable',
                },


                'Seperator 1' : {},

                'History' : {
                    'label' : 'History',    
                    'sec_label' : 'Ctrl + H', 
                    'underline' : 0, 
                    'command' : lambda : do_something('File' +' >> '+ 'Open') , 
                    'shortcut' : 'Control-h',  
                    'shortcut_command' : lambda e: self.browse_folder_EL(e), #!need to change
                    'state' : 'disable',
                },

                'Exit' : {
                    'label' : 'Exit',    
                    'sec_label' : 'Ctrl + F4', 
                    'underline' : 0, 
                    'command' : lambda : do_something('File' +' >> '+ 'Open') , 
                    'shortcut' : 'Control-F4',  
                    'shortcut_command' : lambda e: self.browse_folder_EL(e), #!need to change
                    'state' : 'disable',
                },

            },

            "Edit" : {
                'Copy' : {
                    'label' : 'Copy',    
                    'sec_label' : 'Ctrl + C', 
                    'underline' : 0, 
                    'command' : lambda : do_something('Edit'+' >> '+ 'Open') , 
                    'shortcut' : 'Control-C',  
                    'shortcut_command' : lambda e: self.browse_folder_EL(e), #!need to change
                    'state' : 'disable',
                },
                'Cut' : {
                    'label' : 'Cut',    
                    'sec_label' : 'Ctrl + X', 
                    'underline' : 0, 
                    'command' : lambda : do_something('Edit'+' >> '+ 'Open') , 
                    'shortcut' : 'Control-x',  
                    'shortcut_command' : lambda e: self.browse_folder_EL(e), #!need to change
                    'state' : 'disable',
                },
                'Paste' : {
                    'label' : 'Paste',    
                    'sec_label' : 'Ctrl + V', 
                    'underline' : 0, 
                    'command' : lambda : do_something('Edit'+' >> '+ 'Open') , 
                    'shortcut' : 'Control-v',  
                    'shortcut_command' : lambda e: self.browse_folder_EL(e), #!need to change
                    'state' : 'disable',
                },
                'Undo' : {
                    'label' : 'Undo',    
                    'sec_label' : 'Ctrl + y', 
                    'underline' : 0, 
                    'command' : lambda : do_something('Edit'+' >> '+ 'Open') , 
                    'shortcut' : 'Control-y',  
                    'shortcut_command' : lambda e: self.browse_folder_EL(e), #!need to change
                    'state' : 'disable',
                },
                'Redo' : {
                    'label' : 'Redo',    
                    'sec_label' : 'Ctrl + Z', 
                    'underline' : 0, 
                    'command' : lambda : do_something('Edit'+' >> '+ 'Open') , 
                    'shortcut' : 'Control-z',  
                    'shortcut_command' : lambda e: self.browse_folder_EL(e), #!need to change
                    'state' : 'disable',
                },

            },

            "Effects":{
                    'Effect 1' : {
                        'label' : 'Effect 1',    
                        'sec_label' : 'Ctrl + Shift + 1', 
                        'underline' : 0, 
                        'command' : lambda : do_something('Effects'+' >> '+ 'Open') , 
                        'shortcut' : 'Control-C',  
                        'shortcut_command' : lambda e: self.browse_folder_EL(e), #!need to change
                        'state' : 'disable',
                    },

                    'Effect 2' : {
                        'label' : 'Effect 2',    
                        'sec_label' : 'Ctrl + Shift + 2', 
                        'underline' : 0, 
                        'command' : lambda : do_something('Effects'+' >> '+ 'Open') , 
                        'shortcut' : 'Control-C',  
                        'shortcut_command' : lambda e: self.browse_folder_EL(e), #!need to change
                        'state' : 'disable',
                    },

            },

            "Licence" : {
                    'Trail Period' : {
                        'label' : 'Trail Period',    
                        'sec_label' : self.activation_days_info, 
                        'underline' : 0, 
                        'command' : lambda : do_something('Licence'+' >> '+ 'Open') , 
                        'shortcut' : 'Control-C',  
                        'shortcut_command' : lambda e: self.browse_folder_EL(e), #!need to change 
                        'state' : 'disabled',
                    },
                    'Activated' : {
                        'label' : 'Activated',    
                        'sec_label' : self.activation_days_info , 
                        'underline' : 0, 
                        'command' : lambda : do_something('Licence'+' >> '+ 'Open') , 
                        'shortcut' : 'Control-C',  
                        'shortcut_command' : lambda e: self.browse_folder_EL(e), #!need to change
                        'state' : 'disabled',
                    },
                    'Add activation key' : {
                        'label' : 'Add activation key',    
                        'sec_label' : '', 
                        'underline' : 0, 
                        'command' : lambda : self.add_new_licence_key() , 
                        'shortcut' : 'Control-C',  
                        'shortcut_command' : lambda e: self.browse_folder_EL(e), #!need to change
                        'state' : 'normal',
                    },
                    

                },

                "Help":{
                    'Shortcuts' : {
                        'label' : 'Shortcuts',    
                        'sec_label' : 'Ctrl + C', 
                        'underline' : 0, 
                        'command' : lambda : do_something('Help'+' >> '+ 'Open') , 
                        'shortcut' : 'Control-C',  
                        'shortcut_command' : lambda e: self.browse_folder_EL(e), #!need to change
                        'state' : 'disable',
                    },

                    'Documentations' : {
                        'label' : 'Documentations',    
                        'sec_label' : 'Ctrl + C', 
                        'underline' : 0, 
                        'command' : lambda : do_something('Help'+' >> '+ 'Open') , 
                        'shortcut' : 'Control-C',  
                        'shortcut_command' : lambda e: self.browse_folder_EL(e), #!need to change
                        'state' : 'disable',
                    },

                },

                # "About":{

                # },

                # "View":{

                # },

                
                



            }











        self.working_menu = copy.deepcopy(self.base_menu)
        del self.working_menu['Licence']['Activated']
        self.update_menu()










    def update_menu(self):





      
        


        
                            

        app_menu = TkMenu(self.root)

        for each_menu in self.working_menu:
            app_menu.add_menu(each_menu,underline=0)
            for each_member in self.working_menu[each_menu]:
                # print(':::>>',each_menu,each_member,)
                # print('++',self.working_menu[each_menu][each_member]['label'])
                if 'seperator' not in each_member.lower():
                    app_menu.add_member(each_menu , label=self.working_menu[each_menu][each_member]['label'],    sec_label=self.working_menu[each_menu][each_member]['sec_label'], underline=self.working_menu[each_menu][each_member]['underline'], command= self.working_menu[each_menu][each_member]['command'] , shortcut= self.working_menu[each_menu][each_member]['shortcut'] , shortcut_command= self.working_menu[each_menu][each_member]['shortcut_command'] , state= self.working_menu[each_menu][each_member]['state']) 
                else:
                    app_menu.add_separator(each_menu)


        # menu_name = 'File'
        # app_menu.add_menu(menu_name, underline=0)
        # app_menu.add_member(menu_name, label='New',     sec_label='Ctrl + N', underline=0, command=lambda : do_something(menu_name+' >> '+ 'New') , shortcut='Control-n' , shortcut_command=lambda e: do_something_EL(e,menu_name+' >> '+ 'New') )
        # app_menu.add_member(menu_name, label='Import Images',    sec_label='Ctrl + I', underline=0, command= self.browse_images , shortcut='Control-i' , shortcut_command= lambda e: self.browse_images_EL(e))
        # # app_menu.add_member(menu_name, label=label,    sec_label=sec_label, underline=underline, command= command , shortcut=shortcut_ , shortcut_command= shortcut_command)
        
        # app_menu.add_member(menu_name, label='Import Video',    sec_label='Ctrl + V', underline=0, command= self.browse_video , shortcut='Control-v' , shortcut_command= lambda e: self.browse_video_EL(e))
        # app_menu.add_member(menu_name, label='Import Folder',    sec_label='Ctrl + O', underline=0, command= self.browse_folder , shortcut='Control-o' , shortcut_command= lambda e: self.browse_folder_EL(e))
        # app_menu.add_member(menu_name, label='Save',    sec_label='Ctrl + S', underline=0, command=lambda : do_something(menu_name+' >> '+ 'Open'))
        # app_menu.add_member(menu_name, label='Save as',    sec_label='Ctrl + Shift + S', underline=0, command=lambda : do_something(menu_name+' >> '+ 'Open'))
        # app_menu.add_separator(menu_name)
        # app_menu.add_member(menu_name, label='History', sec_label='Ctrl + H', underline=0, command=lambda : do_something(menu_name+' >> '+ 'History'))
        # app_menu.add_member(menu_name, label='Exit',    sec_label='Ctrl + O', underline=0, command=lambda : do_something(menu_name+' >> '+ 'Exit'))

        # menu_name = 'Edit'
        # app_menu.add_menu(menu_name, underline=0)
        # app_menu.add_member(menu_name, label='Copy',  sec_label='Ctrl + C', underline=0, command=lambda : do_something(menu_name+' >> '+ 'Copy'))
        # app_menu.add_member(menu_name, label='Cut',   sec_label='Ctrl + X', underline=0, command=lambda : do_something(menu_name+' >> '+ 'Cut'))
        # app_menu.add_member(menu_name, label='Paste', sec_label='Ctrl + P', underline=0, command=lambda : do_something(menu_name+' >> '+ 'Paste'))

        # menu_name = 'View'
        # app_menu.add_menu(menu_name, underline=0)
        # app_menu.add_member(menu_name, label='Copy',  sec_label='Ctrl + C', underline=0, command=lambda : do_something(menu_name+' >> '+ 'Copy'))
        # app_menu.add_member(menu_name, label='Cut',   sec_label='Ctrl + X', underline=0, command=lambda : do_something(menu_name+' >> '+ 'Cut'))
        # app_menu.add_member(menu_name, label='Paste', sec_label='Ctrl + P', underline=0, command=lambda : do_something(menu_name+' >> '+ 'Paste'))

        # menu_name = 'Effect'
        # app_menu.add_menu(menu_name, underline=5)
        # app_menu.add_member(menu_name, label='Effect 1', sec_label='Ctrl + E + 1', underline=7, command=lambda : do_something(menu_name+' >> '+ 'Effect 1'))
        # app_menu.add_member(menu_name, label='Effect 2', sec_label='Ctrl + O', underline=7, command=lambda : do_something(menu_name+' >> '+ 'Effect 2'))
        # app_menu.add_member(menu_name, label='Effect 3', sec_label='Ctrl + O', underline=7, command=lambda : do_something(menu_name+' >> '+ 'Effect 3'))

        # menu_name = 'Licence'
        # app_menu.add_menu(menu_name, underline=5)
        # if self.is_running_trail:
        #     app_menu.add_member(menu_name, label='Trail Period', sec_label=self.activation_days_info , underline=7, command=lambda : do_something(menu_name+' >> '+ 'Activated') , state='disabled')  
        # else:
        #     app_menu.add_member(menu_name, label='Activated', sec_label=self.activation_days_info , underline=7, command=lambda : do_something(menu_name+' >> '+ 'Activated') , state='disabled')
            
        # app_menu.add_member(menu_name, label='Add activation key', sec_label='', underline=7, command=lambda : self.add_new_licence_key() , state='normal')
        # # app_menu.add_member(menu_name, label='AZXF-JHVC6-GFDCX-IJHHG', sec_label='Ctrl + O', underline=7, command=lambda : do_something(menu_name+' >> '+ 'Trial'))
        # # app_menu.add_member(menu_name, label='Add new', sec_label='Ctrl + O', underline=7, command=lambda : do_something(menu_name+' >> '+ 'Add new'))

        # menu_name = 'Help'
        # app_menu.add_menu(menu_name, underline=5)
        # app_menu.add_member(menu_name, label='Shortcuts', sec_label='Ctrl + O', underline=7, command=lambda : do_something(menu_name+' >> '+ 'Shortcuts'))
        # app_menu.add_member(menu_name, label='Documentations', sec_label='Ctrl + O', underline=7, command=lambda : do_something(menu_name+' >> '+ 'Documentations'))
        
        # menu_name = 'About'
        # app_menu.add_menu(menu_name, underline=5)
        # app_menu.add_member(menu_name, label='Owener', sec_label='Ctrl + O', underline=7, command=lambda : do_something(menu_name+' >> '+ 'Owener'))
        # app_menu.add_member(menu_name, label='Others', sec_label='Ctrl + O', underline=7, command=lambda : do_something(menu_name+' >> '+ 'Others'))




    def pass_timeline(self,timeline_fun):
        self.timeline_fun = timeline_fun
    
    def load_images_into_timeline(self):
        self.timeline_fun(self.selected_image_files)

    def browse_images_EL(self,e):
        self.browse_images()
    def browse_images(self):
        self.APP_IMPORT_FILES.selectfiles(type='image')

    def browse_video_EL(self,e):
        self.browse_video()
    def browse_video(self):
        self.APP_IMPORT_FILES.selectfiles(type='video')

    def browse_folder_EL(self,e):
        self.browse_folder()
    def browse_folder(self):
        self.APP_IMPORT_FILES.folder()


    




    def disable_on_run(self,disable_menu):
        print('disable on run...')
        previous_menu_settings =  copy.deepcopy(self.working_menu)

        # disable_menu = {
        #     "File" : [ 'Import Images' , 'Import Video' , 'Import Folder' , 'Save', 'Save as'],
        #     "Effects" : ['Effect 1'],
        # }


        for each_catagory in disable_menu:
            for each_menu in disable_menu[each_catagory]:
                previous_menu_settings[each_catagory][each_menu]['state'] = 'disable'
        

        self.working_menu = copy.deepcopy(previous_menu_settings)
        self.update_menu()
        return self.working_menu

    def disable_enable_after_run(self,disable_menu,previous_menu_settings):
        print('disable enable after run ')



        for each_catagory in disable_menu:
            for each_menu in disable_menu[each_catagory]:
                previous_menu_settings[each_catagory][each_menu]['state'] = 'normal'
        

        self.working_menu = copy.deepcopy(previous_menu_settings)
        self.update_menu()
        # return self.working_menu

        




    def add_new_licence_key(self):       
        self.licenseactivation.licence_key_activation_window()
        self.update_menu()

    def update_activation_date(self,activation_days_info):        
        self.activation_days_info = activation_days_info

        self.working_menu = copy.deepcopy(self.base_menu)
        if self.is_running_trail:
            del self.working_menu['Licence']['Activated']
            self.working_menu['Licence']['Activated']['Trail Period'] = self.activation_days_info
            
        else:
            del self.working_menu['Licence']['Trail Period']
            self.working_menu['Licence']['Activated']['sec_label'] = self.activation_days_info
            
        self.update_menu()
        


    def pass_licence_checker(self,licenseactivation):
        self.licenseactivation = licenseactivation
       
    def pass_import_files(self,APP_IMPORT_FILES):
        self.APP_IMPORT_FILES = APP_IMPORT_FILES





if __name__ == '__main__':
    root = Tk()
    root.mainloop()