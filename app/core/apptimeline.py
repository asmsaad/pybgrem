"""
╔══════════════════════════════════════════════════════════╗
║                    apptimeline.py                        ║
╚══════════════════════════════════════════════════════════╝
┌──────────────────────────────────────────────────────────┐
│                          Author                          │
├──────┬────────────────────┬───────┬──────────────────────┤
│ Name │ A S M Saad         │ Email │ asmsaad3@gmail.com   │
├──────┼────────────────────┼───────┼──────────────────────┤
│ Date │ April 10, 2023     │ Github│ asmsaad/pybgrem      │
├──────┴────────────────────┴───────┴──────────────────────┤
│                       Description                        │
├──────────────────────────────────────────────────────────┤
│                                                          │
│                                                          │
└──────────────────────────────────────────────────────────┘
"""

from tkinter import *
from tkinter import ttk
from app.core.appsettings import *
from app.core.appeffects import ImageHoverEffect
from app.core.appvectors import *
from app.core.appbgrem import *
from app.core.tksupport import Tooltip
# from app.core.core import APP_SAVE_FILES
import numpy as np
import os,time,copy
from threading import Thread




TIMELINE_DISPLAY_IMAGE_HEIGHT = TIMELINE_HEIGHT-TIMELINE_INFO_BAR_HEIGHT-TIMELINE_TOOL_BAR_HEIGHT
TIMELINE_DISPLAY_IMAGE_WIDTH = TIMELINE_DISPLAY_IMAGE_HEIGHT


# self.CURRENT_TIMELINE_CORD = 0


class AppTimeline:
    CURRENT_TIMELINE_CORD = 0

    SELECTED_IMAGE_FROM_TIMELINE = {}

    show_timeline_status =True
    tools_widgets = {}
    tools={
         "Control":{
            "space 1" : {'side':LEFT},
            "Batch Run": {'dim':(24,24),'side':RIGHT},
            "space 2" : {'side':LEFT},
            "Left shift":{'dim':(26,26),'side':LEFT},
            "space 3" : {'side':LEFT},
            "Right shift": {'dim':(26,26),'side':LEFT} , 
            

            #  "Current":{'dim':(20,20)}, 
            
            #  "Single Run": {'dim':(24,24)} , 
    }
            
        #  "Settings":{"Switch on":{'dim':(30,30)}},         
    }


    unprocessed_placeholder_image = Image.open("app/res/icons/timeline/loading.png")

    def __init__(self,root) -> None:
        self.root = root

        self.base_frame = Frame(self.root,background='gray',height=TIMELINE_HEIGHT ,border=0,borderwidth=0,highlightthickness=0,bd=0)
        self.base_frame.pack(expand=True,fill=X)

        
        self.navtools_frmae = Frame(self.base_frame, background='#f0f0f0',height=30 ,border=0,borderwidth=0,highlightthickness=0,bd=0)
        self.navtools_frmae.pack(expand=True,fill=X)


        self.displayimage_frmae = Frame(self.base_frame, background='#f0f0f0',height=TIMELINE_DISPLAY_IMAGE_HEIGHT ,border=0,borderwidth=0,highlightthickness=0,bd=0)
        self.displayimage_frmae.pack(expand=True,fill=X)

        self.label_frmae = Frame(self.displayimage_frmae, background='#f0f0f0',height=TIMELINE_DISPLAY_IMAGE_HEIGHT, width=16 ,border=0,borderwidth=0,highlightthickness=0,bd=0)
        self.label_frmae.pack(side=LEFT)

        img_original = APP_VECT.get_centered_text('Original')
        original_img_lbl = Label(self.label_frmae, image= img_original, height=62,border=0,borderwidth=0,highlightthickness=0,bd=0 )
        original_img_lbl.image = img_original
        original_img_lbl.pack(side=TOP)

        

        img_modified = APP_VECT.get_centered_text('Modified')
        modified_img_lbl = Label(self.label_frmae, image= img_modified, height=62,border=0,borderwidth=0,highlightthickness=0,bd=0 )
        modified_img_lbl.image = img_modified
        modified_img_lbl.pack(side=BOTTOM)

        ttk.Separator(self.label_frmae, orient='horizontal').place(relx=0, y=62, width=30 , height=1)

        self.timeline_canvas = Canvas(self.displayimage_frmae, background='white',height=TIMELINE_DISPLAY_IMAGE_HEIGHT ,border=0,borderwidth=0,highlightthickness=0,bd=0)
        self.timeline_canvas.pack(expand=True,fill=X,side=LEFT)


        # self.info_frmae = Canvas(self.base_frame, background='blue',height=TIMELINE_INFO_BAR_HEIGHT ,border=0,borderwidth=0,highlightthickness=0,bd=0)
        # self.info_frmae.pack(expand=True,fill=X)



    def set_toolbar(self):
        # self.menu_bar_start_img = APP_VECT.get('start_tool_menu',(24,24))
        for index, each_section in enumerate(self.tools):
            self.tools_widgets[each_section] = {}
            # Label(self.base_frame,padx=0 if index == 0 else 3,pady=2 , background='white').pack(side=LEFT)
            # self.tools_widgets[each_section]['menu_bar_lbl'] = Label(self.base_frame,background='white',height=24,width=10,border=0,borderwidth=0,highlightthickness=0)
            # self.tools_widgets[each_section]['menu_bar_lbl']['image'] = self.menu_bar_start_img
            # self.tools_widgets[each_section]['menu_bar_lbl'].image = self.menu_bar_start_img
            # self.tools_widgets[each_section]['menu_bar_lbl'].pack(side=LEFT)
            # Label(self.base_frame,padx=1,pady=2).pack(side=LEFT)

            for each_tool in self.tools[each_section]:
                if 'space' not in each_tool:
                    self.tools_widgets[each_section][each_tool] = {}
                    self.tools_widgets[each_section][each_tool]['image'] = {'default': APP_VECT.get(each_tool,self.tools[each_section][each_tool]['dim']) , 'hover': APP_VECT.get(each_tool+'_hover',self.tools[each_section][each_tool]['dim'])}
                    self.tools_widgets[each_section][each_tool]['button'] = Button(self.navtools_frmae,background='#f0f0f0',activebackground='#f0f0f0',height=TIMELINE_TOOL_BAR_HEIGHT,width=TIMELINE_TOOL_BAR_HEIGHT,border=0,borderwidth=0,highlightthickness=0)
                    self.tools_widgets[each_section][each_tool]['button']['image'] = self.tools_widgets[each_section][each_tool]['image']['default']
                    self.tools_widgets[each_section][each_tool]['button'].image = self.tools_widgets[each_section][each_tool]['image']['default']
                    self.tools_widgets[each_section][each_tool]['button'].pack(side=self.tools[each_section][each_tool]['side'])

                    # if each_section == 'Control' and each_tool == 'Batch Run':
                    #     self.tools_widgets[each_section][each_tool]['image']['default_'] = APP_VECT.get(each_tool+'_',self.tools[each_section][each_tool]['dim'])
                    #     self.tools_widgets[each_section][each_tool]['image']['hover_'] = APP_VECT.get(each_tool+'_hover_',self.tools[each_section][each_tool]['dim'])
                    
                    # self.tools_widgets[each_section][each_tool]['button_effect'] = ImageHoverEffect(self.tools_widgets[each_section][each_tool]['button'], (self.tools_widgets[each_section][each_tool]['image']['default'], self.tools_widgets[each_section][each_tool]['image']['hover'] ) )

                    if each_tool == 'Left shift' or each_tool == 'Right shift':
                        self.tools_widgets[each_section][each_tool]['button']['command'] = lambda type=each_tool.split()[0].lower() : self.scroll_canvas(type)

                    elif each_tool == "Batch Run":
                        self.tools_widgets[each_section][each_tool]['button']['command'] = lambda : self.on_click_batch_run_btn()

                    
                    self.tools_widgets[each_section][each_tool]['tooltip'] = Tooltip(self.tools_widgets[each_section][each_tool]['button'],each_tool)
                    self.tools_widgets[each_section][each_tool]['hover_effect'] = ImageHoverEffect(self.tools_widgets[each_section][each_tool]['button'], (self.tools_widgets[each_section][each_tool]['image']['default'], self.tools_widgets[each_section][each_tool]['image']['hover'] ) , tooltip = self.tools_widgets[each_section][each_tool]['tooltip'])
                    # ImageHoverEffect(self.tools_widgets[each_section][each_tool]['button'], (self.tools_widgets[each_section][each_tool]['image']['default'], self.tools_widgets[each_section][each_tool]['image']['hover'] ) , tooltip = self.tools_widgets[each_section][each_tool]['tooltip'])

                    # Tooltip(self.tools_widgets[each_section][each_tool]['button'],each_tool)
                else:
                    Label(self.navtools_frmae,background='#f0f0f0',activebackground='#f0f0f0',height=1,width=1,border=0,borderwidth=0,highlightthickness=0).pack(side=self.tools[each_section][each_tool]['side'])




    def scroll_canvas(self,type):

        if type == 'left':
            dx = 0 if self.CURRENT_TIMELINE_CORD == 0 else TIMELINE_DISPLAY_IMAGE_WIDTH
        elif type == 'right':
            dx = 0 if self.CURRENT_TIMELINE_CORD <= -(self.timeline_canvas.bbox("all")[2] - self.timeline_canvas.winfo_width() - 16) else -TIMELINE_DISPLAY_IMAGE_WIDTH 
            
        # if dx == 0:
        #     self.tools_widgets["Control"]["Left shift"]['button']['state'] = DISABLED
        #     self.tools_widgets["Control"]["Right shift"]['button']['state'] = NORMAL

        # elif abs(dx) >= abs(self.CURRENT_TIMELINE_CORD):
        #     self.tools_widgets["Control"]["Left shift"]['button']['state'] = NORMAL 
        #     self.tools_widgets["Control"]["Right shift"]['button']['state'] = DISABLED
        # else:
        #     self.tools_widgets["Control"]["Left shift"]['button']['state'] = NORMAL 
        #     self.tools_widgets["Control"]["Right shift"]['button']['state'] = NORMAL
            

        
        self.CURRENT_TIMELINE_CORD += dx 
        print('==>',self.timeline_canvas.bbox("all"),dx,self.CURRENT_TIMELINE_CORD)

        # canvas.xview_scroll(dx, "units")
        self.timeline_canvas.scan_mark(0, 0)  # Set the reference point at the top-left corner of the canvas
        self.timeline_canvas.scan_dragto(dx, 0, gain=1)  # Shift the canvas by dx pixels horizontally


    def scrollable_timeline(self,selected_image,type='image'):
        # if type == 'video':
        #     selected_video_files = selected_image
        #     print('**',selected_image)

        #     # Get thumbnail from video.

            



        self.modified_images = {}           #* Storing images for saving.
        self.timeline_widgets = {}

        self.infobar.show_progressbar()
        self.infobar.initiate_progressbar(len(selected_image),title = 'Importing selected image')

        print(selected_image)

        for index,img_path in enumerate(selected_image):
            self.timeline_widgets[img_path] = {}
            self.timeline_widgets[img_path]['loc'] = ''
            self.timeline_widgets[img_path]['name'] = ''
            self.timeline_widgets[img_path]['settings'] = ''
            self.timeline_widgets[img_path]['widgets'] = {}
            self.timeline_widgets[img_path]['widgets']['canvas'] = {}
            
            self.timeline_widgets[img_path]['widgets']['canvas']['base'] = Canvas(self.timeline_canvas, bg='orange' if index%2 == 0 else 'yellow', width=TIMELINE_DISPLAY_IMAGE_WIDTH, height=TIMELINE_DISPLAY_IMAGE_HEIGHT ,border=0,borderwidth=0,highlightthickness=0)
            self.timeline_canvas.create_window(index*(TIMELINE_DISPLAY_IMAGE_HEIGHT), 0, anchor='nw', window=self.timeline_widgets[img_path]['widgets']['canvas']['base'])
            # self.timeline_widgets[img_path]['widgets']['canvas']['base'].pack_propagate(True)
            
            
            
            # self.timeline_widgets[img_path]['widgets']['canvas']['base']['bg'] = 'white'
            # self.timeline_widgets[img_path]['widgets']['canvas']['base'].bind_all('<Leave>', lambda e , canvas_ = self.timeline_widgets[img_path]['widgets']['canvas']['base']  : self.mouse_hover(e,'Leave',canvas_))


            #Original Image
            # self.timeline_widgets[img_path]['widgets']['canvas']['image'] =  Image.open(base_loc+'/'+img_path) 
            self.timeline_widgets[img_path]['widgets']['canvas']['image'] =  {}
            self.timeline_widgets[img_path]['widgets']['canvas']['image']['original'] =  Image.open(img_path) 
            self.timeline_widgets[img_path]['widgets']['canvas']['image']['processed'] =  '' 

            self.timeline_widgets[img_path]['widgets']['canvas']['original'] = Canvas(self.timeline_widgets[img_path]['widgets']['canvas']['base'], bg='white' if index%2 == 0 else 'white', width=TIMELINE_DISPLAY_IMAGE_WIDTH, height=int(TIMELINE_DISPLAY_IMAGE_HEIGHT/2) ,border=0,borderwidth=0,highlightthickness=0)
            self.timeline_widgets[img_path]['widgets']['canvas']['original'].pack()
            self.timeline_widgets[img_path]['widgets']['canvas']['original'].pack_propagate(False)
            # self.timeline_widgets[img_path]['widgets']['canvas']['original'].bind('<Button-1>', lambda e,  image =  self.timeline_widgets[img_path]['widgets']['canvas']['image'] : self.update_canvas_img(e, image))

            #original image
            # Label(self.timeline_widgets[img_path]['widgets']['canvas']['original'] ,border=0,borderwidth=0,highlightthickness=0)
            self.place_image_center(self.timeline_widgets[img_path]['widgets']['canvas']['original'],image_path=img_path)
            
            
            # Processed Image
            self.timeline_widgets[img_path]['widgets']['canvas']['processed'] = Canvas(self.timeline_widgets[img_path]['widgets']['canvas']['base'], bg='white' if index % 2 == 0 else 'white', width=TIMELINE_DISPLAY_IMAGE_WIDTH, height=int(TIMELINE_DISPLAY_IMAGE_HEIGHT / 2), bd=0, borderwidth=0, highlightthickness=0)

            self.timeline_widgets[img_path]['widgets']['canvas']['processed'].pack_propagate(False)
            self.timeline_widgets[img_path]['widgets']['canvas']['processed'].pack()
            # self.place_image_center(self.timeline_widgets[img_path]['widgets']['canvas']['processed'],image_path=img_path)
            self.place_image_center(self.timeline_widgets[img_path]['widgets']['canvas']['processed'],image=Image.open("app/res/icons/timeline/remove_able.png"))
            
            #todo Text_draw
            self.timeline_widgets[img_path]['widgets']['canvas']['processed_info_text'] = self.timeline_widgets[img_path]['widgets']['canvas']['processed'].create_text(int(TIMELINE_DISPLAY_IMAGE_WIDTH/2), int(TIMELINE_DISPLAY_IMAGE_HEIGHT/2) - 6 , text="Click to clear out", font=("Arial", 8, "normal") , fill='gray' ,state= "normal" if index == 0 else "hidden")


            ttk.Separator(self.timeline_widgets[img_path]['widgets']['canvas']['base'], orient='horizontal').place(relx=0, y=62, width=TIMELINE_DISPLAY_IMAGE_WIDTH , height=1)
            # ttk.Separator(self.timeline_widgets[img_path]['widgets']['canvas']['base'], orient='vertical').place(relx=TIMELINE_DISPLAY_IMAGE_WIDTH-10, y=0, width=TIMELINE_DISPLAY_IMAGE_HEIGHT , height=1)
            ttk.Separator(self.timeline_widgets[img_path]['widgets']['canvas']['base'], orient='vertical').place(x=TIMELINE_DISPLAY_IMAGE_WIDTH-1, y=0, width=1 , height=TIMELINE_DISPLAY_IMAGE_HEIGHT)



            


            self.timeline_widgets[img_path]['widgets']['canvas']['processed'].bind('<Enter>',
                                                                                   lambda e,
            img_path = img_path:
            self.on_enter_process_canvas(e,img_path)  )
            self.timeline_widgets[img_path]['widgets']['canvas']['processed'].bind('<Leave>',
                                                                                   lambda e,
            img_path = img_path:
            self.on_leave_process_canvas(e,img_path)  )


            self.timeline_widgets[img_path]['widgets']['canvas']['base'].bind('<Enter>', 
                                                                              lambda e,
            base_img_canvas  = self.timeline_widgets[img_path]['widgets']['canvas']['base'],
            original_img_canvas  = self.timeline_widgets[img_path]['widgets']['canvas']['original'],
            modified_img_canvas  = self.timeline_widgets[img_path]['widgets']['canvas']['processed'] :
            self.timeline_enter(e,base_img_canvas,original_img_canvas,modified_img_canvas) )

            
            self.timeline_widgets[img_path]['widgets']['canvas']['base'].bind('<Leave>', 
                                                                              lambda e,
            base_img_canvas  = self.timeline_widgets[img_path]['widgets']['canvas']['base'],
            original_img_canvas  = self.timeline_widgets[img_path]['widgets']['canvas']['original'],
            modified_img_canvas  = self.timeline_widgets[img_path]['widgets']['canvas']['processed'] :
            self.timeline_leave(e,base_img_canvas,original_img_canvas,modified_img_canvas) )

            
            self.timeline_widgets[img_path]['widgets']['canvas']['original'].bind('<Button-1>', 
                                                                              lambda e,
            clicked_on = 'original',
            img_path= img_path,
            image = self.timeline_widgets[img_path]['widgets']['canvas']['image'],                                                                  
            base_img_canvas  = self.timeline_widgets[img_path]['widgets']['canvas']['base'],
            original_img_canvas  = self.timeline_widgets[img_path]['widgets']['canvas']['original'],
            modified_img_canvas  = self.timeline_widgets[img_path]['widgets']['canvas']['processed'] :
            self.timeline_image_click(e, image, clicked_on, base_img_canvas,original_img_canvas,modified_img_canvas, img_path=img_path) )

            self.timeline_widgets[img_path]['widgets']['canvas']['processed'].bind('<Button-1>', 
                                                                              lambda e,
            clicked_on = 'processed',
            img_path= img_path, 
            image = self.timeline_widgets[img_path]['widgets']['canvas']['image'],                                                                 
            base_img_canvas  = self.timeline_widgets[img_path]['widgets']['canvas']['base'],
            original_img_canvas  = self.timeline_widgets[img_path]['widgets']['canvas']['original'],
            modified_img_canvas  = self.timeline_widgets[img_path]['widgets']['canvas']['processed'] :
            self.timeline_image_click(e,image , clicked_on, base_img_canvas,original_img_canvas,modified_img_canvas, img_path=img_path) )

            

        
            self.infobar.update_progressbar(index+1)

        time.sleep(5)
        self.infobar.hide_progressbar()

    
    def resize_image(self,image,margin=5):

        window_width  = TIMELINE_DISPLAY_IMAGE_WIDTH - (margin*2)
        window_height = int(TIMELINE_DISPLAY_IMAGE_HEIGHT/2) - (margin*2)

        original_width, original_height = image.size
        
        # Calculate the aspect ratio of the original image
        original_aspect_ratio = original_width / original_height
        # Calculate the aspect ratio of the window
        window_aspect_ratio = window_width / window_height
        
        # Resize the image to fit within the window dimensions while maintaining aspect ratio
        if window_aspect_ratio > original_aspect_ratio:
            # Window is wider than the image, adjust height
            new_height = window_height
            new_width = int(new_height * original_aspect_ratio)
        else:
            # Window is taller than the image, adjust width
            new_width = window_width
            new_height = int(new_width / original_aspect_ratio)
        
        return (new_width, new_height)
    

    
    def place_image_center(self, canvas, image_path=None , image=None):
        print(image_path)
        # if image_path is not None:
        #     print('[0bj]',image_path)
        #     image = image_path
            
        # else:
        #     print('[str]',image_path)
        #     image = Image.open(image_path)

        if image_path != None and image==None:
            image = Image.open(image_path)
        elif image != None and image_path == None:
            pass

            

        image = image.resize(self.resize_image(image),Image.LANCZOS)
        
        # Convert the image to a format Tkinter supports
        tk_image = ImageTk.PhotoImage(image)
        
        canvas_width  = TIMELINE_DISPLAY_IMAGE_WIDTH
        canvas_height = int(TIMELINE_DISPLAY_IMAGE_HEIGHT/2)

        x = (canvas_width - image.size[0]) / 2
        y = (canvas_height - image.size[1]) / 2
        
        # Create the image on the canvas
        canvas.create_image(x, y, anchor=NW, image=tk_image)
        # Ensure that the image persists by keeping a reference to the Tkinter image object
        canvas.image = tk_image



    def timeline_enter(self,e,base_img_canvas,original_img_canvas,modified_img_canvas):
        # if type == 'Enter':
        #     canvas_['bg'] = 'red'
        # else:
        #     canvas_['bg'] = 'white'
        #     canvas_['border'] = 0

        # original_img_canvas['bg'] = '#d9daff'
        original_img_canvas['bg'] = '#f2f3ff'
        modified_img_canvas['bg'] = '#f2f3ff'

        print('all Enter')
        ...

    def timeline_leave(self,e,base_img_canvas,original_img_canvas,modified_img_canvas):
        # if type == 'Enter':
        #     canvas_['bg'] = 'red'
        # else:
        #     canvas_['bg'] = 'white'
        #     canvas_['border'] = 0

        original_img_canvas['bg'] = 'white'
        modified_img_canvas['bg'] = 'white'

        print('all Leave')
        ...


    def timeline_image_click(self, e, image, clicked_on  ,base_img_canvas,original_img_canvas,modified_img_canvas,img_path=None):
        print('>> ', clicked_on)


        if self.SELECTED_IMAGE_FROM_TIMELINE != {} :
            self.SELECTED_IMAGE_FROM_TIMELINE['original']['bg'] = 'white'
            self.SELECTED_IMAGE_FROM_TIMELINE['modified']['bg'] = 'white'

            self.SELECTED_IMAGE_FROM_TIMELINE['base'].bind('<Enter>', 
                                                        lambda e,
            base_img_canvas  = self.SELECTED_IMAGE_FROM_TIMELINE['base'],
            original_img_canvas  = self.SELECTED_IMAGE_FROM_TIMELINE['original'],
            modified_img_canvas  = self.SELECTED_IMAGE_FROM_TIMELINE['modified'] :
            self.timeline_enter(e,base_img_canvas,original_img_canvas,modified_img_canvas) )

            self.SELECTED_IMAGE_FROM_TIMELINE['base'].bind('<Leave>', 
                                                        lambda e,
            base_img_canvas  = self.SELECTED_IMAGE_FROM_TIMELINE['base'],
            original_img_canvas  = self.SELECTED_IMAGE_FROM_TIMELINE['original'],
            modified_img_canvas  = self.SELECTED_IMAGE_FROM_TIMELINE['modified'] :
            self.timeline_leave(e,base_img_canvas,original_img_canvas,modified_img_canvas) )




        base_img_canvas.unbind("<Enter>")
        base_img_canvas.unbind("<Leave>")
        


        
        if clicked_on == 'original':
            original_img_canvas['bg'] = '#d9daff'
            modified_img_canvas['bg'] = '#f2f3ff'
            #click to show image
            self.appcanvas.update_imgae(image=image['original'])
        else:
            original_img_canvas['bg'] = '#f2f3ff'
            modified_img_canvas['bg'] = '#d9daff'
            #click to show image
            if image['processed'] == '':
                #do removing process
                def make_remove():
                    self.place_image_center(modified_img_canvas,image=self.unprocessed_placeholder_image)
                    self.timeline_widgets[img_path]['widgets']['canvas']['processed'].itemconfig(self.timeline_widgets[img_path]['widgets']['canvas']['processed_info_text'], state="hidden")
                    image['processed'] = REMOVE_BG.remove(image['original'])                    
                    self.place_image_center(modified_img_canvas,image=image['processed'])
                    self.appcanvas.update_imgae(image=image['processed'])

                    
                    
                    self.update_saveable_images(img_path) # Store processed image for save functionality.
                    
                    #* Transfer all processed images for the save function.
                    save_path = "/".join(os.path.abspath(img_path).split('\\')[:-1])
                    self.APP_SAVE_FILES.save_at_default_folder(self.modified_images,save_path,type='image')

                remove_bg_fun = Thread(target=make_remove)
                remove_bg_fun.start()
                self.timeline_widgets[img_path]['widgets']['canvas']['processed'].itemconfig(self.timeline_widgets[img_path]['widgets']['canvas']['processed_info_text'], state="hidden")
                # remove_bg_fun.join()

            else:
                self.appcanvas.update_imgae(image=image['processed'])
                self.place_image_center(modified_img_canvas,image=image['processed'])
                ...

            


        self.SELECTED_IMAGE_FROM_TIMELINE={
            'base' : base_img_canvas,
            'original' : original_img_canvas,
            'modified' : modified_img_canvas,
        }



    #todo This function removes the background from all images one by one and passes the background image to the save functions.
    def on_click_batch_run_Thread(self):
        #* Scaling the scrolling timeline to initially show the first images to synchronize the image timeline with the processing progress.
        if self.CURRENT_TIMELINE_CORD != 0:
            animation_time = self.generate_exponential_list(150, 350, len(self.timeline_widgets.keys())) [::-1]
            if len(animation_time) < len(self.timeline_widgets.keys()):
                diffrence = len(self.timeline_widgets.keys()) - len(animation_time)
                animation_time = animation_time + [animation_time[-1] for i in range(diffrence)]
            # print('>>>',len(self.timeline_widgets.keys()), animation_time, int(abs(self.CURRENT_TIMELINE_CORD) / abs(TIMELINE_DISPLAY_IMAGE_WIDTH)))
            for each_dealay in animation_time:
                each_dealay = float("{:.3f}".format(each_dealay / 1000))
                self.scroll_canvas(type='left')
                time.sleep(each_dealay)
            

        #* Bottom info bar progress information initiated with progress bar, range, and process number.
        total_images = len(self.timeline_widgets.keys())
        self.infobar.show_progressbar()
        self.infobar.initiate_progressbar(total_images,title = 'Removing background',progress=0)
        
        
        #* Batch Run Button turns into Stop Batch Button. 
        self.stop_batch_run_btn_enable = True
        each_tool = 'Batch Run'
        self.tools_widgets['Control'][each_tool]['image']['default'] = APP_VECT.get(each_tool+'_',(20,20))
        self.tools_widgets['Control'][each_tool]['image']['hover'] = APP_VECT.get(each_tool+'_hover_',(20,20))
        self.tools_widgets['Control'][each_tool]['hover_effect'].update(default_img=self.tools_widgets['Control'][each_tool]['image']['default'],hover_img=self.tools_widgets['Control'][each_tool]['image']['hover'])
        self.tools_widgets['Control'][each_tool]['button']['command'] = lambda : self.terminate_batch_run() # Modified with the terminate batch run command.


        #* Disabling all types of collation processes such as importing, saving, and deleting from tools and menu.
        previous_menu_settings = self.running_ongoing_action(type='ongoing') #!disable all type of import and saves

        
        #* Apply the removing process to all available images on the timeline.
        for index, img_path in enumerate(self.timeline_widgets):
            image = self.timeline_widgets[img_path]['widgets']['canvas']['image']                                                                  
            modified_img_canvas  = self.timeline_widgets[img_path]['widgets']['canvas']['processed']            
            
            if image['processed'] == '':
                self.place_image_center(modified_img_canvas,image=self.unprocessed_placeholder_image)
                image['processed'] = REMOVE_BG.remove(image['original']) # Removing background operations.                   
                self.place_image_center(modified_img_canvas,image=image['processed']) # Update timeline image with processed image. 
                self.appcanvas.update_imgae(image=image['processed']) # Placed on the main canvas with processed image.
                
                self.update_saveable_images(img_path) # Store processed image for save functionality.
                self.timeline_widgets[img_path]['widgets']['canvas']['processed'].\
                itemconfig(self.timeline_widgets[img_path]['widgets']['canvas']['processed_info_text'], state="hidden") #Hide the timeline processed image placeholder image hover text 'Click for remove'.

            
            #! break #Testing purpose
            #*Scroll one step on every image process and update the bottom info bar index.
            self.scroll_canvas(type='right')
            self.infobar.update_progressbar(index+1) #showing update the progress


            #* Terminate if the "Stop Batch Run" button is pressed.
            if not self.stop_batch_run_btn_enable : break #! Terminated 



       

        



     


        # APP_SAVE_FILES.save_at_default_folder(type='image')
        #Ask for save criteria
        # print('----*',os.path.abspath(img_path))
        # print('----*',os.path.abspath(img_path).split('\\'))
        # print('----*',os.path.abspath(img_path).split('\\')[:-1])

        # time.sleep(5)
        # self.infobar.hide_progressbar()

        #* Transfer all processed images for the save function.
        save_path = "/".join(os.path.abspath(img_path).split('\\')[:-1])
        self.APP_SAVE_FILES.save_at_default_folder(self.modified_images,save_path,type='image')

        #* Enabling all disabled menus and tools during running.
        self.running_ongoing_action(type='normal',previous_menu_settings=previous_menu_settings) #! enable all type of import and saves

        
        #* Enable running another batch mode after finishing/terminating the previous batch run.
        self.tools_widgets['Control'][each_tool]['image']['default'] = APP_VECT.get(each_tool,self.tools['Control'][each_tool]['dim'])
        self.tools_widgets['Control'][each_tool]['image']['hover'] = APP_VECT.get(each_tool+'_hover',self.tools['Control'][each_tool]['dim'])
        self.tools_widgets['Control']['Batch Run']['button']['state'] = NORMAL
        self.tools_widgets['Control'][each_tool]['hover_effect'].update(default_img=self.tools_widgets['Control'][each_tool]['image']['default'],hover_img=self.tools_widgets['Control'][each_tool]['image']['hover'])
        self.tools_widgets['Control'][each_tool]['button']['command'] = lambda : self.on_click_batch_run_btn() # Modified with the batch run command.
        print('*********************************')
        

    # todo Storing processed images into a variable for saving function call.
    def update_saveable_images(self,img_path):
        self.modified_images['.'.join(os.path.abspath(img_path).split('\\')[-1].split('.')[:-1])]  = self.timeline_widgets[img_path]['widgets']['canvas']['image']['processed']


    def terminate_batch_run(self):
        self.stop_batch_run_btn_enable = False
        self.tools_widgets['Control']['Batch Run']['button']['state'] = DISABLED
        print('&&&&&&&&&')



    def pass_save_files(self, APP_SAVE_FILES):
        self.APP_SAVE_FILES = APP_SAVE_FILES


    def on_click_batch_run_btn(self):
        # Make button chage to stop 
        print('Hi')
        
        



        # Run process on the thread
        Thread(target=self.on_click_batch_run_Thread).start()





    def generate_exponential_list(self,start_range, end_range, point_number):
        # Calculate the base for the exponential growth
        base = (end_range / start_range) ** (1 / (point_number - 1))
        # Generate the list of exponentially increasing values
        exponential_list = [int(start_range * (base ** i)) for i in range(point_number)]
        return exponential_list

        # # Example usage:
        # start_range = 80
        # end_range = 250
        # point_number = 10

        # exponential_values = generate_exponential_list(start_range, end_range, point_number)
        # print("Exponential values:", exponential_values)
            





    # def update_canvas_img(self,e,image):
    #     self.appcanvas.update_imgae(image=image)

    def get_canvas(self,canvas_obj):
        self.appcanvas = canvas_obj

        

    def get_btn_control(self,running_ongoing_action):
        self.running_ongoing_action = running_ongoing_action

    def get_infobar(self,infobar_obj):
        self.infobar = infobar_obj




    def on_leave_process_canvas(self, e, img_path): 
        # if self.timeline_widgets[img_path]['widgets']['canvas']['image']['processed'] == "":
        self.timeline_widgets[img_path]['widgets']['canvas']['processed'].itemconfig(self.timeline_widgets[img_path]['widgets']['canvas']['processed_info_text'], state="hidden")
        

        
        

    def on_enter_process_canvas(self, e, img_path):
        if self.timeline_widgets[img_path]['widgets']['canvas']['image']['processed'] == "":
            self.timeline_widgets[img_path]['widgets']['canvas']['processed'].itemconfig(self.timeline_widgets[img_path]['widgets']['canvas']['processed_info_text'], state="normal")
        




if __name__ == '__main__':
    root = Tk()
    root.mainloop()