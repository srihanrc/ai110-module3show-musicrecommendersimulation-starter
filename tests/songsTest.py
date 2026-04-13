import pytest
from src.recommender import score_song, recommend_songs


@pytest.fixture
def sample_songs():
    return [
        {
            "id": 1, "title": "A", "artist": "X", "genre": "pop", "mood": "happy",
            "energy": 0.8, "tempo_bpm": 100.0, "valence": 0.7, "danceability": 0.7, "acousticness": 0.9
        },
        {
            "id": 2, "title": "B", "artist": "Y", "genre": "rock", "mood": "chill",
            "energy": 0.6, "tempo_bpm": 90.0, "valence": 0.5, "danceability": 0.6, "acousticness": 0.85
        },
        {
            "id": 3, "title": "C", "artist": "Z", "genre": "metal", "mood": "angry",
            "energy": 0.2, "tempo_bpm": 150.0, "valence": 0.3, "danceability": 0.4, "acousticness": 0.1
        },
    ]


def test_recommend_songs_respects_k_and_sorts(sample_songs):
    prefs = {
        "favorite_genres": ["pop", "rock"],
        "favorite_moods": ["happy", "chill"],
        "target_valence": 0.7,
        "positive_energy": (0.5, 1.0),
        "target_energy": 0.8,
        "target_acousticness": (0.8, 1.0),
        "preferred_tempo_range": (60, 120),
        "artist_preferences": [],
    }

    recs = recommend_songs(prefs, sample_songs, k=2)
    assert len(recs) == 2
    scores = [r[1] for r in recs]
    assert scores == sorted(scores, reverse=True)


def test_no_match_profile_returns_zero_scores(sample_songs):
    prefs = {
        "favorite_genres": ["metalcore"],
        "favorite_moods": ["romantic"],
        "target_valence": -1.0,
        "positive_energy": (1.1, 2.0),
        "target_energy": 1.5,
        "target_acousticness": (1.1, 2.0),
        "preferred_tempo_range": (400, 500),
        "artist_preferences": ["Nobody"],
    }

    recs = recommend_songs(prefs, sample_songs, k=5)
    assert all(score == 0 for _, score, _ in recs)


def test_artist_preferences_currently_do_not_affect_scoring(sample_songs):
    base = {
        "favorite_genres": ["pop"],
        "favorite_moods": ["happy"],
        "target_valence": 0.7,
        "positive_energy": (0.5, 1.0),
        "target_energy": 0.8,
        "target_acousticness": (0.8, 1.0),
        "preferred_tempo_range": (60, 120),
    }

    prefs_a = {**base, "artist_preferences": ["Artist A"]}
    prefs_b = {**base, "artist_preferences": ["Totally Different Artist"]}

    recs_a = recommend_songs(prefs_a, sample_songs, k=3)
    recs_b = recommend_songs(prefs_b, sample_songs, k=3)

    assert recs_a == recs_b


def test_valence_boundary_exact_point_two_not_counted():
    song = {
        "id": 99, "title": "Boundary", "artist": "Edge", "genre": "none", "mood": "none",
        "energy": 0.0, "tempo_bpm": 0.0, "valence": 0.3, "danceability": 0.0, "acousticness": 0.0
    }