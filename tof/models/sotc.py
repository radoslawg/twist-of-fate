from . import Base
from sqlalchemy import (
    Column,
    Integer,
    Text,
    )

class Aspect(Base):
    __tablename__ = 'aspects'
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)

class Stunt(Base):
    __tablename__ = 'stunts'
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)

class Skill(Base):
    __tablename__ = 'skills'
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)
    level = Column(Integer)

class Ladder(object):
    SUPERB = 5
