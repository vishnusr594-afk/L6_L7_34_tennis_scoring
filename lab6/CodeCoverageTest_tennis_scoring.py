import pytest
from tennis_scoring import game_score, set_winner, match_status


def test_normal_game_scores():
    assert game_score(1, 2) == "15-30"


def test_negative_points():
    with pytest.raises(ValueError):
        game_score(-1, 0)


def test_deuce():
    assert game_score(3, 3) == "deuce"


def test_game_a_after_deuce():
    assert game_score(5, 3) == "game A"


def test_game_b_after_deuce():
    assert game_score(3, 5) == "game B"


def test_advantage_a():
    assert game_score(4, 3) == "advantage A"


def test_advantage_b():
    assert game_score(3, 4) == "advantage B"


def test_game_a_normal():
    assert game_score(4, 0) == "game A"


def test_game_b_normal():
    assert game_score(0, 4) == "game B"


def test_set_a_wins():
    assert set_winner(6, 4) == "A"


def test_set_b_wins():
    assert set_winner(4, 6) == "B"


def test_set_a_wins_tiebreak():
    assert set_winner(7, 6) == "A"


def test_set_b_wins_tiebreak():
    assert set_winner(6, 7) == "B"


def test_match_a_wins():
    assert match_status(2, 0, 3) == "A wins"


def test_match_b_wins():
    assert match_status(0, 2, 3) == "B wins"


def test_match_decider():
    assert match_status(1, 1, 3) == "decider"


def test_match_in_progress():
    assert match_status(1, 0, 3) == "in progress"