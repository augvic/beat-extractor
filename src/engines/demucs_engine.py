import subprocess

class DemucsEngine:
    
    def extract_beat(self, song_path: str) -> None:
        subprocess.run(
            [
                "python",
                "-m",
                "demucs",
                "--two-stems=vocals",
                song_path
            ]
        )

