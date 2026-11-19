import csv
import os

print("======= GYM BRO =======")
print("=== Welcome From Gym Tracker ===")

pros = []
pro2 = []
notes = []

name = input("Enter your name: ")

while True:
    try:
        age = int(input("Enter your age: "))
        if age <= 8:
            print("You are below the age requirement!")
            continue
        break
    except ValueError:
        print(f"{name} Enter integer!")

if os.path.exists("Historys.csv"):
    with open("Historys.csv", "r") as file:
        reader = csv.reader(file)
        next(reader, None)

        for row in reader:
            if len(row) == 6:
                try:
                    pros.append({
                        "Name": row[0],
                        "Age": int(row[1]),
                        "Height": int(row[2]),
                        "Weight": int(row[3]),
                        "Gym Program": row[4],
                        "Experience": int(row[5])
                    })
                except ValueError:
                    continue

if os.path.exists("Gym_progress.csv"):
    with open("Gym_progress.csv", "r") as file:
        reader = csv.reader(file)
        next(reader, None)

        for row in reader:
            if len(row) == 3:
                try:
                    pro2.append({
                        "Weight gain": int(row[0]),
                        "Progressive [Weight]": int(row[1]),
                        "Workout": row[2]
                    })
                except ValueError:
                    continue

if os.path.exists("Note.csv"):
    with open("Note.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if len(row) > 0:
                notes.append(row[0])

print('''
    1. User info
    11. View user info
    2. Gym\User progress
    22. View Gym\User progress
    3. Notes
    33. View notes
    4. Exit ''')

while True:
    try:
        command = int(input("Enter your choice[1,2 etc..]: "))
    except ValueError:
        print(f"{name} Enter integer![1,2 etc..]")
        continue

    if command == 1:
        print("=== User info ===")
        gym_program = input("What plan do you follow[PPL etc...]?: ")

        try:
            year_gym = int(input("How long you have been playing?: "))
        except ValueError:
            print(f"{name} Enter integer!")
            continue

        while True:
            try:
                weight = int(input("Enter your weight[kg]: "))
                if weight <= 0:
                    print("Invalid!")
                    continue
                break
            except ValueError:
                print("Enter integer!")

        while True:
            try:
                height = int(input("Enter your height[ft]: "))
                if height <= 0:
                    print("Invalid!")
                    continue
                break
            except ValueError:
                print("Enter integer!")

        new_pros = {
            "Name": name,
            "Age": age,
            "Weight": weight,
            "Height": height,
            "Gym Program": gym_program,
            "Experience": year_gym
        }
        pros.append(new_pros)

        with open("Historys.csv", "a", newline="") as file:
            writer = csv.writer(file)

            if os.path.getsize("Historys.csv") == 0:
                writer.writerow(["Name", "Age", "Height", "Weight", "Gym Program", "Experience"])

            writer.writerow([name, age, height, weight, gym_program, year_gym])
            print("Successfully saved!")

    elif command == 11:
        if not pros:
            print("No history found!")
        else:
            print("\n=== Here ===")

            for item in pros:
                print(
                    f"{item['Name']} - "
                    f"{item['Age']} yrs old - "
                    f"{item['Height']} ft - "
                    f"{item['Weight']} kg - "
                    f"{item['Gym Program']} - "
                    f"{item['Experience']} yrs"
                )

    elif command == 2:
        try:
            weight_gain = int(input("How you gain (weight): "))
        except ValueError:
            print("Enter integer!")
            continue

        try:
            gym_weight = int(input("Enter how much you can lift weight[in specific workout]: "))
        except ValueError:
            print("Enter integer!")
            continue

        workout = input("What workout weight is this: ")

        pross = {
            "Weight gain": weight_gain,
            "Progressive [Weight]": gym_weight,
            "Workout": workout
        }
        pro2.append(pross)

        with open("Gym_progress.csv", "a", newline="") as file:
            writer = csv.writer(file)

            if os.path.getsize("Gym_progress.csv") == 0:
                writer.writerow(["Weight gain", "Progressive [Weight]", "Workout"])

            writer.writerow([weight_gain, gym_weight, workout])

            print("Successfully saved!")

    elif command == 22:
        if not pro2:
            print("Not found!")

        else:
            print("=== Here ===")
            for index, item in enumerate(pro2):
                print(
                    f"{index + 1} month. "
                    f"Weight gain: {item['Weight gain']} kg - "
                    f"Lift: {item['Progressive [Weight]']} kg - "
                    f"Workout[Lift]: {item['Workout']}"
                )

    elif command == 3:
        note = input(''' ''')
        notes.append(note)

        with open("Note.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([note])

        print("Saved Note")

    elif command == 33:
        if not notes:
            print("Not found!")

        else:
            print("=== Here ===")

            for item in notes:
                print(item)

    elif command == 4:
        print("Thanks for using Gym Bro!")
        break

    else:
        print("Invalid!")
