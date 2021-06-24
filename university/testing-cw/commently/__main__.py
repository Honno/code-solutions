from sys import modules

from . import db
from utils import get_models

with db:
    db.create_tables(get_models())
