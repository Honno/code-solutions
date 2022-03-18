#!/usr/bin/env python
import csv

import requests
from dagster import job, op, get_dagster_logger


@op
def hello_cereal():
    res = requests.get("https://docs.dagster.io/assets/cereal.csv")
    lines = res.text.split("\n")
    cereals = [row for row in csv.DictReader(lines)]
    get_dagster_logger().info(f"Found {len(cereals)} cereals")


@job
def hello_cereal_job():
    hello_cereal()


if __name__ == "__main__":
    result = hello_cereal_job.execute_in_process()
