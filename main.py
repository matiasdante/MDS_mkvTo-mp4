from moviepy.editor import VideoFileClip
import tkinter as tk
from tkinter import filedialog

def convert_to_mp4(input_file, output_file):
    video = VideoFileClip(input_file)
    video.write_videofile(output_file, codec='libx264')

# Open file dialog to select input file
root = tk.Tk()
root.withdraw()
input_file = filedialog.askopenfilename()

# Open folder dialog to select output folder
output_folder = filedialog.askdirectory()

# Construct output file path
output_file = output_folder + "/output.mp4"

# Call the convert_to_mp4 function
convert_to_mp4(input_file, output_file)

convert_to_mp4(input_file, output_file)