import unittest
import transaction

from pyramid import testing
from pyramid.paster import get_appsettings
from sqlalchemy import engine_from_config
from sqlalchemy.exc import IntegrityError

from tof.models import DBSession

class TestCharacter(unittest.TestCase):

    def setUp(self):
        self.config = testing.setUp()
        settings = get_appsettings('development.ini')
        engine = engine_from_config(settings, 'sqlalchemy.')
        from tof.models import Base
        DBSession.configure(bind=engine)
        Base.metadata.create_all(engine)
        
    def tearDown(self):
        DBSession.remove()
        testing.tearDown()

    def character_duplicate_test(self):
        from tof.models.sotc.character import SotCCharacter as Character
        with self.assertRaises(IntegrityError):
            with transaction.manager:
                model = Character(name='Jet Black, Flying Soldier', played_by="John", fate_points=11, refresh_rate=11)
                DBSession.add(model)

    def character_create_test(self):
        from tof.models.sotc.character import SotCCharacter as Character
        from tof.models.sotc.crunch import Skill, Aspect, Stunt, Ladder

        try:
            with transaction.manager:
                aspects = [Aspect(name="\"Lucy\", the Century Clipper"), Aspect(name="Fly by Night")]
                skills = [Skill(name="Contacting", level=Ladder.superb), Skill(name="Pilot", level=Ladder.great)]
                stunts = [Stunt(name="Walk the Walk"), Stunt(name="Lucy (Personal Gadget)")]
                model = Character(name='Mack Silver, Entrepreneurial Pilot', played_by="John", skills=skills, aspects=aspects, stunts=stunts, fate_points=11, refresh_rate=11)
                DBSession.add(model)

            with transaction.manager:
                model = DBSession.query(Character).filter(Character.name=="Mack Silver, Entrepreneurial Pilot").one()
                self.assertEqual(model.name, "Mack Silver, Entrepreneurial Pilot")
                self.assertEqual(model.played_by, "John")
                self.assertEqual(model.fate_points, 11)
                self.assertEqual(model.refresh_rate, 11)
                self.assertItemsEqual([m.name for m in model.aspects], [a.name for a in aspects])
                self.assertItemsEqual([{m.name: m.level} for m in model.skills], [{m.name: m.level.value} for m in skills])
                self.assertItemsEqual([m.name for m in model.stunts], [a.name for a in stunts])
        finally:
            with transaction.manager:
                c = DBSession.query(Character).filter(Character.name=="Mack Silver, Entrepreneurial Pilot").one()
                DBSession.delete(c)
                for skill in skills: 
                    s = DBSession.query(Skill).filter(Skill.name==skill.name).one()
                    DBSession.delete(s)
                for aspect in aspects: 
                    s = DBSession.query(Aspect).filter(Aspect.name==aspect.name).one()
                    DBSession.delete(s)
                for stunt in stunts: 
                    s = DBSession.query(Stunt).filter(Stunt.name==stunt.name).one()
                    DBSession.delete(s)
