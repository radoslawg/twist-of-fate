from . import Base
from tof.models.crunch import Crunch
from sqlalchemy import (
    Column,
    Integer,
    Text,
    )

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)
    played_by = Column(Text)
    crunch = Column(Crunch.db_type())
    __mapper_args__ = {'polymorphic_on': crunch}
