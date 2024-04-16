from tkinter import *
from tkinter import ttk
from app.core.appsettings import *
from app.core.appeffects import ImageHoverEffect
from app.core.appvectors import *
from app.core.appbgrem import *
import os,time
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
         "Control":{"Left shift":{'dim':(26,26)}, "Current":{'dim':(20,20)}, "Right shift": {'dim':(26,26)}},
        #  "Settings":{"Switch on":{'dim':(30,30)}},         
    }

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
                self.tools_widgets[each_section][each_tool] = {}
                self.tools_widgets[each_section][each_tool]['image'] = {'default': APP_VECT.get(each_tool,self.tools[each_section][each_tool]['dim']) , 'hover': APP_VECT.get(each_tool+'_hover',self.tools[each_section][each_tool]['dim'])}
                self.tools_widgets[each_section][each_tool]['button'] = Button(self.navtools_frmae,background='#f0f0f0',activebackground='#f0f0f0',height=TIMELINE_TOOL_BAR_HEIGHT,width=TIMELINE_TOOL_BAR_HEIGHT,border=0,borderwidth=0,highlightthickness=0)
                self.tools_widgets[each_section][each_tool]['button']['image'] = self.tools_widgets[each_section][each_tool]['image']['default']
                self.tools_widgets[each_section][each_tool]['button'].image = self.tools_widgets[each_section][each_tool]['image']['default']
                self.tools_widgets[each_section][each_tool]['button'].pack(side=LEFT)
                self.tools_widgets[each_section][each_tool]['button_effect'] = ImageHoverEffect(self.tools_widgets[each_section][each_tool]['button'], (self.tools_widgets[each_section][each_tool]['image']['default'], self.tools_widgets[each_section][each_tool]['image']['hover'] ) )

                if each_tool == 'Left shift' or each_tool == 'Right shift':
                    self.tools_widgets[each_section][each_tool]['button']['command'] = lambda type=each_tool.split()[0].lower() : self.scroll_canvas(type)

                # elif each_tool == 'Right shift':
                    ...
                    # self.tools_widgets[each_section][each_tool]['button']['command'] = lambda x_cord = (self.timeline_canvas.bbox("all")[2] - 16) if self.CURRENT_TIMELINE_CORD==(self.timeline_canvas.bbox("all")[2] - 16) else self.CURRENT_TIMELINE_CORD+TIMELINE_DISPLAY_IMAGE_WIDTH: self.scroll_canvas(x_cord)


    def scroll_canvas(self,type):

        if type == 'left':
            dx = 0 if self.CURRENT_TIMELINE_CORD == 0 else TIMELINE_DISPLAY_IMAGE_WIDTH
        elif type == 'right':
            dx = 0 if self.CURRENT_TIMELINE_CORD <= -(self.timeline_canvas.bbox("all")[2] - self.timeline_canvas.winfo_width() - 16) else -TIMELINE_DISPLAY_IMAGE_WIDTH 
            

        
        self.CURRENT_TIMELINE_CORD += dx 
        print('==>',self.timeline_canvas.bbox("all"),dx,self.CURRENT_TIMELINE_CORD)

        # canvas.xview_scroll(dx, "units")
        self.timeline_canvas.scan_mark(0, 0)  # Set the reference point at the top-left corner of the canvas
        self.timeline_canvas.scan_dragto(dx, 0, gain=1)  # Shift the canvas by dx pixels horizontally


    def scrollable_timeline(self,selected_image):
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
            self.place_image_center(self.timeline_widgets[img_path]['widgets']['canvas']['processed'],image_path="app/res/icons/timeline/remove_able.png")



            ttk.Separator(self.timeline_widgets[img_path]['widgets']['canvas']['base'], orient='horizontal').place(relx=0, y=62, width=TIMELINE_DISPLAY_IMAGE_WIDTH , height=1)
            # ttk.Separator(self.timeline_widgets[img_path]['widgets']['canvas']['base'], orient='vertical').place(relx=TIMELINE_DISPLAY_IMAGE_WIDTH-10, y=0, width=TIMELINE_DISPLAY_IMAGE_HEIGHT , height=1)
            ttk.Separator(self.timeline_widgets[img_path]['widgets']['canvas']['base'], orient='vertical').place(x=TIMELINE_DISPLAY_IMAGE_WIDTH-1, y=0, width=1 , height=TIMELINE_DISPLAY_IMAGE_HEIGHT)




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
            image = self.timeline_widgets[img_path]['widgets']['canvas']['image'],                                                                  
            base_img_canvas  = self.timeline_widgets[img_path]['widgets']['canvas']['base'],
            original_img_canvas  = self.timeline_widgets[img_path]['widgets']['canvas']['original'],
            modified_img_canvas  = self.timeline_widgets[img_path]['widgets']['canvas']['processed'] :
            self.timeline_image_click(e, image, clicked_on, base_img_canvas,original_img_canvas,modified_img_canvas) )

            self.timeline_widgets[img_path]['widgets']['canvas']['processed'].bind('<Button-1>', 
                                                                              lambda e,
            clicked_on = 'processed', 
            image = self.timeline_widgets[img_path]['widgets']['canvas']['image'],                                                                 
            base_img_canvas  = self.timeline_widgets[img_path]['widgets']['canvas']['base'],
            original_img_canvas  = self.timeline_widgets[img_path]['widgets']['canvas']['original'],
            modified_img_canvas  = self.timeline_widgets[img_path]['widgets']['canvas']['processed'] :
            self.timeline_image_click(e,image , clicked_on, base_img_canvas,original_img_canvas,modified_img_canvas) )

            

        
            self.infobar.update_progressbar(index+1)

        time.sleep(20)
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


    def timeline_image_click(self, e, image, clicked_on  ,base_img_canvas,original_img_canvas,modified_img_canvas):
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
                image['processed'] = REMOVE_BG.remove(image['original'])
                self.appcanvas.update_imgae(image=image['processed'])
                ...
            else:
                self.appcanvas.update_imgae(image=image['processed'])
                ...

            self.place_image_center(modified_img_canvas,image=image['processed'])


        self.SELECTED_IMAGE_FROM_TIMELINE={
            'base' : base_img_canvas,
            'original' : original_img_canvas,
            'modified' : modified_img_canvas,
        }



    # def update_canvas_img(self,e,image):
    #     self.appcanvas.update_imgae(image=image)

    def get_canvas(self,canvas_obj):
        self.appcanvas = canvas_obj

        


    def get_infobar(self,infobar_obj):
        self.infobar = infobar_obj




if __name__ == '__main__':
    root = Tk()
    root.mainloop()