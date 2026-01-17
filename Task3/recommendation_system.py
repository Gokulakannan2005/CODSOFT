# Recommendation System for Movies and Games
# Content-based filtering using user preferences

movies = {
    "Inception": {
        "screenplay": 5,
        "mood": 4,
        "ending": 4
    },
    "Interstellar": {
        "screenplay": 5,
        "mood": 3,
        "ending": 5
    },
    "The Dark Knight": {
        "screenplay": 5,
        "mood": 4,
        "ending": 4
    },
    "Avengers: Endgame": {
        "screenplay": 4,
        "mood": 5,
        "ending": 5
    },
    "Tenet": {
        "screenplay": 4,
        "mood": 3,
        "ending": 3
    }
}

games = {
    "The Witcher 3": {
        "difficulty": 3,
        "story": 5,
        "graphics": 5,
        "involvement": 5,
        "time": 5,
        "worth": 5
    },
    "Dark Souls": {
        "difficulty": 5,
        "story": 4,
        "graphics": 4,
        "involvement": 5,
        "time": 4,
        "worth": 4
    },
    "God of War": {
        "difficulty": 3,
        "story": 5,
        "graphics": 5,
        "involvement": 5,
        "time": 4,
        "worth": 5
    },
    "Minecraft": {
        "difficulty": 2,
        "story": 2,
        "graphics": 3,
        "involvement": 5,
        "time": 5,
        "worth": 5
    },
    "Celeste": {
        "difficulty": 4,
        "story": 4,
        "graphics": 4,
        "involvement": 4,
        "time": 3,
        "worth": 4
    }
}


def get_user_preferences(attributes):
    preferences = {}
    for attr in attributes:
        while True:
            try:
                value = int(input(f"Rate your preference for {attr} (1-5): "))
                if 1 <= value <= 5:
                    preferences[attr] = value
                    break
                else:
                    print("Please enter a value between 1 and 5.")
            except ValueError:
                print("Invalid input. Enter a number.")
    return preferences


def calculate_score(item_attributes, user_preferences):
    score = 0
    for attr in user_preferences:
        score += 5 - abs(item_attributes[attr] - user_preferences[attr])
    return score


def recommend(items, user_preferences):
    scores = []

    for item, attributes in items.items():
        score = calculate_score(attributes, user_preferences)
        scores.append((item, score))

    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[:3]


def main():
    print("Recommendation System")
    print("1. Movies")
    print("2. Games")

    choice = input("What would you like recommendations for? (1/2): ")

    if choice == "1":
        print("\nAnswer a few questions to get movie recommendations.\n")
        attributes = ["screenplay", "mood", "ending"]
        user_preferences = get_user_preferences(attributes)
        results = recommend(movies, user_preferences)

        print("\nTop 3 Movie Recommendations:")
        for item, score in results:
            print(f"- {item}")

    elif choice == "2":
        print("\nAnswer a few questions to get game recommendations.\n")
        attributes = ["difficulty", "story", "graphics", "involvement", "time", "worth"]
        user_preferences = get_user_preferences(attributes)
        results = recommend(games, user_preferences)

        print("\nTop 3 Game Recommendations:")
        for item, score in results:
            print(f"- {item}")

    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
