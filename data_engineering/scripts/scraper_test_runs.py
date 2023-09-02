import json
import time

from kuda.scrapers import scrape_workout


def scrape_single_workout(link: str):
    start = time.time()
    workout = scrape_workout(link)
    print(f"Time taken: {time.time() - start}")
    with open("data/workout_links/example.json", "w") as f:
        f.write(json.dumps(workout, indent=4))
    return workout
