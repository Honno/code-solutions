from peewee import SqliteDatabase

from . import db
from .models import *

def create_staff(forename, surname, username, password):
    Staff.create(forename, surname, username, password)

def create_module(code, name, leaders, assessors=None):
    pass
