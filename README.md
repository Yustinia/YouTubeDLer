# YouTube Downloader

A downloader and converter wrapper using ytdlp to download and ffmpeg for additional processing.

# Prerequisites

The following packages are needed to use the CLI wrapper.

- python
- pip
- ytdlp
- ffmpeg

# Installation

1. Start by using `git clone` to clone the repo to your system.

2. Ensure that you have pip installed, else download and install it.

3. Use `pip install -r requirements.txt` to download the necessary packages

# Usage

1. Inside the cloned repo, `python main.py`.

2. Provide the link. It accepts the following domains:

    - youtube.com
    - youtu.be
    - music.youtube.com

3. Choose the download option you need:

    1. Audio Only - Only downloads the audio with the best quality.
    2. Video Only - Only download the video with the best quality.
    3. Merged - Downloads both and merges it to a `.mkv` container.

4. Optional: Additional post-processing using ffmpeg:

    1. Compress - Reduce the file size approximately to your given size.
    2. Cut - Slice a segment of the source.
    3. Convert - Convert the download to a different format entirely.

5. Locate the downloaded/processed file in your *"Downloads"* home directory.

# Disclaimer

The tool **does not** touch nor interact with user and system files other than the working directory of the tool. All downloaded/processed files outputs to *"Downloads"* and nowhere else.

# License

This small project is licensed under *The Unlicense*.

It depends on:

- ytdlp
- ffmpeg

Refer to their respective repositories for more information about their license.
