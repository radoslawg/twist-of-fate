import unittest
import transaction

from pyramid import testing
from pyramid.paster import get_appsettings
from sqlalchemy import engine_from_config

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

    def character_create_test(self):
        from tof.models.character import Character
        with transaction.manager:
            model = Character(name='the Rocketeer', played_by="John", fate_points=11, refresh_rate=11)
            DBSession.add(model)

        with transaction.manager:
            model = DBSession.query(Character).filter(Character.name=="the Rocketeer").one()
            self.assertEqual(model.name, "the Rocketeer")
            self.assertEqual(model.played_by, "John")
            self.assertEqual(model.fate_points, 11)
            self.assertEqual(model.refresh_rate, 11)

        with transaction.manager:
            DBSession.delete(model)
