from pyramid.view import view_config

@view_config(route_name='action', match_param='action=edit', renderer='string')
def edit_page(request):
    return "edit page"
