from yt_dlp import YoutubeDL
from pathlib import Path


class YTDWrapper:
    def __init__(self, dl_dir=None):
        self.dl_dir = dl_dir or Path.home() / "Downloads"

        self.base_opts = {
            "outtmpl": str(self.dl_dir / "%(title)s.%(ext)s"),
            "embedthumbnail": True,
            "addmetadata": True,
        }

        self.ydl_opts = self.base_opts.copy()

    def audio_only(self, out_format="bestaudio"):
        self.ydl_opts = {
            **self.base_opts,
            "format": out_format,
        }

    def video_only(self, out_format="bestvideo"):
        self.ydl_opts = {
            **self.base_opts,
            "format": out_format,
        }

    def merged(self, out_format="mkv"):
        self.ydl_opts = {
            **self.base_opts,
            "format": "bestaudio+bestvideo",
            "merge_output_format": out_format,
        }

    def start_downloader(self, url: str):
        with YoutubeDL(self.ydl_opts) as ydl:
            ydl.download([url])

        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)

        return filename  # returns path/name
