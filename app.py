from parser import load_history
import statistics as stats

print("=" * 45)
print("Spotify History Analyzer")
print("=" * 45)

print()

print("Lendo histórico...")

df = load_history("data")

print("OK!\n")

print(f"Reproduções: {stats.total_tracks(df):,}")

print(f"Músicas únicas: {stats.unique_tracks(df):,}")

print(f"Artistas únicos: {stats.unique_artists(df):,}")

print(f"Álbuns únicos: {stats.unique_albums(df):,}")

dias, horas, minutos = stats.listening_time(df)

print()

print(f"Tempo ouvindo música: {dias} dias {horas} horas {minutos} minutos")

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