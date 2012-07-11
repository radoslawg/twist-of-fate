from . import Base
from sqlalchemy import (
    Column,
    Integer,
    Text,
    )

sotc_tablename = '.'.join(__name__.split('.')[2:])

# enumerations
from tof.recipies.declarative_enum import DeclEnum

class ConsequenceType(DeclEnum):
    mild = "mild", "Mild Consequence"
    moderate = "moderate", "Moderate Consequence"
    mild = "severe", "Severe Consequence"

class Ladder(DeclEnum):
    superb = "5", "superb"
    great = "4", "great"
    good = "3", "good"
    fair = "2", "fair"
    average = "1", "average"

class Aspect(Base):
    __tablename__ = '.'.join([sotc_tablename, 'aspects'])
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)

class Stunt(Base):
    __tablename__ = '.'.join([sotc_tablename, 'stunts'])
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)

class Skill(Base):
    __tablename__ = '.'.join([sotc_tablename, 'skills'])
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)
    level = Column(Ladder.db_type())

class Consequence(Base):
    __tablename__ = '.'.join([sotc_tablename, 'consequences'])
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)
    type = Column(ConsequenceType.db_type())


