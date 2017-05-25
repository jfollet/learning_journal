from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.security import forget, remember

from .forms import LoginForm
from ..models import User

@view_config(route_name='auth', match_param='action=in', renderer='string', permission='view', request_method='POST')
def login(request):
    login_form = None
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
    if login_form and login_form.validate():
        user = User.by_name(login_form.username.data, request.dbsession)
        if user and user.verify_password(login_form.password.data):
            headers = remember(request, user.username)
        else:
            headers = format(request)
    else:
        headers = forget(request)

    return HTTPFound(location=request.route_url('home'), headers=headers)
