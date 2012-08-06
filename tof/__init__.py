from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import DBSession

from os.path import dirname, join, abspath
templates=join(abspath(dirname(__file__)), 'templates')

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('tutorial_home', '/tutorial')
    config.add_route('sotc_home', '/sotc')
    config.add_route('sotc_character', '/sotc/character')
    config.scan()

    config.add_subscriber('tof.subscribers.add_base_template',
                      'pyramid.events.BeforeRender')
    return config.make_wsgi_app()

