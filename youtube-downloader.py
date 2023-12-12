import os
import platform
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pytube import YouTube, Playlist
from moviepy.editor import VideoFileClip
import requests
import threading
import re
from plyer import notification

class YouTubeDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Downloader")

        self.url_label = ttk.Label(root, text="Enter YouTube URL or Playlist URL:")
        self.url_entry = ttk.Entry(root, width=50)
        self.resolution_label = ttk.Label(root, text="Select Resolution:")
        self.resolution_combobox = ttk.Combobox(root, values=["720p", "480p", "360p"], state="readonly")
        self.resolution_combobox.set("720p")  # default resolution
        self.video_extension_label = ttk.Label(root, text="Select Video Extension:")
        self.video_extension_combobox = ttk.Combobox(root, values=["mp4", "webm", "mkv"], state="readonly")
        self.video_extension_combobox.set("mp4")  # default video extension
        self.download_path_label = ttk.Label(root, text="Download Path:")
        self.download_path_entry = ttk.Entry(root, width=40, state="readonly")
        self.browse_button = ttk.Button(root, text="Browse", command=self.browse_path)
        self.convert_to_mp3_var = tk.BooleanVar()
        self.convert_to_mp3_checkbox = ttk.Checkbutton(root, text="Convert to MP3", variable=self.convert_to_mp3_var)
        self.download_metadata_var = tk.BooleanVar()
        self.download_metadata_checkbox = ttk.Checkbutton(root, text="Download Metadata", variable=self.download_metadata_var)
        self.download_thumbnail_var = tk.BooleanVar()
        self.download_thumbnail_checkbox = ttk.Checkbutton(root, text="Download Thumbnail", variable=self.download_thumbnail_var)
        self.download_subtitle_var = tk.BooleanVar()
        self.download_subtitle_checkbox = ttk.Checkbutton(root, text="Download Subtitle", variable=self.download_subtitle_var)
        self.download_playlist_var = tk.BooleanVar()
        self.download_playlist_checkbox = ttk.Checkbutton(root, text="Download Playlist", variable=self.download_playlist_var)
        self.download_button = ttk.Button(root, text="Download", command=self.download_video_threaded)

        self.batch_download_label = ttk.Label(root, text="Batch Download (comma-separated URLs):")
        self.batch_download_entry = ttk.Entry(root, width=50)
        self.batch_download_button = ttk.Button(root, text="Batch Download", command=self.batch_download_videos_threaded)

        self.setup_layout()

    def setup_layout(self):
        # Positioning elements using grid
        self.url_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.url_entry.grid(row=0, column=1, columnspan=2, padx=10, pady=10, sticky="ew")
        self.resolution_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.resolution_combobox.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky="ew")
        self.video_extension_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.video_extension_combobox.grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky="ew")
        self.download_path_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.download_path_entry.grid(row=3, column=1, padx=10, pady=10, sticky="ew")
        self.browse_button.grid(row=3, column=2, padx=10, pady=10)
        self.convert_to_mp3_checkbox.grid(row=8, column=0, columnspan=3, pady=10)
        self.download_metadata_checkbox.grid(row=9, column=0, columnspan=3, pady=10)
        self.download_thumbnail_checkbox.grid(row=10, column=0, columnspan=3, pady=10)
        self.download_subtitle_checkbox.grid(row=11, column=0, columnspan=3, pady=10)
        self.download_playlist_checkbox.grid(row=12, column=0, columnspan=3, pady=10)
        self.download_button.grid(row=13, column=0, columnspan=3, pady=10)

        # Batch Download elements
        self.batch_download_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.batch_download_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky="ew")
        self.batch_download_button.grid(row=14, column=0, columnspan=3, pady=10)


    def browse_path(self):
        download_path = filedialog.askdirectory()
        self.download_path_entry.configure(state="normal")
        self.download_path_entry.delete(0, tk.END)
        self.download_path_entry.insert(0, download_path)
        self.download_path_entry.configure(state="readonly")

    def has_hdr_stream(self, yt):
        streams = yt.streams
        for stream in streams:
            # Check if the stream has the 'abr' attribute (audio bitrate)
            if hasattr(stream, 'abr') and stream.abr is not None and "hdr" in stream.abr.lower():
                return True
        return False
    
    def get_vr_stream(self, yt, resolution):
        # Pilih stream VR jika tersedia
        vr_stream = yt.streams.filter(file_extension="mp4", resolution=resolution, type="vr").first()
        if vr_stream:
            return vr_stream
        else:
            return None

    def get_360_stream(self, yt, resolution):
        # Pilih stream 360 jika tersedia
        stream_360 = yt.streams.filter(file_extension="mp4", resolution=resolution, type="360").first()
        if stream_360:
            return stream_360
        else:
            return None


    # New method for URL validation
    def validate_url(self, url):
        if not re.match(r'^(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/', url):
            self.update_status("Please enter a valid YouTube URL.")
            return False

        # Validate that the URL uses either HTTP or HTTPS
        if not url.startswith("http://") and not url.startswith("https://"):
            self.update_status("Please use a secure HTTP or HTTPS URL.")
            return False

        return True
    
    def validate_resolution(self, resolution):
        if resolution not in ["720p", "480p", "360p"]:
            self.update_status("Please select a valid resolution.")
            return False
        return True

    # New method for directory validation
    def validate_directory(self, directory):
        if not os.path.isdir(directory):
            self.update_status("Please select a valid download directory.")
            return False

        return True

    def download_video(self):
        url = self.url_entry.get()
        resolution = self.resolution_combobox.get()
        download_path = self.download_path_entry.get()
        convert_to_mp3 = self.convert_to_mp3_var.get()
        download_metadata = self.download_metadata_var.get()
        download_thumbnail = self.download_thumbnail_var.get()
        download_subtitle = self.download_subtitle_var.get()
        download_playlist = self.download_playlist_var.get()

        if not self.validate_resolution(resolution):
            return

        if url and resolution and download_path:
            if not self.validate_url(url):
                return
            if not self.validate_directory(download_path):
                return
            try:
                self.update_status("Downloading...")
                if download_playlist and "playlist" in url.lower():
                    playlist = Playlist(url)
                    self.download_playlist(playlist, download_path, resolution, convert_to_mp3, download_metadata, download_thumbnail, download_subtitle)
                else:
                    yt = YouTube(url)
                    self.download_single_video(yt, download_path, resolution, convert_to_mp3, download_metadata, download_thumbnail, download_subtitle)

                self.update_status("Download Completed!")
            except Exception as e:
                self.update_status("Error occurred: " + str(e))
        else:
            self.update_status("Please enter a valid URL, choose a resolution, and select a download path.")

    def download_single_video(self, yt, download_path, resolution, convert_to_mp3, download_metadata, download_thumbnail, download_subtitle):
        try:
            if self.has_hdr_stream(yt):
                video = yt.streams.filter(file_extension="mp4", resolution=resolution, hdr=True).first()
            else:
                video_streams = yt.streams.filter(progressive=True, file_extension="mp4", resolution=resolution)
                high_frame_rate_stream = None
                for stream in video_streams:
                    if stream.fps and stream.fps > 30:
                        high_frame_rate_stream = stream
                        break
                video = high_frame_rate_stream or video_streams.first()

                if not video:
                    self.update_status("Error: Video is unavailable or has been deleted.")
                    return

                video_path = video.download(download_path)

                if convert_to_mp3:
                    self.convert_to_mp3(video_path)
                    os.remove(video_path)  # Hapus file video

                if download_metadata:
                    self.download_metadata(yt, download_path)

                if download_thumbnail:
                    self.download_thumbnail(yt, download_path)

                if download_subtitle:
                    self.download_subtitle(yt, download_path)

                if self.has_hdr_stream(yt):
                    self.update_status("HDR stream detected. Downloading HDR video...")

        except Exception as e:
            error_message = str(e)
            if "Video unavailable" in error_message:
                self.update_status("Error: Video is unavailable or has been deleted.")
            else:
                self.update_status("Error occurred: " + error_message, is_error=True)

    def download_playlist(self, playlist, download_path, resolution, convert_to_mp3, download_metadata, download_thumbnail, download_subtitle):
        for video_url in playlist.video_urls:
            try:
                yt = YouTube(video_url)
                self.download_single_video(yt, download_path, resolution, convert_to_mp3, download_metadata, download_thumbnail, download_subtitle)
            except Exception as e:
                messagebox.showwarning("Warning", f"Skipped video: {video_url}\nError: {str(e)}")

    def convert_to_mp3(self, video_path):
        mp3_path = os.path.splitext(video_path)[0] + ".mp3"
        video_clip = VideoFileClip(video_path)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(mp3_path)
        audio_clip.close()
        video_clip.close()

    def download_metadata(self, yt, download_path):
        metadata_file_path = os.path.join(download_path, f"{yt.title}.txt")
        with open(metadata_file_path, "w", encoding="utf-8") as metadata_file:
            metadata_file.write("Video Title: {}\n".format(yt.title))
            metadata_file.write("Video Author: {}\n".format(yt.author))
            metadata_file.write("Video Length: {} seconds\n".format(yt.length))
            metadata_file.write("Video Views: {}\n".format(yt.views))
            metadata_file.write("Video Rating: {}\n".format(yt.rating))
            metadata_file.write("Video URL: {}\n".format(yt.watch_url))
            metadata_file.write("Video Description:\n{}\n".format(yt.description))
            metadata_file.write("Video Thumbnail URL: {}\n".format(yt.thumbnail_url))
            metadata_file.write("Video Publish Date: {}\n".format(yt.publish_date))
            metadata_file.write("Video Keywords: {}\n".format(", ".join(yt.keywords)))
            metadata_file.write("Video Age Restriction: {}\n".format(yt.age_restricted))
            metadata_file.write("Video Caption Tracks: {}\n".format(yt.caption_tracks))
            metadata_file.write("Video Captions: {}\n".format(yt.captions))
            metadata_file.write("Video Length (hh:mm:ss): {}\n".format(yt.length))
            metadata_file.write("Video Live Broadcast: {}\n".format(yt.is_live))
            metadata_file.write("Video Live Broadcast Content: {}\n".format(yt.live_broadcast_content))
            metadata_file.write("Video Live Broadcast Start: {}\n".format(yt.live_broadcast_start))
            metadata_file.write("Video Categories: {}\n".format(", ".join(yt.categories)))  # Add categories
            metadata_file.write("Video Channel ID: {}\n".format(yt.channel_id))  # Add channel ID

    def download_thumbnail(self, yt, download_path):
        thumbnail_url = yt.thumbnail_url
        thumbnail_path = os.path.join(download_path, f"{yt.title}_thumbnail.jpg")
        thumbnail_data = requests.get(thumbnail_url).content
        with open(thumbnail_path, "wb") as thumbnail_file:
            thumbnail_file.write(thumbnail_data)

    def download_subtitle(self, yt, download_path):
        subtitle_tracks = yt.captions
        for track in subtitle_tracks.values():
            subtitle_path = os.path.join(download_path, f"{yt.title}_{track.code}_subtitle.srt")
            with open(subtitle_path, "w", encoding="utf-8") as subtitle_file:
                subtitle_file.write(track.generate_srt_captions())

    def batch_download_videos(self):
        urls = self.batch_download_entry.get().split(',')
        resolution = self.resolution_combobox.get()
        download_path = self.download_path_entry.get()
        convert_to_mp3 = self.convert_to_mp3_var.get()
        download_metadata = self.download_metadata_var.get()
        download_thumbnail = self.download_thumbnail_var.get()
        download_subtitle = self.download_subtitle_var.get()
        download_playlist = self.download_playlist_var.get()

        # Additional validation checks
        if not self.validate_resolution(resolution):
            return

        if all(url.strip() for url in urls) and resolution and download_path:
            for url in urls:
                if not self.validate_url(url.strip()):
                    return
            if not self.validate_directory(download_path):
                return
            try:
                self.update_status("Batch Downloading...")
                for url in urls:
                    url = url.strip()
                    if download_playlist and "playlist" in url.lower():
                        playlist = Playlist(url)
                        self.download_playlist(playlist, download_path, resolution, convert_to_mp3, download_metadata, download_thumbnail, download_subtitle)
                    else:
                        yt = YouTube(url)
                        self.download_single_video(yt, download_path, resolution, convert_to_mp3, download_metadata, download_thumbnail, download_subtitle)

                self.update_status("Batch Download Completed!")
            except Exception as e:
                self.update_status("Error occurred: " + str(e))
        else:
            self.update_status("Please enter valid URLs, choose a resolution, and select a download path.")

    def update_status(self, message, is_error=False):
        if is_error:
            messagebox.showerror("Error", message)
        else:
            messagebox.showinfo("Status", message)
            notification_title = "YouTube Downloader"
            notification_text = message
            notification.notify(
                title=notification_title,
                message=notification_text,
                app_icon=None,
                timeout=10,
        )

    def download_video_threaded(self):
        threading.Thread(target=self.download_video).start()

    def batch_download_videos_threaded(self):
        threading.Thread(target=self.batch_download_videos).start()

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeDownloaderApp(root)
    root.resizable(width=False, height=False)
    root.mainloop()

