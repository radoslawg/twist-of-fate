from pyramid.view import view_config


from os.path import join
from tof import templates

@view_config(route_name='home', renderer=join(templates, 'home.pt'))
def home(request):
    return {'project':'tof'}

