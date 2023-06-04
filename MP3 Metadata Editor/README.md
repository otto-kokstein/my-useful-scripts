# MP3 Metadata Editor

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A Python script used for editing the information (metadata) and the image embedded in a .mp3 file.

## Requirements:
You will need to install the library [pydub](https://github.com/jiaaro/pydub "Pydub's GitHub Page").

Installation with pip: `pip install pydub`

You will also need to download [FFmpeg](https://www.gyan.dev/ffmpeg/builds "FFmpeg for Windows") and add its directory to your system's PATH.

## Usage:
Put the .mp3 file in the "merger" folder. (You may need to create it yourself.)

Optionally, also put the cover image you want to embed in the .mp3 file into the folder.

Do not put anything else into the folder, else the script will fail.

Start application with `python main.py`.
