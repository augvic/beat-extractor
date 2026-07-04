# 🎵 Beat Extractor

Download a song from YouTube and extract its instrumental (no-vocals) track using Demucs AI source separation. 🎧

## ⚙️ How it works

1. ⬇️ Downloads the best audio stream from a YouTube URL via `yt-dlp`
2. 🧠 Runs Demucs (`htdemucs` model) with `--two-stems=vocals` to separate vocals from the instrumental
3. 💾 Saves the resulting `no_vocals.wav` to the `resources/` directory

## 📋 Requirements

- 🐍 Python 3.14+
- 🚀 CUDA-capable GPU recommended (falls back to CPU)

## 🚀 Usage

```bash
python main.py
```

Or:

```bash
python -m src
```

You will be prompted for a URL:

```
Music URL:
```

The extracted instrumental is saved to `resources/<title>.wav`.

## 📦 Building standalone executable

```bash
pyinstaller make.spec
```
