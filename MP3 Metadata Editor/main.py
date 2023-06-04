from ROOT_PATH import root_path
from os import listdir
from os import path as os_path
from pathlib import Path
from typing import List, Tuple

import pydub as pd
from pydub import utils


abs_path_to_src_folder: str = str(Path(root_path, "./merger/").resolve())
files: List[str] = listdir(abs_path_to_src_folder)
exts: List[str] = [os_path.splitext(file)[1] for file in files]
accepted_img_exts: List[str] = [".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff"]
if (
    len(files) == 2 and ".mp3" in exts and any(x in accepted_img_exts for x in exts)
) or (len(files) == 1 and ".mp3" in exts):
    audio_file: pd.AudioSegment | None = None
    img_path: str | None = None
    for file in files:
        file_name_with_ext: Tuple[str, str] = os_path.splitext(file)
        if file_name_with_ext[1] == ".mp3":
            audio_file = pd.AudioSegment.from_mp3(
                str(Path(abs_path_to_src_folder, f"./{file}").resolve())
            )
        else:
            img_path = str(Path(abs_path_to_src_folder, f"./{file}").resolve())
    if audio_file is not None:
        title: str = input("Title: ")
        track: str = input("Track: ")
        artist: str = input("Artist: ")
        album: str = input("Album: ")
        audio_file.export(
            str(Path(abs_path_to_src_folder, f"./{title}.mp3").resolve()),
            "mp3",
            tags={
                "title": title,
                "track": track,
                "artist": artist,
                "album": album,
            },
            id3v2_version="3",
            cover=img_path,
        )
else:
    print("Invalid amount of files in folder!")
