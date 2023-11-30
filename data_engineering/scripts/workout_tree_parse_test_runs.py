import json

from kuda.data_pipelining.highrise.file_transformers import parse_workout_tree

if __name__ == "__main__":
    file_path = ""
    with open(file_path, "r", encoding="utf-8") as f:
        workouts = json.load(f)

    workout_tree = parse_workout_tree(workouts=workouts)

    print(workout_tree)
