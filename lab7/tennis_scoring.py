
def parse_score(text):
    if not isinstance(text, str):
        return 0, 0

    try:
        parts = text.split('-')
        if len(parts) != 2:
            return 0, 0

        a = int(parts[0])
        b = int(parts[1])

        if a < 0 or b < 0:
            return 0, 0

        return a, b
    except ValueError:
        return 0, 0


def game_lead(text):
    points = {'0': 0, '15': 1, '30': 2, '40': 3}

    if not isinstance(text, str):
        return 0

    try:
        parts = text.split('-')
        if len(parts) != 2:
            return 0

        first, second = parts

        if first not in points or second not in points:
            return 0

        return points[first] - points[second]
    except (ValueError, TypeError):
        return 0


def set_spread(games_csv):
    if not isinstance(games_csv, str) or not games_csv.strip():
        return 0

    try:
        games = [int(g.strip()) for g in games_csv.split(',')]

        if not games or any(g < 0 for g in games):
            return 0

        return max(games) - min(games)
    except ValueError:
        return 0


def main():
    print("==== Running parse_score ====")
    user_input = input("Enter points won as A-B (e.g. 3-2): ")
    result = parse_score(user_input)
    print("Points A and B:", result)

    print("\n==== Running game_lead ====")
    user_input = input("Enter a game score (e.g. 40-30): ")
    result = game_lead(user_input)
    print("Lead in Points:", result)

    print("\n==== Running set_spread ====")
    user_input = input("Enter games won per set as CSV (e.g. 6,4,7): ")
    result = set_spread(user_input)
    print("Spread:", result)


if __name__ == "__main__":
    main()
