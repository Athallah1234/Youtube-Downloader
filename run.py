import tkinter as tk
from tkinter import ttk
from pytube import YouTube
from threading import Thread
from moviepy.editor import VideoFileClip
import os

def download_video(url, save_path, convert_to_mp3, resolution):
    try:
        yt = YouTube(url)
        video = yt.streams.filter(file_extension='mp4', progressive=True, resolution=resolution).first()

        if video is None:
            status_label.config(text=f"Error: Selected resolution {resolution} not available for the video.")
            return

        video_path = video.download(save_path)
        status_label.config(text=f"Video downloaded: {video_path}")

        # Get the base filename (without extension)
        base_filename = os.path.splitext(os.path.basename(video_path))[0]

        if convert_to_mp3:
            status_label.config(text="Converting to MP3...")
            mp3_path = os.path.join(save_path, f"{base_filename}.mp3")
            clip = VideoFileClip(video_path)
            clip.audio.write_audiofile(mp3_path)
            clip.close()
            status_label.config(text=f"MP3 converted: {mp3_path}")

        status_label.config(text="Download Complete")
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}")

def on_download_button_click():
    url = url_entry.get()
    save_path = save_path_entry.get()
    convert_to_mp3 = mp3_var.get()
    resolution = resolution_var.get()

    if not url or not save_path:
        status_label.config(text="Please enter a valid URL and save path")
        return

    status_label.config(text="Downloading...")

    download_thread = Thread(target=download_video, args=(url, save_path, convert_to_mp3, resolution))
    download_thread.start()

# Create the main window
root = tk.Tk()
root.title("YouTube Downloader")

# Create and place widgets
url_label = tk.Label(root, text="YouTube URL:")
url_label.pack(pady=5)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

save_path_label = tk.Label(root, text="Save Path:")
save_path_label.pack(pady=5)

save_path_entry = tk.Entry(root, width=50)
save_path_entry.pack(pady=5)

mp3_var = tk.BooleanVar()
mp3_checkbox = tk.Checkbutton(root, text="Convert to MP3", variable=mp3_var)
mp3_checkbox.pack(pady=5)

# Add resolution dropdown
resolutions = ['360p', '720p', '1080p']
resolution_var = tk.StringVar()
resolution_var.set(resolutions[0])  # Set the default resolution
resolution_label = tk.Label(root, text="Select Resolution:")
resolution_label.pack(pady=5)
resolution_dropdown = tk.OptionMenu(root, resolution_var, *resolutions)
resolution_dropdown.pack(pady=5)

download_button = tk.Button(root, text="Download", command=on_download_button_click)
download_button.pack(pady=10)

status_label = tk.Label(root, text="")
status_label.pack(pady=5)

# Run the main loop
root.mainloop()

