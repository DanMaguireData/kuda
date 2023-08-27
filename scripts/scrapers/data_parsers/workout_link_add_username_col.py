# Doing some Analysis on the old Male Workout Links Data

import pandas as pd
import os

root_path: str = "./phase_zero/data/workout_links/male/set_2"

example_workout_link: str = (
    "https://bodyspace.bodybuilding.com/"  # base url
    "workouts/viewworkoutlog/reycuban/"  # username
    "5622848d0cf2002249c7305a"  # workout uuid
)


def extract_username(links: str) -> str:
    """
    Extracts the username from the links column
    """

    links = list(eval(links))
    if len(links) == 0:
        return "n/a"
    return links[0].split("viewworkoutlog")[1].split("/")[1]


for _, _, files in os.walk(root_path):
    for file in files:
        if ".csv" not in file:
            continue
        df = pd.read_csv(f"{root_path}/{file}")
        if "username" in df.columns:
            continue
        print(f"Processing: '{file}'")
        df["username"] = df["Links"].apply(extract_username)
        df.to_csv(f"{root_path}/{file}", index=False)
