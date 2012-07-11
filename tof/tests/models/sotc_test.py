import unittest
import transaction

from pyramid import testing
from pyramid.paster import get_appsettings
from sqlalchemy import engine_from_config

from tof.models import DBSession

class TestSotC(unittest.TestCase):

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

    def aspect_create_test(self):
        from tof.models.sotc import Aspect
        with transaction.manager:
            name = "Astounding Aspect"
            model = Aspect(name=name)
            DBSession.add(model)

        with transaction.manager:
            model = DBSession.query(Aspect).filter(Aspect.name==name).one()
            self.assertEqual(model.name, name)

        with transaction.manager:
            DBSession.delete(model)

    def stunt_create_test(self):
        from tof.models.sotc import Stunt
        with transaction.manager:
            name = "Stupendous Stunt"
            model = Stunt(name=name)
            DBSession.add(model)

        with transaction.manager:
            model = DBSession.query(Stunt).filter(Stunt.name==name).one()
            self.assertEqual(model.name, name)

        with transaction.manager:
            DBSession.delete(model)

    def skill_create_test(self):
        from tof.models.sotc import Skill, Ladder
        with transaction.manager:
            name = "Superlative Skill"
            model = Skill(name=name, level=Ladder.SUPERB)
            DBSession.add(model)

        with transaction.manager:
            model = DBSession.query(Skill).filter(Skill.name==name).one()
            self.assertEqual(model.name, name)

        with transaction.manager:
            DBSession.delete(model)
