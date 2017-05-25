from pyramid.httpexceptions import HTTPNotFound
from pyramid.view import view_config

from ..models import Entry


@view_config(route_name='detail', renderer='templates/detail.jinja2', permission='view')
def detail_page(request):
    this_id = request.matchdict.get('id', -1)
    entry = Entry.by_id(this_id, request.dbsession)

    if not entry:
        return HTTPNotFound()
    return {'entry': entry}
