import csv
from typing import List

import requests
from dagster import job, op, get_dagster_logger


@op
def download_cereals() -> List[dict]:
    res = requests.get("https://docs.dagster.io/assets/cereal.csv")
    lines = res.text.split("\n")
    return [row for row in csv.DictReader(lines)]


# @op
# def find_sugariest(cereals) -> str:
#     sorted_cereals = sorted(cereals, key=lambda cereal: cereal["sugars"])
#     return sorted_cereals[-1]["name"]


@op
def find_highest_calorie_cereal(cereals) -> str:
    sorted_cereals = sorted(cereals, key=lambda cereal: cereal["calories"])
    return sorted_cereals[-1]["name"]


@op
def find_highest_protein_cereal(cereals) -> str:
    sorted_cereals = sorted(cereals, key=lambda cereal: cereal["protein"])
    return sorted_cereals[-1]["name"]


@op
def display_results(most_calories: str, most_protein: str):
    logger = get_dagster_logger()
    logger.info(f"Most caloric cereal: {most_calories}")
    logger.info(f"Most protein-rich cereal: {most_protein}")


@job
def diamond():
    cereals = download_cereals()
    display_results(
        most_calories=find_highest_calorie_cereal(cereals),
        most_protein=find_highest_protein_cereal(cereals),
    )


def test_find_highest_calorie_cereal():
    cereals = [
        {"name": "hi-cal cereal", "calories": 400},
        {"name": "lo-cal cereal", "calories": 50},
    ]
    result = find_highest_calorie_cereal(cereals)
    assert result == "hi-cal cereal"


def test_diamond():
    res = diamond.execute_in_process()
    assert res.success
    assert res.output_for_node("find_highest_protein_cereal")  == "Special K"
