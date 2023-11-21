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
A: Make sure you have Python installed. Open a terminal, navigate to the project directory, and run the script using `python youtube_downloader.py`. You may need to use `python3` instead of `python` on some systems.

### Q: Can I run this script on Windows?
A: Yes, the script is compatible with Windows. Ensure you have Python installed, open a command prompt, navigate to the project directory, and run the script using `python youtube_downloader.py`.

### Q: Is there a limit to the length of the video I can download?
A: The script doesn't impose a specific limit on video length. However, extremely long videos may take longer to download, and you may experience performance issues with very large files.

### Q: How can I download videos with subtitles?
A: Currently, the script doesn't support downloading subtitles. This feature is planned for a future update.

### Q: Does the script work with YouTube videos only?
A: Yes, the script is specifically designed for downloading videos from YouTube. It may not work with other video platforms.

### Q: Why does the script throw an error sometimes?
A: Errors can occur due to changes in the YouTube website structure. If you encounter persistent issues, check for updates in the script or report the problem on the [Issues](https://github.com/Athallah1234/Youtube-Downloader/issues) page.

## Author

[Athallahra](https://github.com/Athallah1234)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have further questions or need assistance, feel free to reach out:

- Email: your.email@example.com
- Instagram : [@athallahrajendrapj123](https://instagram.com/athallahrajendrapj123)

Your support is greatly appreciated!
