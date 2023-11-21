# YouTube Downloader

This is a simple YouTube downloader script built using Python and Tkinter for the user interface. It allows you to download YouTube videos and optionally convert them to MP3 format. The script uses the Pytube library for YouTube video downloading and the MoviePy library for video to MP3 conversion.

## Features

- Download YouTube videos with specified resolution.
- Optional conversion to MP3 format.
- User-friendly Tkinter GUI.

## Prerequisites

Make sure you have the following dependencies installed:

- Python 3.x
- Pytube library: `pip install pytube`
- MoviePy library: `pip install moviepy`

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/youtube-downloader.git
    cd youtube-downloader
    ```

2. Run the script:

    ```bash
    python run.py
    ```

3. Enter the YouTube URL, select the save path, choose optional settings, and click the "Download" button.

## Configuration

- **Resolution:** Choose the desired video resolution from the dropdown menu.
- **Convert to MP3:** Check this option to convert the downloaded video to MP3 format.

## Screenshots

Include some screenshots of your application to give users a visual representation.

## Acknowledgments

- [Pytube](https://github.com/pytube/pytube) - Python library for YouTube video downloading.
- [MoviePy](https://github.com/Zulko/moviepy) - Python library for video editing and conversion.

## Contributing

If you want to contribute to this project, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m 'Add feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

Please make sure to update tests as appropriate.

## Issues

If you encounter any issues or have suggestions, feel free to open an issue [here](https://github.com/Athallah1234/Youtube-Downloader/issues).

## Frequently Asked Questions (FAQ)

### Q: How do I specify the download location for the videos?
A: When you run the script, you will be prompted to enter the save path. Alternatively, you can provide the save path as a command-line argument when running the script.

### Q: Can I download videos in bulk or playlists?
A: Currently, the script supports downloading individual videos. Support for bulk downloads and playlists is planned for a future update.

### Q: Why am I getting an error about resolution not being available?
A: This error occurs when the selected resolution is not available for the video. Try selecting a different resolution or check the available resolutions for the video on the YouTube website.

### Q: Is there a way to track the download progress?
A: Currently, the script doesn't provide a progress bar, but it will display status messages in the GUI. Implementing a progress bar is a planned enhancement for a future update.

### Q: I encountered an issue not listed here. What should I do?
A: Please check the [Issues](https://github.com/Athallah1234/Youtube-Downloader/issues) section on GitHub. If the issue hasn't been reported, feel free to open a new issue, providing details about the problem you encountered.

### Q: What video resolutions are supported by the script?
A: The script supports resolutions such as 360p, 720p, and 1080p. You can select your desired resolution from the dropdown menu in the GUI.

### Q: How can I run the script on macOS/Linux?
A: Make sure you have Python installed. Open a terminal, navigate to the project directory, and run the script using `python run.py`. You may need to use `python3` instead of `python` on some systems.

### Q: Can I run this script on Windows?
A: Yes, the script is compatible with Windows. Ensure you have Python installed, open a command prompt, navigate to the project directory, and run the script using `python.exe run.py`.

### Q: Is there a limit to the length of the video I can download?
A: The script doesn't impose a specific limit on video length. However, extremely long videos may take longer to download, and you may experience performance issues with very large files.

### Q: How can I download videos with subtitles?
A: Currently, the script doesn't support downloading subtitles. This feature is planned for a future update.

### Q: Does the script work with YouTube videos only?
A: Yes, the script is specifically designed for downloading videos from YouTube. It may not work with other video platforms.

### Q: Can I download videos from channels or user-specific URLs?
A: Currently, the script is designed to download individual videos. Support for channel-based downloads is on the roadmap for future updates.

### Q: Can I customize the filename of the downloaded video?
A: The script uses the default video title as the filename. Future updates may include an option to customize filenames.

### Q: Does the script work with YouTube API keys?
A: No, the script does not require a YouTube API key for basic functionality. However, if you plan to contribute to the development or use advanced features, refer to the [YouTube API documentation](https://developers.google.com/youtube/v3) for information on obtaining an API key.

### Q: Why does the script need MoviePy for MP3 conversion?
A: MoviePy is a versatile video editing library that includes audio conversion functionality. It provides a simple and efficient way to extract audio from video files.

### Q: What should I do if the script stops working after a YouTube website update?
A: Check the GitHub repository for any recent updates or issues related to YouTube website changes. If necessary, create a new issue or pull request, and the community can work together to address the compatibility issue.

### Q: Is there a way to download videos without the GUI (headless mode)?
A: Headless mode is not currently supported in the script. However, you can modify the script to run in headless mode by adapting the code accordingly.

### Q: Can I use this script on my mobile device?
A: The script is designed for desktop environments and may not work seamlessly on mobile devices. Consider using a computer for the optimal experience.

### Q: Are there any plans for a command-line interface (CLI) version?
A: Yes, a CLI version is on the development roadmap for users who prefer a command-line interface. Contributions to this feature are welcome!

### Q: How can I disable the GUI and run the script in console-only mode?
A: The script currently relies on the Tkinter GUI library for user interaction. To create a console-only version, additional modifications to the code would be necessary.

### Q: Can I use a proxy to download videos?
A: The script does not currently support proxy configurations. If you require proxy functionality, consider contributing to the project or using external tools to route your internet traffic through a proxy.

### Q: Does the script work in countries where YouTube is restricted?
A: The script relies on YouTube's public APIs, and its functionality may be affected in countries where YouTube is restricted. Ensure compliance with local laws and regulations.

### Q: Can I run multiple instances of the script simultaneously?
A: Running multiple instances concurrently is possible, but exercise caution to avoid potential conflicts, especially when specifying the same download directory for multiple instances.

### Q: What video formats are supported for download?
A: The script currently supports downloading videos in the MP4 format. Support for additional formats may be considered in future updates.

### Q: How can I customize the appearance of the GUI?
A: While the current version of the script has a basic GUI, further customization options are planned for future releases. Feel free to share your suggestions or contribute to the project.

## Author

[Athallahra](https://github.com/Athallah1234)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have further questions or need assistance, feel free to reach out:

- Email: your.email@example.com
- Instagram : [@athallahrajendrapj123](https://instagram.com/athallahrajendrapj123)

Your support is greatly appreciated!
