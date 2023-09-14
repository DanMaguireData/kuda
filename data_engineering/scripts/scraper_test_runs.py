import json
import time

import requests

from kuda.scrapers import scrape_workout

BASE_WORKOUT_URL: str = (
    "https://bodyspace.bodybuilding.com/workouts/viewworkoutlog/"
)


def scrape_single_workout(link: str):
    """
    Scrape a single workout and save it to a file.
    """

    requests_session = requests.Session()
    start = time.time()
    workout = scrape_workout(url=link, requests_session=requests_session)
    print(f"Time taken: {time.time() - start}")
    with open("data/workout_links/example.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(workout, indent=4))
    return workout


scrape_single_workout(
    f"{BASE_WORKOUT_URL}coachdmurph/5bf3ec42176a3027b0ad04d8"
)
