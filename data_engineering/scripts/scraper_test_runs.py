import json
import time

from kuda.scrapers.async_scrape import scrape_urls
from kuda.scrapers.workout.parser import parse_workout_html

BASE_WORKOUT_URL: str = (
    "https://bodyspace.bodybuilding.com/workouts/viewworkoutlog/"
)

start = time.time()

data = scrape_urls(
    urls=[
        f"{BASE_WORKOUT_URL}102561/54ff1aed0cf2b9e68f9ec26f",
        f"{BASE_WORKOUT_URL}coachdmurph/5bf3ec42176a3027b0ad04d8",
        f"{BASE_WORKOUT_URL}1243week/5a65f0b549cd4326e09821ca",
        f"{BASE_WORKOUT_URL}12laynew/58097f260cf27a6fb6996c8d",
        f"{BASE_WORKOUT_URL}12LittLebit/5a024d9fb36829286bb464e9",
        f"{BASE_WORKOUT_URL}zzolowicz/5901402f36d69c3acb773dd4",
        f"{BASE_WORKOUT_URL}zzshad/593210b4af19ce69876e7dcd",
        f"{BASE_WORKOUT_URL}-NYSE1-/4fb56f36b488e39f44f45352",
        f"{BASE_WORKOUT_URL}zzohaib/5376f2f70cf28afcb6ce2e9a",
        f"{BASE_WORKOUT_URL}zzneo/5bcad0494e400527ce7156fc",
    ],
    html_parser=parse_workout_html,
    batch_size=10,
)

end = time.time()
print(f"Time taken: {end - start}")

with open("data/workout_links/example.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(data, indent=4))
