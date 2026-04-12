from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    user_profile = {
        "favorite_genres": ["rock", "pop", "lofi", "jazz", "ambient"],
        "favorite_moods": ["chill", "happy", "melancholic", "energetic", "romantic"],
        "target_valence": 0.7,
        "positive_energy": (0.5, 1.0),
        "target_energy": 0.8,
        "target_acousticness": (0.8, 1.0),
        "preferred_tempo_range": (60, 120),
        "artist_preferences": ["The Beatles", "Taylor Swift", "Miles Davis", "Lofi Beats"],
    }


class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    This loads songs from a CSV file and returns a list of song dictionaries.
    Required by src/main.py
    """
    import csv
    songs = []
    with open(csv_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['id'] = int(row['id'])
            row['energy'] = float(row['energy'])
            row['tempo_bpm'] = float(row['tempo_bpm'])
            row['valence'] = float(row['valence'])
            row['danceability'] = float(row['danceability'])
            row['acousticness'] = float(row['acousticness'])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences and return the score along with reasons for the score.
    Required by recommend_songs() and src/main.py
    """
    score = 0.0
    reasons = []

    # Genre match: 2 points
    if song['genre'].lower() in [g.lower() for g in user_prefs['favorite_genres']]:
        score += 2
        reasons.append(f"Matched favorite genre: {song['genre']}")

    # Mood match: 1 point
    if song['mood'].lower() in [m.lower() for m in user_prefs['favorite_moods']]:
        score += 1
        reasons.append(f"Matched favorite mood: {song['mood']}")

    # Energy match: 1 point
    energy_range = user_prefs['positive_energy']
    if energy_range[0] <= song['energy'] <= energy_range[1]:
        score += 1
        reasons.append(f"Energy level within preferred range: {song['energy']}")

    # Valence match: 1 point
    if abs(song['valence'] - user_prefs['target_valence']) < 0.2:
        score += 1
        reasons.append(f"Valence close to preference: {song['valence']}")

    # Tempo match: 1 point
    tempo_range = user_prefs['preferred_tempo_range']
    if tempo_range[0] <= song['tempo_bpm'] <= tempo_range[1]:
        score += 1
        reasons.append(f"Tempo within preferred range: {song['tempo_bpm']} BPM")

    # Acousticness match: 1 point
    acoustic_range = user_prefs['target_acousticness']
    if acoustic_range[0] <= song['acousticness'] <= acoustic_range[1]:
        score += 1
        reasons.append(f"Acousticness within preferred range: {song['acousticness']}")

    return (score, reasons)

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, List[str]]]:
    """
    Scores all songs and returns the top k songs along with their scores and reasons for recommendation.
    Required by src/main.py
    """
    # Score all songs and pass reasons list through
    scored_songs = [
        (song, score, reasons)
        for song in songs
        for score, reasons in [score_song(user_prefs, song)]
    ]
    # Sort by score descending and return top k
    top_k = sorted(scored_songs, key=lambda x: x[1], reverse=True)[:k]
    return top_k