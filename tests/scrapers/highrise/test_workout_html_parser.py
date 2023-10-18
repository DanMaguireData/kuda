import json

from deepdiff import DeepDiff

from kuda.scrapers import parse_workout_html
from tests.scrapers import FILE_PATH
from tests.vars import WORKOUT_VARIANTS


def test_workout_link_html_parser() -> None:
    """
    Test that the parsed data is the same as the one
    """

    with open(
        f"{FILE_PATH}/html/workout_links.json", "r", encoding="utf-8"
    ) as f:
        raw_html = json.load(f)

    with open(
        f"{FILE_PATH}/parsed/workout_links.json", "r", encoding="utf-8"
    ) as f:
        parsed_workouts = json.load(f)

    for index, html_page in enumerate(raw_html):
        parsed_page = parse_workout_html(
            html_text=html_page, url=WORKOUT_VARIANTS[index]["link"]
        )

        # Inaccessible Workout will just be an empty dict
        if not parsed_page:
            assert parsed_page == parsed_workouts[index]
            continue

        assert set(parsed_page.pop("muscles_used")) == set(
            parsed_workouts[index].pop("muscles_used")
        )
        assert DeepDiff(parsed_workouts[index], parsed_page) == {}
