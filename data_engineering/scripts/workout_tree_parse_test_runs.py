import json

from kuda.data_pipelining.highrise.file_transformers import parse_workout_tree


if __name__ == "__main__":

	file_path = ""
	workouts = json.load(open(file_path, "r"))

	workout_tree = parse_workout_tree(workouts=workouts)

	print(workout_tree)
