"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    """
    Execute the music recommendation system workflow.
    This function orchestrates the complete recommendation pipeline:
    1. Loads songs from a CSV data file
    2. Defines user preferences including favorite genres, moods, audio features,
       tempo ranges, and preferred artists
    3. Generates song recommendations using a scoring algorithm
    4. Displays the top 5 recommended songs in a formatted table with:
       - Rank number and song title/artist
       - Numerical score (0-7.0) with visual progress bar
       - Song metadata (genre, mood, energy level)
       - Reasons why each song was recommended
    The scoring system awards points based on how well each song matches user
    preferences across multiple dimensions (genre, mood, audio features, artists).
    Songs are ranked by their total match score in descending order.
    Returns:
        None
    """
    songs = load_songs("data/songs.csv")
    print(f"Loaded {len(songs)} songs\n")

    user_prefs = {
        "favorite_genres": ["rock", "pop", "lofi", "jazz", "ambient"],
        "favorite_moods": ["chill", "happy", "melancholic", "energetic", "romantic"],
        "target_valence": 0.7,
        "positive_energy": (0.5, 1.0),
        "target_energy": 0.8,
        "target_acousticness": (0.8, 1.0),
        "preferred_tempo_range": (60, 120),
        "artist_preferences": ["The Beatles", "Taylor Swift", "Miles Davis", "Lofi Beats"],
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    MAX_SCORE = 7.0  # max possible points from score_song

    # ── Header ──────────────────────────────────────────────────────────────
    print("═" * 60)
    print("🎵  TOP MUSIC RECOMMENDATIONS FOR YOU")
    print("═" * 60)

    for rank, rec in enumerate(recommendations, start=1):
        song, score, reasons = rec

        # Visual score bar scaled to max possible score
        filled = round((score / MAX_SCORE) * 10)
        bar = "█" * filled + "░" * (10 - filled)

        print(f"\n  #{rank}  {song['title']}  —  {song['artist']}")
        print(f"       Score  : {score:.1f} / {MAX_SCORE:.1f}  [{bar}]")
        print(f"       Genre  : {song['genre']}   Mood: {song['mood']}   Energy: {song['energy']}")
        print(f"       Reasons:")
        if reasons:
            for reason in reasons:
                print(f"         ✔  {reason}")
        else:
            print("         —  No matching preferences found")
        print("  " + "─" * 57)

    print("═" * 60 + "\n")


if __name__ == "__main__":
    main()
