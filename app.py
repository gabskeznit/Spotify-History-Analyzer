from src.parser import load_history
import src.stats as stats

from src.utils import print_header

from src.utils import format_total_time

print_header("Spotify History Analyzer")

print()

print("Lendo histórico...")

df = load_history("data")

print(f"OK! ({len(df):,} reproduções carregadas)")

print(f"Reproduções: {stats.total_tracks(df):,}")

print(f"Músicas únicas: {stats.unique_tracks(df):,}")

print(f"Artistas únicos: {stats.unique_artists(df):,}")

print(f"Álbuns únicos: {stats.unique_albums(df):,}")

print()

tempo = format_total_time(df["duration_ms"].sum())
print(f"Tempo ouvindo música: {tempo}")

print()

print("=" * 45)

print("TOP 10 ARTISTAS")

print("=" * 45)

print(stats.top_artists(df))

print()

print("=" * 45)

print("TOP 10 MÚSICAS")

print("=" * 45)

print(stats.top_tracks(df))

print()

print("=" * 45)

print("TOP 10 ÁLBUNS")

print("=" * 45)

print(stats.top_albums(df))
