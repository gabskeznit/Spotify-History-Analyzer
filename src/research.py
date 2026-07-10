from statistics import *
import pandas as pd


def search_track(df, track):

    result = df[df["track"].str.lower() == track.lower()]

    if result.empty:
        print("Música não encontrada.")
        return

    print("=" * 45)

    print(result.iloc[0]["track"])

    print("=" * 45)

    print()

    print(f"Artista: {result.iloc[0]['artist']}")

    print(f"Álbum: {result.iloc[0]['album']}")

    print()

    print(f"Total de plays: {len(result)}")

    print()

    print("Primeira reprodução:")

    print(result["timestamp"].min())

    print()

    print("Última reprodução:")

    print(result["timestamp"].max())

    print()

    print("Tempo médio ouvido:")

    media = result["duration_ms"].mean() / 1000

    print(f"{media:.1f} segundos")

    print()

    print("Plataformas")

    print(result["platform"].value_counts())

    print()

    print("Shuffle")

    print(result["shuffle"].value_counts())

    print()

    print("Offline")

    print(result["offline"].value_counts())

    print()

    print("País")

    print(result["country"].value_counts())

    print()

    print("Reason End")

    print(result["reason_end"].value_counts())

    print()

    print("Reason Start")

    print(result["reason_start"].value_counts())