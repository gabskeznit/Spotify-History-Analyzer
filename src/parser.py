import json
from pathlib import Path

import pandas as pd


MIN_PLAY_TIME = 30000


def load_history(folder="data"):

    folder = Path(folder)

    files = sorted(folder.glob("Streaming_History_Audio_*.json"))

    if not files:
        raise FileNotFoundError("Nenhum arquivo Streaming_History encontrado.")

    rows = []

    for file in files:

        with open(file, encoding="utf-8") as f:
            data = json.load(f)

        for item in data:

            # ignora podcasts
            if item["master_metadata_track_name"] is None:
                continue

            # mínimo de 30 segundos
            if item["ms_played"] < MIN_PLAY_TIME:
                continue

            # músicas puladas
            if item["skipped"]:
                continue

            # terminou normalmente
            if item["reason_end"] != "trackdone":
                continue

            rows.append({

                "timestamp": item["ts"],

                "artist": item["master_metadata_album_artist_name"],

                "track": item["master_metadata_track_name"],

                "album": item["master_metadata_album_album_name"],

                "track_uri": item["spotify_track_uri"],

                "duration_ms": item["ms_played"],

                "platform": item["platform"],

                "country": item["conn_country"],

                "reason_start": item["reason_start"],

                "reason_end": item["reason_end"],

                "shuffle": item["shuffle"],

                "offline": item["offline"],

                "offline_timestamp": item["offline_timestamp"]

            })

    df = pd.DataFrame(rows)

    df["timestamp"] = pd.to_datetime(df["timestamp"])

    return df