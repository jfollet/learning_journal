import os

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from .forms import EntryForm
from ..models import Entry

@view_config(route_name='action', match_param='action=create', renderer='templates/edit.jinja2', permission='create')
def create_page(request):
    entry = Entry()
    form = EntryForm(request.POST)

    if request.method == 'POST' and form.validate():
        form.populate_obj(entry)
        request.dbsession.add(entry)
        return HTTPFound(location=request.route_url('home'))
    return {'form': form, 'action': request.matchdict.get('action')}
