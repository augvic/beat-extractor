from ..tasks import ExtractBeat

class Cli:
    
    def __init__(self, extract_beat: ExtractBeat) -> None:
        self.extract_beat = extract_beat

    def run(self) -> None:
        url = input("Music URL: ")
        self.extract_beat.execute(url)

