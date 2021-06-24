from peewee import *

from . import db

__all__ = ['Module',
           'Assignment',
           'Staff',
           'ModuleLeaders',
           'ModuleAssessors',
           'GradeBandComment',
           'AdjustableComment',
           'LateComment',
           'PenaltyComment']

class BaseModel(Model):
    class Meta:
        database = db

class Module(BaseModel):
    code = FixedCharField(max_length=10,
                          unique=True,
                          primary_key=True)
    name = CharField(max_length=10)
    # TODO leaders = 1+
    # TODO assessors =  0+

class Assignment(BaseModel):
    assignment_code = FixedCharField(max_length=10,
                                     unique=True,
                                     primary_key=True)
    module_code = ForeignKeyField(Module)
    title = CharField(max_length=100)
    # TODO weight = IntegerField()  1 - 100
    description = TextField()
    # TODO submissions = 0+

    # TODO del only if no submissions

class Staff(BaseModel):
    forename = CharField(max_length=50)
    surname = CharField(max_length=50)
    username = CharField(max_length=10)
    password = CharField(max_length=255)

    # TODO 1+ as leader and/or assessor of module
    # TODO del only if not teaching nor assessing any modules

class ModuleLeaders(BaseModel):
    module_code = ForeignKeyField(Module)
    staff = ForeignKeyField(Staff)

class ModuleAssessors(BaseModel):
    module_code = ForeignKeyField(Module)
    staff = ForeignKeyField(Staff)

class Comment(BaseModel):
    assignment_code = ForeignKeyField(Assignment)
    title = TextField()
    comment = TextField()

class GradeBandComment(Comment):
    min_grade = IntegerField() # TODO <= 100
    max_grade = IntegerField() # TODO <= 100, > min_grade

class AdjustableComment(Comment):
    grade_adjustment = IntegerField() # TODO -5 to +5 including 0

class LateComment(Comment):
    days_late = IntegerField() # TODO max 7

class PenaltyComment(Comment):
    grade_deduction = IntegerField() # TODO 1 - 100
