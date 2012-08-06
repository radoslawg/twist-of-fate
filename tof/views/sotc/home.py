from pyramid.view import view_config
from os.path import join
from tof import templates

@view_config(route_name='sotc_home', renderer=join(templates, 'sotc', 'home.pt'))
def view_wiki(request):
    return {}
    # return HTTPFound(location = request.route_url('view_sotc'))
