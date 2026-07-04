from ..engines.demucs_engine import DemucsEngine
from ..engines.song_downloader import SongDownloader
from ..config import Config
import os
import shutil

class ExtractBeat:

    def __init__(self,
        config: Config,
        demucs_engine: DemucsEngine,
        song_downloader: SongDownloader
    ) -> None:
        self.config = config 
        self.demucs_engine = demucs_engine
        self.song_downloader = song_downloader

    def execute(self, url: str) -> None:
        song_name = self.song_downloader.download(url)
        self.demucs_engine.extract_beat(f"{self.config.beats_path}/{song_name}.webm")
        shutil.move(f"{self.config.separated_path}/htdemucs/{song_name}/no_vocals.wav", f"{self.config.beats_path}/{song_name}.wav")
        shutil.rmtree(self.config.separated_path)
        os.remove(f"{self.config.beats_path}/{song_name}.webm")

