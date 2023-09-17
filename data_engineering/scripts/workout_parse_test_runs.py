import json
import requests
from kuda.scrapers.workout.parser import parse_workout_html


broken = [
]

html = requests.get(broken[0]).text

workout = parse_workout_html(
	html_text=html,
	url=broken[0],
)

with open("data/workout_links/parse_test.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(workout, indent=4))
