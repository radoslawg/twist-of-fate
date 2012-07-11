from . import Base
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
    fate_points = Column(Integer)
    refresh_rate = Column(Integer)
