import json
from datetime import datetime
from pathlib import Path

DATA_FILE = Path("moods.json")


def load_moods():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def save_moods(moods):
    with open(DATA_FILE, "w") as f:
        json.dump(moods, f, indent=2)


def log_mood():
    mood = input("How are you feeling today? (1-5): ")
    note = input("Any note for today? (optional): ")

    entry = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "mood": mood,
        "note": note
    }

    moods = load_moods()
    moods.append(entry)
    save_moods(moods)

    print("Mood saved!")


def view_moods():
    moods = load_moods()

    if not moods:
        print("No moods logged yet.")
        return

    for entry in moods:
        print(f"{entry['date']} | Mood: {entry['mood']} | {entry['note']}")


def main():
    print("Daily Mood Logger")
    print("1. Log today's mood")
    print("2. View past moods")

    choice = input("Choose an option (1/2): ")

    if choice == "1":
        log_mood()
    elif choice == "2":
        view_moods()
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
