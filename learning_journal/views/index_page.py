from pyramid.view import view_config

from ..models import Entry


@view_config(route_name='home', renderer='templates/list.jinja2')
def index_page(request):
    return {'entries': Entry.all(request.dbsession)}
