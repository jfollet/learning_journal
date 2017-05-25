from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from pyramid.view import view_config

from .forms import EntryForm
from ..models import Entry


@view_config(route_name='action', match_param='action=edit', renderer='templates/edit.jinja2', permission='edit')
def edit_page(request):
    this_id = int(request.params.get('id', -1))
    entry = Entry.by_id(this_id, request.dbsession)
    if not entry:
        return HTTPNotFound()

    form = EntryForm(request.POST, entry)
    if request.method == 'POST' and form.validate():
        form.populate_obj(entry)
        return HTTPFound(location=request.route_url('detail', id=entry.id))

    return {'form': form, 'action': request.matchdict.get('action')}
