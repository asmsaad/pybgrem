# import tkinter as tk
# from tkinter import filedialog
# import cv2
# import PIL.Image, PIL.ImageTk

# class VideoPlayer:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Video Player")
        
#         self.video_width = 640
#         self.video_height = 360
        
#         self.video_frame = tk.Frame(self.root, width=self.video_width, height=self.video_height)
#         self.video_frame.pack()
        
#         self.canvas = tk.Canvas(self.video_frame, width=self.video_width, height=self.video_height)
#         self.canvas.pack()
        
#         self.play_button = tk.Button(self.root, text="Play", command=self.play_video)
#         self.play_button.pack(side=tk.LEFT)
        
#         self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_video)
#         self.pause_button.pack(side=tk.LEFT)
        
#         self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_video)
#         self.stop_button.pack(side=tk.LEFT)
        
#         self.open_button = tk.Button(self.root, text="Open", command=self.open_file)
#         self.open_button.pack(side=tk.LEFT)
        
#         self.filepath = ""
#         self.paused = False
#         self.playing = False
#         self.video = None

#     def open_file(self):
#         self.filepath = filedialog.askopenfilename()
#         if self.filepath:
#             if self.video:
#                 self.video.release()
#             self.video = cv2.VideoCapture(self.filepath)
#             self.play_video()

#     def play_video(self):
#         if self.video:
#             self.playing = True
#             while self.playing:
#                 ret, frame = self.video.read()
#                 if ret:
#                     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#                     frame = PIL.Image.fromarray(frame)
#                     frame = PIL.ImageTk.PhotoImage(image=frame)
#                     self.canvas.create_image(0, 0, anchor=tk.NW, image=frame)
#                     self.root.update()
#                 else:
#                     self.playing = False
#                     break

#     def pause_video(self):
#         self.playing = False

#     def stop_video(self):
#         self.playing = False
#         if self.video:
#             self.video.release()

# root = tk.Tk()
# app = VideoPlayer(root)
# root.mainloop()


# #todo check thambine
# import ffmpeg
# from PIL import Image


# def extract_thumbnail(video_path, thumbnail_path, time='00:00:01', size='320x240'):
#     """
#     Extract a thumbnail image from a video using ffmpeg-python.

#     Args:
#         video_path (str): Path to the input video file.
#         thumbnail_path (str): Path to save the extracted thumbnail image.
#         time (str): Time in HH:MM:SS format where to extract the thumbnail from (default is 1 second).
#         size (str): Size of the thumbnail image in WxH format (default is 320x240).
#     """
#     (
#         ffmpeg
#         .input(video_path, ss=time)
#         .output(thumbnail_path, vframes=1)
#         .run(overwrite_output=True)
#     )
#     print("Thumbnail extracted successfully!")




# # Example usage
# video_path = 'input/video.mp4'
# output_path = 'thumbnail.jpg'
# extract_thumbnail(video_path, output_path)

# # Load the generated thumbnail image using Pillow
# thumbnail_image = Image.open(output_path)
# thumbnail_image.show()  # Display the thumbnail image







# #todo TKinter ScrollBar

from tkinter import *

class ScrollableCanvas:
    def __init__(self, master):
        self.master = master

        self.canvas = Canvas(master)
        self.frame = Frame(self.canvas,bg='red')
        self.vsb = Scrollbar(master, orient="horizontal", command=self.canvas.xview)
        self.canvas.configure(xscrollcommand=self.vsb.set)

        self.canvas.pack(side="top", fill="both", expand=True)
        self.vsb.pack(side="bottom", fill="x")

        self.canvas.create_window((0,0), window=self.frame, anchor="nw", tags=self.frame)

        self.frame.bind("<Configure>", self.on_frame_configure)
        # self.canvas.bind("<Configure>", self.on_canvas_configure)

        # self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        self.create_widgets()


    def _on_mousewheel(self, event):
        self.canvas.xview_scroll(-1*(event.delta//120), "units")

    def create_widgets(self):
        # self.btn_left = Button(self.master, text="Scroll Left", command=self.scroll_left)
        # self.btn_left.pack(side="top")

        # self.btn_right = Button(self.master, text="Scroll Right", command=self.scroll_right)
        # self.btn_right.pack(side="top")

        for i in range(50):
            Label(self.frame, text="Label " + str(i)).pack(side=LEFT)

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event):
        # width = event.width
        # print(width,'---->')
        # self.canvas.itemconfig(self.frame, width=width)
        ...

    def scroll_left(self):
        self.canvas.yview_scroll(-1, "units")

    def scroll_right(self):
        self.canvas.yview_scroll(1, "units")






root = Tk()
root.geometry("400x300")
scrollable_canvas = ScrollableCanvas(root)
root.mainloop()

# #todo new mod
# from tkinter import *

# class ScrollableCanvas:
#     def __init__(self, master):
#         self.master = master
#         self.canvas = Canvas(master)
#         self.frame = Frame(self.canvas, bg='red')
#         self.vsb = Scrollbar(master, orient="horizontal", command=self.canvas.xview)
#         self.canvas.configure(xscrollcommand=self.vsb.set)

#         self.canvas.pack(side="top", fill="both", expand=True)
#         self.vsb.pack(side="bottom", fill="x")

#         self.canvas.create_window((0,0), window=self.frame, anchor="nw", tags=self.frame)

#         self.frame.bind("<Configure>", self.on_frame_configure)
#         self.canvas.bind("<Configure>", self.on_canvas_configure)

#         self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

#         self.create_widgets()


#     def _on_mousewheel(self, event):
#         self.canvas.xview_scroll(-1*(event.delta//120), "units")

#     def create_widgets(self):
#         # self.btn_left = Button(self.master, text="Scroll Left", command=self.scroll_left)
#         # self.btn_left.pack(side="top")

#         # self.btn_right = Button(self.master, text="Scroll Right", command=self.scroll_right)
#         # self.btn_right.pack(side="top")

#         for i in range(50):
#             Label(self.frame, text="Label " + str(i)).pack(side=LEFT)

#     def on_frame_configure(self, event):
#         self.canvas.configure(scrollregion=self.canvas.bbox("all"))

#     def on_canvas_configure(self, event):
#         width = event.width
#         self.canvas.itemconfig(self.frame, width=width)

#     def scroll_left(self):
#         self.canvas.yview_scroll(-1, "units")

#     def scroll_right(self):
#         self.canvas.yview_scroll(1, "units")

# root = Tk()
# root.geometry("400x300")
# scrollable_canvas = ScrollableCanvas(root)
# root.mainloop()
