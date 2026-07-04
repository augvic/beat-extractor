from os import path, makedirs
import sys

class Config:
    
    def __init__(self) -> None:
        if getattr(sys, "frozen", False):
            self.root_path = path.abspath(path.dirname(sys.executable))
        else:
            self.root_path = path.abspath(path.join(path.dirname(__file__), ".."))
        self.beats_path = path.abspath(path.join(self.root_path, "beats"))
        self.separated_path = path.abspath(path.join(self.root_path, "separated"))
        makedirs(self.beats_path, exist_ok=True)
