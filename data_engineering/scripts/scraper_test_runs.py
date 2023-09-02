import json
import time

from .. import WORKOUT_VARIANTS
from kuda.scrapers.workout import scrape_workout_page

def save_links_for_testing() -> None:
    tested_links = []
    for workout in WORKOUT_VARIANTS:
        link = workout["link"]
        print(f"Processing link: '{link}'")
        workout = scrape_workout_page(link)
        tested_links.append(workout)

    with open("test/files/tested_links.json", "w") as f:
        f.write(json.dumps(tested_links, indent=4))
    print("Saved Workout Variants!")


def scrape_single_workout(link: str):
    start = time.time()
    workout = scrape_workout_page(link)
    print(f"Time taken: {time.time() - start}")
    with open("data/workout_links/example.json", "w") as f:
        f.write(json.dumps(workout, indent=4))
    return workout

scrape_single_workout(WORKOUT_VARIANTS[0]["link"])
