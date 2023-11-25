import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pytube import YouTube
from pytube import Playlist
from moviepy.editor import VideoFileClip
import os
from threading import Thread
from ttkthemes import ThemedTk  # Import the ThemedTk class
import requests

def download_video():
    status_label.config(text="Downloading...")

    video_url = url_entry.get()
    download_path = path_var.get()
    resolution = resolution_var.get()
    file_extension = file_extension_var.get()
    
    try:
        if 'playlist' in video_url.lower() and playlist_var.get():
            playlist = Playlist(video_url)
            for video in playlist.video_urls:
                download_single_video(video, download_path, resolution, file_extension)
        else:
            download_single_video(video_url, download_path, resolution, file_extension)

        status_label.config(text="Download Completed")

    except Exception as e:
        status_label.config(text="Error Occurred")
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    root.after(3000, lambda: status_label.config(text=""))

def download_single_video(video_url, download_path, resolution, file_extension):
    yt = YouTube(video_url)
    
    if metadata_var.get():
        metadata_filename = os.path.join(download_path, f"metadata_{yt.video_id}.txt")
        with open(metadata_filename, "w") as metadata_file:
            metadata_file.write(str(yt))

    if thumbnail_var.get():
        thumbnail_url = yt.thumbnail_url
        thumbnail_filename = os.path.join(download_path, f"thumbnail_{yt.video_id}.jpg")
        with open(thumbnail_filename, "wb") as thumbnail_file:
            thumbnail_file.write(requests.get(thumbnail_url).content)

    if subtitle_var.get():
        subtitles = yt.captions
        for caption in subtitles:
            caption.download(download_path, srt=True)

    if audio_only_var.get():
        video = yt.streams.filter(only_audio=True, file_extension="mp4").first()
    else:
        video = yt.streams.filter(res=f"{resolution}p", file_extension=file_extension).first()

    if convert_var.get():
        video = video.download(download_path, filename_prefix="")
        convert_to_audio(video, audio_format_var.get())
        os.remove(video)
    else:
        video = video.download(download_path)

def convert_to_audio(video_path, audio_format):
    audio_path = video_path[:-4] + f".{audio_format.lower()}"
    video_clip = VideoFileClip(video_path)
    video_clip.audio.write_audiofile(audio_path, codec=audio_format.lower())
    video_clip.close()

    try:
        if video_clip.audio.reader:
            video_clip.audio.reader.close_proc()
    except Exception as e:
        print(f"Error closing audio subprocess: {str(e)}")

    status_label.config(text=f"Conversion to {audio_format.upper()} Completed")

def download_thread():
    download_btn["state"] = "disabled"
    status_label.config(text="Downloading...")

    if hide_gui_var.get():
        root.iconify()

    thread = Thread(target=download_video)
    thread.start()
    check_thread_status(thread)

def check_thread_status(thread):
    # Check if the thread is still alive
    if thread.is_alive():
        # If alive, check the status again after 100 milliseconds
        root.after(100, lambda: check_thread_status(thread))
    else:
        # If not alive, enable the download button
        download_btn["state"] = "normal"

        # Show the GUI after the download process if it was hidden
        if hide_gui_var.get():
            root.deiconify()

def browse_path():
    path = filedialog.askdirectory()
    path_var.set(path)

def convert_checkbox_changed():
    if convert_var.get():
        resolution_dropdown.config(state="disabled")
        audio_format_label.config(state="normal")
        audio_format_entry.config(state="normal")
    else:
        resolution_dropdown.config(state="readonly")
        audio_format_label.config(state="disabled")
        audio_format_entry.config(state="disabled")
        audio_format_var.set("mp3")

root = ThemedTk(theme="arc")
root.resizable(width=False, height=False)
root.title("YouTube Downloader")

url_label = ttk.Label(root, text="Video URL or Playlist URL:")
url_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

url_entry = ttk.Entry(root, width=40, style="TEntry")
url_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

path_label = ttk.Label(root, text="Download Path:")
path_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

path_var = tk.StringVar()
path_entry = ttk.Entry(root, textvariable=path_var, width=30, style="TEntry")
path_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

browse_btn = ttk.Button(root, text="Browse", command=browse_path)
browse_btn.grid(row=1, column=2, padx=5, pady=10, sticky="w")

resolution_label = ttk.Label(root, text="Resolution:")
resolution_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")

resolutions = ["144", "240", "360", "480", "720", "1080", "1440", "2160", "4320"]
resolution_var = tk.StringVar()
resolution_dropdown = ttk.Combobox(root, textvariable=resolution_var, values=resolutions, state="readonly", style="TCombobox")
resolution_dropdown.set("720")
resolution_dropdown.grid(row=2, column=1, padx=10, pady=10, sticky="w")

file_extension_label = ttk.Label(root, text="File Extension:")
file_extension_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")

file_extensions = ["mp4", "webm", "mkv"]
file_extension_var = tk.StringVar()
file_extension_dropdown = ttk.Combobox(root, textvariable=file_extension_var, values=file_extensions, state="readonly", style="TCombobox")
file_extension_dropdown.set("mp4")
file_extension_dropdown.grid(row=3, column=1, padx=10, pady=10, sticky="w")

audio_format_label = ttk.Label(root, text="Audio Format:")
audio_format_label.grid(row=4, column=0, padx=10, pady=10, sticky="e")

audio_formats = ["mp3"]
audio_format_var = tk.StringVar()
audio_format_entry = ttk.Combobox(root, textvariable=audio_format_var, values=audio_formats, state="readonly", style="TCombobox")
audio_format_entry.set("mp3")
audio_format_entry.grid(row=4, column=1, padx=10, pady=10, sticky="w")

convert_var = tk.BooleanVar()
convert_checkbox = ttk.Checkbutton(root, text="Convert to audio", variable=convert_var, command=convert_checkbox_changed)
convert_checkbox.grid(row=5, column=0, padx=10, pady=10)

playlist_var = tk.BooleanVar()
playlist_checkbox = ttk.Checkbutton(root, text="Download Playlist", variable=playlist_var)
playlist_checkbox.grid(row=5, column=1, padx=10, pady=10)

hide_gui_var = tk.BooleanVar()
hide_gui_checkbox = ttk.Checkbutton(root, text="Hide GUI during download", variable=hide_gui_var)
hide_gui_checkbox.grid(row=5, column=2, padx=10, pady=10)

audio_only_var = tk.BooleanVar()
audio_only_checkbox = ttk.Checkbutton(root, text="Audio Only", variable=audio_only_var)
audio_only_checkbox.grid(row=6, column=0, padx=10, pady=10)

subtitle_var = tk.BooleanVar()
subtitle_checkbox = ttk.Checkbutton(root, text="Download Subtitles", variable=subtitle_var)
subtitle_checkbox.grid(row=6, column=1, padx=10, pady=10)

thumbnail_var = tk.BooleanVar()
thumbnail_checkbox = ttk.Checkbutton(root, text="Download Video Thumbnail", variable=thumbnail_var)
thumbnail_checkbox.grid(row=6, column=2, padx=10, pady=10)

metadata_var = tk.BooleanVar()
metadata_checkbox = ttk.Checkbutton(root, text="Download Video Metadata", variable=metadata_var)
metadata_checkbox.grid(row=7, column=0, padx=10, pady=10)

download_btn = ttk.Button(root, text="Download", command=download_thread)
download_btn.grid(row=10, column=0, columnspan=2, pady=20)

status_label = ttk.Label(root, text="", font=("Helvetica", 12))
status_label.grid(row=11, column=0, columnspan=2, pady=10)

root.mainloop()

