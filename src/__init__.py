from .config import Config
from .engines import DemucsEngine, SongDownloader
from .tasks import ExtractBeat
from .interactions.cli import Cli

class BeatExtractor:
    
    def __init__(self) -> None:
        self.config = Config()
        self.demucs_engine = DemucsEngine()
        self.song_downloader = SongDownloader(self.config.beats_path)
        self.extract_beat = ExtractBeat(self.config, self.demucs_engine, self.song_downloader)
        self.cli = Cli(self.extract_beat)
    
    def run(self) -> None:
        self.cli.run()

