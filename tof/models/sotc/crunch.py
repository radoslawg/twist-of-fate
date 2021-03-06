from tof.models import Base
from tof.models.sotc import sotc_tablename
from sqlalchemy import (
    Column,
    Integer,
    Text,
    )
from sqlalchemy.schema import ForeignKey

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

#class SotCCharacter(Character):
#    __mapper_args__ = {'polymorphic_identity':

class Aspect(Base):
    __tablename__ = '.'.join([sotc_tablename, 'aspects'])
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)
    character_id = Column(Integer, ForeignKey('characters.id'))

class Stunt(Base):
    __tablename__ = '.'.join([sotc_tablename, 'stunts'])
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)
    character_id = Column(Integer, ForeignKey('characters.id'))

class Skill(Base):
    __tablename__ = '.'.join([sotc_tablename, 'skills'])
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)
    level = Column(Ladder.db_type())
    character_id = Column(Integer, ForeignKey('characters.id'))

class Consequence(Base):
    __tablename__ = '.'.join([sotc_tablename, 'consequences'])
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)
    type = Column(ConsequenceType.db_type())


