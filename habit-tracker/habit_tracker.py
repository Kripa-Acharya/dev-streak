import json
import os
from datetime import date

FILE_NAME = "habits.json"


def load_habits():
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME, "r") as f:
        return json.load(f)


def save_habits(habits):
    with open(FILE_NAME, "w") as f:
        json.dump(habits, f, indent=2)


def mark_habit(habits, name):
    today = str(date.today())
    habit = habits.get(name, [])

    if habit and habit[-1] == today:
        print("✅ Already marked today!")
        return

    habit.append(today)
    habits[name] = habit
    print(f"🔥 Streak updated for '{name}'")


def show_habits(habits):
    if not habits:
        print("No habits tracked yet.")
        return

    print("\nYour Habits:")
    for name, days in habits.items():
        print(f"- {name}: {len(days)} day streak")


def main():
    habits = load_habits()

    print("\n📆 Habit Streak Tracker")
    print("1. Mark habit")
    print("2. View habits")
    print("3. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        name = input("Habit name: ").strip()
        mark_habit(habits, name)
        save_habits(habits)
    elif choice == "2":
        show_habits(habits)
    else:
        print("Goodbye 👋")


if __name__ == "__main__":
    main()
