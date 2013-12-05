from pyramid.view import view_config


@view_config(route_name='contactus', renderer='contactus.mako')
def contactus(request):
   return {'title': 'Contact Us'}


@view_config(route_name='calendar', renderer='calendar.mako')
def calendar(request):
   return {'title': 'Calendar'}

@view_config(route_name='orgs', renderer='orgs.mako')
def orgs(request):
     return {'title': 'Organizations'}


@view_config(route_name='home', renderer='home.mako')
def home(request):
    return {'title' : 'Home'}