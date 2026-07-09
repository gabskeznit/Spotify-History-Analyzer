import json
from pathlib import Path
import pandas as pd


def load_history(folder="data"):

    folder = Path(folder)

    files = sorted(folder.glob("Streaming_History_Audio_*.json"))

    if not files:
        raise FileNotFoundError("Nenhum histórico encontrado.")

    rows = []

    for file in files:

        with open(file, encoding="utf-8") as f:

            data = json.load(f)

        for item in data:

            # ignora podcasts
            if item["master_metadata_track_name"] is None:
                continue

            # ignora músicas curtas
            if item["ms_played"] < 30000:
                continue

            rows.append({

                "timestamp": item["ts"],

                "artist": item["master_metadata_album_artist_name"],

                "track": item["master_metadata_track_name"],

                "album": item["master_metadata_album_album_name"],

                "duration_ms": item["ms_played"]

            })

    df = pd.DataFrame(rows)

    df["timestamp"] = pd.to_datetime(df["timestamp"])

    return df