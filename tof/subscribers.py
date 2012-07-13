from pyramid.renderers import get_renderer

def add_base_template(event):
    sotc = get_renderer('templates/sotc.pt').implementation()
    event.update({'sotc': sotc})
