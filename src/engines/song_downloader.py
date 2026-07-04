import yt_dlp
from pathlib import Path

class SongDownloader:
    
    def __init__(self, output_folder: str) -> None:
        self.output_folder = output_folder
    
    def download(self, url: str) -> str:
        with yt_dlp.YoutubeDL({
            "format": "bestaudio",
            "outtmpl": f"{self.output_folder}/%(title)s.%(ext)s",
            "verbose": True
        }) as ydl:
            info = ydl.extract_info(url, download=True)
            output_path = ydl.prepare_filename(info)
            song_name = Path(output_path).stem
            return song_name 

