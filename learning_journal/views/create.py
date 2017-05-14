from pyramid.view import view_config

@view_config(route_name='action', match_param='action=create', renderer='string')
def create_page(request):
    return "create page"
