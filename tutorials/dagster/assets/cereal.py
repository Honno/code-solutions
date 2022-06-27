import csv
from typing import Dict, List

import requests
from dagster import asset, materialize

Table = List[Dict[str, str]]


@asset
def cereals() -> Table:
    response = requests.get("https://docs.dagster.io/assets/cereal.csv")
    lines = response.text.split("\n")
    cereal_rows = [row for row in csv.DictReader(lines)]
    return cereal_rows


@asset
def nabisco_cereals(cereals: Table) -> Table:
    """
    Cereals manufactured by Nabisco
    """
    return [row for row in cereals if row["mfr"] == "N"]


@asset
def cereal_protein_fractions(cereals: Table) -> Dict[str, float]:
    """
    For each cereal, records its protein content as a fraction of its total mass.
    """
    result = {}
    for cereal in cereals:
        total_grams = float(cereal["weight"]) * 28.35
        result[cereal["name"]] = float(cereal["protein"]) / total_grams
    return result


@asset
def highest_protein_nabisco_cereal(
    nabisco_cereals: Table, cereal_protein_fractions: Dict[str, float]
) -> str:
    """
    The name of the nabisco cereal that has the highest protein content.
    """
    sorted_by_protein = sorted(
        nabisco_cereals, key=lambda cereal: cereal_protein_fractions[cereal["name"]]
    )
    return sorted_by_protein[-1]["name"]


def test_nabisco_cereals():
    cereals = [
        {"name": "cereal1", "mfr": "N"},
        {"name": "cereal2", "mfr": "K"},
    ]
    result = nabisco_cereals(cereals)
    assert len(result) == 1
    assert result == [{"name": "cereal1", "mfr": "N"}]


def test_cereal_assets():
    assets = [
        nabisco_cereals,
        cereals,
        cereal_protein_fractions,
        highest_protein_nabisco_cereal,
    ]
    result = materialize(assets)
    assert result.success
    assert result.output_for_node("highest_protein_nabisco_cereal") == "100% Bran"
