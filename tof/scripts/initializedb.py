import os
import sys
import transaction

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from tof.models import (
    DBSession,
    Base,
    )
from tof.models.character import Character
from tof.models.sotc import Aspect, Stunt, Skill, Ladder

def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd)) 
    sys.exit(1)

def main(argv=sys.argv):
    if len(argv) != 2:
        usage(argv)
    config_uri = argv[1]
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    with transaction.manager:
        character = Character(name='Jet Black, Flying Soldier', played_by="John", fate_points=11, refresh_rate=11)
        DBSession.add(character)
        aspect = Aspect(name='Amazing Jet Pack!')
        DBSession.add(aspect)
        skill = Skill(name='Athletics', level=Ladder.superb)
        DBSession.add(skill)
        stunt = Stunt(name='The Amazing Jet Pack')
        DBSession.add(stunt)
