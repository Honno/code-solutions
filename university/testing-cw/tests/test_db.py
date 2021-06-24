from copy import copy

import pytest
from playhouse.shortcuts import model_to_dict

from commently import db
from commently.models import *
from commently.utils import get_models
from commently.repo import create_staff

db = copy(db)

def dcd(dict1, dict2):
    """i.e. dict contains dict"""
    for key, value in dict2.items():
        if key not in dict1 or dict1[key] != value:
            return False
    else:
        return True


def test_create_staff():
    with db:
        person = {
            'forename': "Matthew",
            'surname': "Barber",
            'username': "honno",
            'password': "stoplooking"
        }

        Staff.create(**person)

        record = Staff.get(Staff.username == person['username'])

        assert dcd(model_to_dict(record), person)


