from sqlalchemy import (
    Column,
    Integer,
    )
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship

from tof.models.character import Character
from tof.models.crunch import Crunch
from tof.models.sotc import sotc_tablename

class SotCCharacter(Character):
    __tablename__ = '.'.join([sotc_tablename, 'characters'])
    __mapper_args__ = {'polymorphic_identity': Crunch.SotC}
    id = Column(Integer, ForeignKey('characters.id'), primary_key=True)
    fate_points = Column(Integer)
    refresh_rate = Column(Integer)
    aspects = relationship("Aspect")
    skills = relationship("Skill")
    stunts = relationship("Stunt")
