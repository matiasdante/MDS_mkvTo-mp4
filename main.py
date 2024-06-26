from moviepy.editor import VideoFileClip
import tkinter as tk
from tkinter import filedialog

def convert_video(input_file, output_file, codec):
    video = VideoFileClip(input_file)
    video.write_videofile(output_file, codec=codec)

def main():
    # Open file dialog to select input file
    root = tk.Tk()
    root.withdraw()
    input_file = filedialog.askopenfilename()
    
    if not input_file:
        print("No input file selected.")
        return

    # Open folder dialog to select output folder
    output_folder = filedialog.askdirectory()
    
    if not output_folder:
        print("No output folder selected.")
        return

    # Define available formats and codecs
    formats = {
        '1': ('mp4', 'libx264'),
        '2': ('avi', 'libxvid'),
        '3': ('mov', 'libx264'),
        '4': ('ogv', 'libtheora'),
        '5': ('webm', 'libvpx')
    }

    # Display format options
    print("Select the output format:")
    for key, (ext, codec) in formats.items():
        print(f"{key}: .{ext}")

    # Get user selection
    choice = input("Enter the number of the desired format: ")
    if choice not in formats:
        print("Invalid choice. Exiting.")
        return

    # Get the selected format and codec
    selected_format, selected_codec = formats[choice]

    # Ask the user for the output file name
    output_file_name = input("Enter the output file name (without extension): ")

    # Construct output file path
    output_file = f"{output_folder}/{output_file_name}.{selected_format}"

    # Call the convert_video function
    convert_video(input_file, output_file, selected_codec)

    print(f"Conversion complete. The output file is saved as: {output_file}")

if __name__ == "__main__":
    main()
