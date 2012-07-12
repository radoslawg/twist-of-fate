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
        from tof.models.character import Character
        with self.assertRaises(IntegrityError):
            with transaction.manager:
                model = Character(name='Jet Black, Flying Soldier', played_by="John")
                DBSession.add(model)

    def character_create_test(self):
        from tof.models.character import Character
        try:
            with transaction.manager:
                model = Character(name='Mack Silver, Entrepreneurial Pilot', played_by="John")
                DBSession.add(model)

            with transaction.manager:
                model = DBSession.query(Character).filter(Character.name=="Mack Silver, Entrepreneurial Pilot").one()
                self.assertEqual(model.name, "Mack Silver, Entrepreneurial Pilot")
                self.assertEqual(model.played_by, "John")
        finally:
            with transaction.manager:
                DBSession.delete(model)
