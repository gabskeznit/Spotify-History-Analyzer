import pandas as pd


def total_tracks(df):

    return len(df)


def unique_tracks(df):

    return df["track"].nunique()


def unique_artists(df):

    return df["artist"].nunique()


def unique_albums(df):

    return df["album"].nunique()


def listening_time(df):

    total = df["duration_ms"].sum() // 1000

    days = total // 86400

    total %= 86400

    hours = total // 3600

    total %= 3600

    minutes = total // 60

    return days, hours, minutes


def top_artists(df, n=10):

    return df["artist"].value_counts().head(n)


def top_tracks(df, n=10):

    return df.groupby(["artist", "track"]).size().sort_values(ascending=False).head(n)


def top_albums(df, n=10):

    return df.groupby(["artist", "album"]).size().sort_values(ascending=False).head(n)