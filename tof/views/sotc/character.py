from pyramid.view import view_config
from os.path import join
from tof import templates
from tof.models.sotc.character import SotCCharacter

def get_characters(context):
    characters = SotCCharacter.find_all()
    return characters

@view_config(route_name='sotc_character', renderer=join(templates, 'sotc', 'character.pt'))
def view_character(context, request):
    return dict( 
		characters = get_characters(context)
	)
    # return HTTPFound(location = request.route_url('view_sotc'))
