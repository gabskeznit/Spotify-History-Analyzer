# Spotify-History-Analyzer

Analyze your complete Spotify Streaming History using the official Spotify Extended Streaming History export.

Spotify History Analyzer is an open-source Python application that helps you explore, search and analyze your complete Spotify listening history locally.

---

## ✨ Features

- 📊 General listening statistics
- 🎵 Top Tracks
- 🎤 Top Artists
- 💿 Top Albums
- ⏱️ Total listening time
- 📁 Multi-file Spotify history support
- 🔍 Research Mode
- ⚡ Fast local analysis using Pandas

---

## 📸 Preview

```text
=============================================
Spotify History Analyzer
=============================================

Loading history...
OK!

Tracks Played: 18,155
Unique Tracks: 2,377
Unique Artists: 694
Unique Albums: 1,372

Listening Time:
40 days 23 hours 21 minutes

=============================================
TOP ARTISTS
=============================================

MHRAP
Matuê
7 Minutoz
Kanye West
Veigh
...
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/gabskeznit/Spotify-History-Analyzer.git

cd Spotify-History-Analyzer
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

## 📂 Export your Spotify History

Request your **Extended Streaming History** directly from Spotify.

After receiving your data, place every file like:

```text
Streaming_History_Audio_*.json
```

inside the `data/` folder.

Example:

```text
data/

Streaming_History_Audio_2022.json
Streaming_History_Audio_2023.json
Streaming_History_Audio_2024.json
Streaming_History_Audio_2025.json
Streaming_History_Audio_2026.json
Streaming_History_Audio_*.json
```

---

## ▶ Usage

General statistics:

```bash
python app.py
```

Research mode:

```bash
python research_app.py
```

---

## 📁 Project Structure

```text
Spotify-History-Analyzer/

app.py
research_app.py

src/
│
├── parser.py
├── stats.py
├── research.py
├── utils.py
├── constants.py
└── __init__.py

data/

requirements.txt
README.md
LICENSE
```

---

## 🛣 Roadmap

### ✅ v0.1

- JSON Parser
- Statistics
- Top Artists
- Top Tracks
- Top Albums

### ✅ v0.2

- Better project structure
- Research module
- Utilities module
- Constants module
- Cleaner architecture

### 🚧 v0.3

- Artist Search
- Album Search
- Better Track Search
- First/Last Play
- Listening Time per Artist
- Shuffle statistics
- Offline/Online statistics

### 🔮 Future

- Spotify Wrapped Generator
- Timeline Visualization
- Charts
- Streamlit Dashboard
- Stats.fm Comparison
- Last.fm Export
- Web Version

---

## 🤝 Contributing

Contributions, suggestions and ideas are always welcome.

Feel free to open an Issue or submit a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 🤔 Why?

Spotify provides users with their complete listening history, but there are very few tools capable of fully exploring that data.

Spotify History Analyzer was created to provide an easy, fast and open-source way to analyze your listening history locally using the official Spotify export.
