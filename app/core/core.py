from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from threading import Thread
import os,time
from PIL import Image



class ImportFiles:

    def __init__(self) -> None:
        pass

    def pass_timeline(self,timeline_fun):
        self.timeline_fun = timeline_fun
    
    def load_images_into_timeline(self):
        self.timeline_fun(self.selected_image_files)

    # Import Images
    def selectfiles(self , type='all' , initialdir = '.'):



        if type == 'image':
            filetypes = [
            ("Image files", "*.png *.jpg *.jpeg"),
        ]

        elif type == 'video':
            filetypes = [
            ("Video files", "*.mp4 *.mov") ,
        ]
            
        else:
            filetypes = [
            ("Image files", "*.png *.jpg *.jpeg"),
            ("Video files", "*.mp4 *.mov") ,
        ]

        
        print(filetypes)



        
        
        if type == 'image':
            files = filedialog.askopenfilenames(
                title= "Select image or video files" if type=='all' else  "Select image files" if type=='image' else 'Select video file',
                filetypes=filetypes,
                initialdir = initialdir,
            )


            self.selected_image_files = [file for file in files if file.lower().endswith(('.jpg', '.jpeg', '.png' ,'.mp4' ,'.mov' ))]
            if len(self.selected_image_files) > 0:
                    Thread(target=self.load_images_into_timeline).start()

        elif type == 'video':
            files = filedialog.askopenfilename(
                title= "Select image or video files" if type=='all' else  "Select image files" if type=='image' else 'Select video file',
                filetypes=filetypes,
                initialdir = initialdir,
            )
                    
            print('We will work on It')




    # Import Video
    def video():
        ...


    # Import Folder
    def folder(self):
        # filetypes = [
        #     ("Image files", "*.png *.jpg *.jpeg"),
        #     ("Video files", "*.mp4 *.mov")
        # ]
        folder_dir = filedialog.askdirectory(
            title="Select folder",
            # filetypes=filetypes,
            initialdir = '.',
        )
        
        # Filter out non-image files
        # self.selected_image_files = [file for file in files if file.lower().endswith(('.jpg', '.jpeg', '.png'))]

        print(folder_dir)
        selected_image_list = []
        selected_video_list = []
        for each_file in os.listdir(folder_dir):
            if each_file.split('.')[-1].lower() in ['jpg', 'jpeg', 'png']:
                selected_image_list.append(folder_dir+'/'+each_file)

            if each_file.split('.')[-1].lower() in ['mov', 'mp4']:
                selected_video_list.append(folder_dir+'/'+each_file)

     
        if len(selected_video_list) != 0 and len(selected_image_list) != 0:
            response = messagebox.askyesno("Video and image imported simultaneously", "Please select either a video or images. Unfortunately, we can't process both on the same canvas. Select either video or images.\n\n Click 'Yes' to continue.")
            if response:
                response_ = messagebox.askyesno("Video and image imported simultaneously", "Do you want to import only images from this directory?\n\n Click 'Yes' to import images from the directory.")
                if response_:
                    self.selectfiles(type='image' , initialdir=folder_dir )
                else:
                    _response_ = messagebox.askyesno("Video and image imported simultaneously", "Do you want to import a video from this directory?\n\n Click 'Yes' to import a video from the directory.")
                    if _response_:
                        self.selectfiles(type='video', initialdir=folder_dir)
            

        elif  len(selected_image_list) > 0 and len(selected_video_list) == 0:
            # self.images(type='image')
            ...
            
        elif len(selected_image_list) == 0 and len(selected_video_list) == 1:
            # self.images(type='video')
            ...
        else:
            messagebox.showinfo("No Video or images imported", "No Video or images imported.")
        # # print('Please Select a video or the images, Video and Images can not be procese in same canvas')
        
        # print(selected_image_list)
        # print(selected_video_list)

        

            


        # else:
        #     messagebox.showinfo("Response", "You clicked No.")


        # if len(self.selected_image_files) > 0:
        #         Thread(target=self.load_images_into_timeline).start()





class SaveFiles:
    def __init__(self) -> None:
        pass

    def pass_infobar(self,infobar_obj):
        self.infobar = infobar_obj 



    def save_images_into_folder(self):
        modified_path = self.save_path.split('/')
        print('--->[1]',modified_path)
        modified_path = '/'.join(modified_path[:-1]) + '/' + modified_path[-1] + '_bgrem'

        print('--->',modified_path)
        if not os.path.exists(modified_path):
            os.makedirs(modified_path)

        total_images = len(self.file_dict.keys())
        self.infobar.show_progressbar()
        self.infobar.initiate_progressbar(total_images,title = 'Saving modified images',progress=0)
        

        # time.sleep(5)

        for index , each_image in enumerate(self.file_dict):
            print(each_image)
            print('>>> ',modified_path+'/'+  each_image  +'.png')
            # print('>>> ',modified_path+'/'+  ".".join(os.path.abspath(each_image).split('\\')[-1].split('.')[:-1])  +'.png')
            self.file_dict[each_image].save(modified_path+'/'+  each_image  +'.png')
            
            self.infobar.update_progressbar(index+1) #todo showing update the progress
        
        time.sleep(5)
        self.infobar.hide_progressbar()
        ...

    def save_at_default_folder(self,file_dict,save_path,type=None):
        self.file_dict = file_dict
        self.save_path = save_path
        self.type = type
        print('--->',self.save_path)
        self.save_at_default_folder_message()
        

    def save_at_default_folder_message(self):
        modified_path = self.save_path.split('/')
        print('--->[1]',modified_path)
        modified_path = '/'.join(modified_path[:-1]) + '/' + modified_path[-1] + '_bgrem'

        if self.type=='image':
            response = messagebox.askyesno("Save modified images", f"Do you want to save the modified image at '{modified_path}'")
            if response:
                self.save_images_into_folder()
    
    def save_at_default_folder_Thread(self):
        print(0)
        Thread(target=self.save_at_default_folder_message).start()



        

#Save Selected


#Save All


#Save As Selected


#Save as Selected






#Copy 



#Paest


#Clipboard



# Undo


#Redo





APP_IMPORT_FILES = ImportFiles()
APP_SAVE_FILES = SaveFiles()











if __name__ == '__main__':
    root = Tk()
    root.mainloop()