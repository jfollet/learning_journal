from pyramid.view import view_config

from ..models import Entry
from pyramid.security import authenticated_userid
from .forms import LoginForm

@view_config(route_name='home', renderer='templates/list.jinja2', permission='view')
def index_page(request):
    form = None
    if not authenticated_userid(request):
        form = LoginForm()
    return {'entries': Entry.all(request.dbsession), 'form': form}
