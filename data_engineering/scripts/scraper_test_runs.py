import json
import time
from pprint import pprint

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


response = scrape_single_workout(
    f"{BASE_WORKOUT_URL}102561/54ff1aed0cf2b9e68f9ec26f"
)

pprint(response)
