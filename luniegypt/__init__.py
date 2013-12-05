from pyramid.config import Configurator
import os

def project_dir():
    current_file = os.path.abspath(__file__)
    return os.path.dirname(current_file)


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    #settings['mako.directories'] = os.path.join(project_dir(), 'templates')

    config = Configurator(settings=settings)
    #config.include('pyramid_mako')

    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('contactus', '/contactus')
    config.add_route('calendar', '/calendar')
    config.add_route('orgs', '/orgs')
    config.scan()
    return config.make_wsgi_app()
