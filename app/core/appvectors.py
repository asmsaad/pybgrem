
from PIL import Image,ImageTk,ImageFont
from typing import Union
import os

root_res_dir = 'app/res/icons/'

icons_dir = {
    'appicon' : {'img' : root_res_dir+'appicon.png',  'max':(512,512), 'min':(16,16), 'default':(32,32)},


    'start_tool_menu' : {'img' : root_res_dir+'tools/start_tool_menu.png',  'max':(512,512), 'min':(16,16), 'default':(16,16)},

    'New' : {'img' : root_res_dir+'tools/new_canvas.png',  'max':(512,512), 'min':(16,16), 'default':(16,16)},
    'New_hover' : {'img' : root_res_dir+'tools/new_canvas_hover.png',  'max':(512,512), 'min':(16,16), 'default':(16,16)},

    'Import images' : {'img' : root_res_dir+'tools/add_image.png',  'max':(512,512), 'min':(16,16), 'default':(16,16)},
    'Import images_hover' : {'img' : root_res_dir+'tools/add_image_hover.png',  'max':(512,512), 'min':(16,16), 'default':(16,16)},

    'Import video' : {'img' : root_res_dir+'tools/add_video.png',  'max':(512,512), 'min':(16,16), 'default':(16,16)},
    'Import video_hover' : {'img' : root_res_dir+'tools/add_video_hover.png',  'max':(512,512), 'min':(16,16), 'default':(16,16)},

    'Import folder' : {'img' : root_res_dir+'tools/folder.png',  'max':(512,512), 'min':(16,16), 'default':(16,16)},
    'Import folder_hover' : {'img' : root_res_dir+'tools/folder_hover.png',  'max':(512,512), 'min':(16,16), 'default':(16,16)},

    'Save' : {'img' : root_res_dir+'tools/save.png',  'max':(512,512), 'min':(16,16), 'default':(16,16)},
    'Save_hover' : {'img' : root_res_dir+'tools/save_hover.png',  'max':(512,512), 'min':(16,16), 'default':(16,16)},

    'Save as' : {'img' : root_res_dir+'tools/save_as.png',  'max':(512,512), 'min':(16,16), 'default':(16,16)},
    'Save as_hover' : {'img' : root_res_dir+'tools/save_as_hover.png',  'max':(512,512), 'min':(16,16), 'default':(16,16)},


    'Cut' : {'img' : root_res_dir+'tools/cut.png',  'max':(512,512), 'min':(16,16), 'default':(16,16)},
    'Cut_hover' : {'img' : root_res_dir+'tools/cut.png',  'max':(512,512), 'min':(16,16), 'default':(16,16)},

    'Copy' : {'img' : root_res_dir+'tools/copy.png',  'max':(512,512), 'min':(16,16), 'default':(16,16)},
    'Copy_hover' : {'img' : root_res_dir+'tools/copy_hover.png',  'max':(512,512), 'min':(16,16), 'default':(16,16)},

    'Paste' : {'img' : root_res_dir+'tools/paste.png',  'max':(512,512), 'min':(16,16), 'default':(16,16)},
    'Paste_hover' : {'img' : root_res_dir+'tools/paste.png',  'max':(512,512), 'min':(16,16), 'default':(16,16)},



    'Redo' : {'img' : root_res_dir+'tools/redo.png',  'max':(512,512), 'min':(16,16), 'default':(16,16)},
    'Redo_hover' : {'img' : root_res_dir+'tools/redo.png',  'max':(512,512), 'min':(16,16), 'default':(16,16)},

    'Undo' : {'img' : root_res_dir+'tools/undo.png',  'max':(512,512), 'min':(16,16), 'default':(16,16)},
    'Undo_hover' : {'img' : root_res_dir+'tools/undo.png',  'max':(512,512), 'min':(16,16), 'default':(16,16)},


    'Single Run' : {'img' : root_res_dir+'tools/bg_eraser.png',  'max':(512,512), 'min':(16,16), 'default':(16,16)},
    'Single Run_hover' : {'img' : root_res_dir+'tools/bg_eraser_hover.png',  'max':(512,512), 'min':(16,16), 'default':(16,16)},

    'Batch Run' : {'img' : root_res_dir+'tools/bg_eraser_all.png',  'max':(512,512), 'min':(16,16), 'default':(16,16)},
    'Batch Run_hover' : {'img' : root_res_dir+'tools/bg_eraser_all_hover.png',  'max':(512,512), 'min':(16,16), 'default':(16,16)},

    'Batch Run_' : {'img' : root_res_dir+'tools/stop.png',  'max':(512,512), 'min':(16,16), 'default':(16,16)},
    'Batch Run_hover_' : {'img' : root_res_dir+'tools/stop_hover.png',  'max':(512,512), 'min':(16,16), 'default':(16,16)},




    #Timeline
    'Left shift' : {'img' : root_res_dir+'timeline/left_arrow.png',  'max':(512,512), 'min':(16,16), 'default':(16,16)},
    'Left shift_hover' : {'img' : root_res_dir+'timeline/left_arrow.png',  'max':(512,512), 'min':(16,16), 'default':(16,16)},

    'Right shift' : {'img' : root_res_dir+'timeline/right_arrow.png',  'max':(512,512), 'min':(16,16), 'default':(16,16)},
    'Right shift_hover' : {'img' : root_res_dir+'timeline/right_arrow.png',  'max':(512,512), 'min':(16,16), 'default':(16,16)},

    'Current' : {'img' : root_res_dir+'timeline/current_task.png',  'max':(512,512), 'min':(16,16), 'default':(16,16)},
    'Current_hover' : {'img' : root_res_dir+'timeline/current_task_hover.png',  'max':(512,512), 'min':(16,16), 'default':(16,16)},

    'Switch on' : {'img' : root_res_dir+'timeline/switch_on.png',  'max':(512,512), 'min':(16,16), 'default':(16,16)},
    'Switch on_hover' : {'img' : root_res_dir+'timeline/switch_on_hover.png',  'max':(512,512), 'min':(16,16), 'default':(16,16)},

    'Switch off' : {'img' : root_res_dir+'timeline/switch_off.png',  'max':(512,512), 'min':(16,16), 'default':(16,16)},
    'Switch off_hover' : {'img' : root_res_dir+'timeline/switch_off_hover.png',  'max':(512,512), 'min':(16,16), 'default':(16,16)},
    
    
    
    'remove able image' : {'img' : root_res_dir+'timeline/remove_able.png',  'max':(40,40), 'min':(16,16), 'default':(40,40)},


}




class CenterAlignTextImage:
    def __init__(self,text,fontsize=13*10,font_loc=os.path.abspath("app/res/font/roboto/Roboto-Light.ttf"),fg='black',bg=None , dim = (60*10, 28*10 )):
        self.bg = bg
        self.dim  = dim 

        img_circle = self.base_image()
        img_number = self.get_number_img(text,fg=fg,fontsize=fontsize,font_loc=font_loc)
        self.overlay_images(img_circle, img_number)

    #todo making circle image
    def base_image(self):
        width, height = self.dim  # Adjust according to your needs
        image = Image.new("RGBA", (width, height) , None if self.bg == None else self.bg)
        return image

    #todo making nuber image
    def get_number_img(self,text,fg='white',fontsize=130,font_loc=''):
        canvas = Image.new('RGBA', (1000,1000))
        draw = ImageDraw.Draw(canvas)
        font = ImageFont.truetype(font_loc,fontsize)
        draw.text((0, 0), text, font=font, fill=fg)
        bbox = canvas.getbbox()
        cropped_image = canvas.crop(bbox)
        # cropped_image.show()
        return cropped_image

    def center_secondary_rectangle(self,base_width, base_height, secondary_width, secondary_height):
        base_center_x = base_width // 2
        base_center_y = base_height // 2
        secondary_x = base_center_x - (secondary_width // 2)
        secondary_y = base_center_y - (secondary_height // 2)
        return (secondary_x, secondary_y)

    def overlay_images(self,base_image, overlay_image):
        self.result_image = base_image.copy()
        self.result_image.paste(overlay_image, self.center_secondary_rectangle(base_image.size[0], base_image.size[1], overlay_image.size[0], overlay_image.size[1],), overlay_image)
        return self.result_image
    
    def get_img(self):
        return self.result_image


# CenterAlignTextImage('Original').get_img().resize((60, 28), Image.LANCZOS).show()
# CenterAlignTextImage('Modified').get_img().resize((60, 28), Image.LANCZOS).show()



from PIL import Image, ImageDraw

def draw_progress_bar(progress, width = 150, height = 7):

    img = Image.new('RGB', (width, height), color='#c5c3c6')
    draw = ImageDraw.Draw(img)
    
    # Draw background rectangle
    # draw.rectangle([0, 0, width, height], fill='red')
    
    # Calculate width of progress bar
    progress_width = int(progress)
    
    # Draw progress bar
    # draw.rectangle([0, 0, progress_width, height], fill='#BDF000')
    for x in range(progress_width+4):
        if x%4 == 0:
            draw.line([x,0,x-3,height],fill='#66b581',width=3)

    # img.show()
    return img



class ImageVector:
    def __init__(self) -> None:
        pass

    def get(self,name,dimentions:Union[str, tuple]) -> object :
        
        return ImageTk.PhotoImage(Image.open(icons_dir[name]['img']).resize(icons_dir[name][dimentions.lower().strip()] if isinstance(dimentions, str) else dimentions, Image.LANCZOS ))

    def get_progressbar(self,progress, width = 150, height = 5):
        return ImageTk.PhotoImage(draw_progress_bar(progress, width = width, height = height))
    
    def get_centered_text(self,text):
        return ImageTk.PhotoImage(CenterAlignTextImage(text).get_img().resize((60, 28), Image.LANCZOS).rotate(90, expand=True))
        




APP_VECT = ImageVector()

















AppImage = ImageVector()