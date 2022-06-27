import csv
from typing import Dict, List

import requests
from dagster import asset, materialize


@asset
def cereals() -> List[Dict[str, str]]:
    response = requests.get("https://docs.dagster.io/assets/cereal.csv")
    lines = response.text.split("\n")
    cereal_rows = [row for row in csv.DictReader(lines)]

    return cereal_rows


if __name__ == "__main__":
    materialize([cereals])
