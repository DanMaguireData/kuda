import json

import requests

from kuda.scrapers.workout.parser import parse_workout_html

broken = [
    "https://bodyspace.bodybuilding.com/workouts/viewworkoutlog/azmatalipasha/56e6ef2c0cf250667f39a72e"
]

html = requests.get(broken[0], timeout=20).text

workout = parse_workout_html(
    html_text=html,
    url=broken[0],
)

with open("data/workout_links/parse_test.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(workout, indent=4))
