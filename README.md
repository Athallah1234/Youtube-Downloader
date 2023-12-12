# YouTube Downloader

YouTube Downloader is a simple and user-friendly Python application that allows you to download YouTube videos and playlists with ease. The application provides a graphical user interface (GUI) built using the Tkinter library and incorporates features such as selecting video resolution, choosing a download path, converting videos to MP3, downloading metadata, thumbnails, subtitles, and more.

## Advanced Features

- **HDR Video Support:** The application automatically detects and downloads HDR streams when available.
- **Smart Stream Selection:** Utilizes intelligent stream selection, including VR and 360 streams, for an enhanced download experience.

## Features

- **User-Friendly Interface:** The application provides a straightforward and easy-to-use interface for downloading YouTube videos and playlists.
- **Resolution Options:** Users can select their preferred video resolution (720p, 480p, 360p) for downloads.
- **Video Format Options:** Choose between popular video formats such as MP4, WebM, and MKV.
- **Additional Options:** Customize your download experience with options like converting videos to MP3, downloading metadata, thumbnails, and subtitles.
- **Batch Download:** Download multiple videos by entering comma-separated URLs for efficient batch downloading.

## Requirements

- Python 3.x
- Required Python packages: tkinter, pytube, moviepy, requests, plyer

## How to Use

1. **Clone the Repository:**
   `` bash
   git clone https://github.com/your_username/youtube-downloader.git
   cd youtube-downloader
   ``
2. **Install Dependencies:**
   `` bash
   pip install -r requirements.txt
   ``
3. **Run the Application:**
   `` bash
   python youtube_downloader.py
   ``
4. **Use the GUI:**
   - Enter the YouTube video or playlist URL.
   - Select your preferred resolution and video format.
   - Choose additional options (convert to MP3, download metadata, thumbnail, subtitle, playlist).
   - Click "Download" to start the download process.
5. **Batch Download:**
   - Enter multiple URLs separated by commas in the Batch Download section.
   - Configure other options.
   - Click "Batch Download" to download multiple videos simultaneously.
  
## Troubleshooting

- **Video Unavailability:** If an error occurs due to video unavailability or deletion, the application provides informative error messages to guide users.
- **Invalid URLs:** The application validates entered URLs and notifies users if an invalid YouTube URL is provided.
- **Secure URL Check:** Ensures users enter secure HTTP or HTTPS URLs, enhancing the security of the download process.

## Known Issues

- **Age-Restricted Videos:** The application does not currently support downloading age-restricted videos due to YouTube's policy restrictions.

## Future Enhancements

- **User Authentication:** Consider implementing user authentication for access to restricted content.
- **Improved Error Handling:** Enhance error handling to provide more detailed information on encountered issues.

## Contributors

Contributions to the project are welcome! If you find a bug, have a feature request, or would like to contribute to the project, please follow our Contribution Guidelines.

## Support

If you encounter any issues or have questions, feel free to [open an issue](). We appreciate your feedback and will do our best to assist you.

## Acknowledgments

We would like to express our gratitude to the open-source community and the developers of the libraries and tools used in this project.

## Disclaimer

This application is intended for personal use only. Ensure that you comply with YouTube's terms of service and respect the intellectual property rights of content creators.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.
