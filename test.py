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


#todo check thambine
import ffmpeg
from PIL import Image
from io import BytesIO

def extract_thumbnail_as_pil(video_path, time='00:00:01'):
    """
    Extract a thumbnail image from a video using ffmpeg-python and return it as a PIL Image object.

    Args:
        video_path (str): Path to the input video file.
        time (str): Time in HH:MM:SS format where to extract the thumbnail from (default is 1 second).
    
    Returns:
        PIL.Image.Image: The extracted thumbnail image.
    """
    try:
        # Run FFmpeg command to extract thumbnail as bytes
        out, err = (
            ffmpeg
            .input(video_path, ss=time)
            .output('pipe:', format='rawvideo', vframes=1)
            .run(capture_stdout=True, capture_stderr=True)
        )
        
        if err:
            print("FFmpeg stderr:", err.decode('utf-8'))
            return None

        # Convert raw bytes to PIL Image
        img = Image.frombytes('RGB', (ffmpeg.input(video_path).width, ffmpeg.input(video_path).height), out)
        
        return img
    except ffmpeg.Error as e:
        print("FFmpeg error:", e.stderr.decode('utf-8'))
        return None

# Example usage:
video_path = 'input/video.mp4'
thumbnail_pil = extract_thumbnail_as_pil(video_path)
if thumbnail_pil:
    thumbnail_pil.show()  # Display the thumbnail image

