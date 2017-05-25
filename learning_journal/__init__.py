from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.config import Configurator
from sqlalchemy import engine_from_config
import os


def create_session(settings):
    from sqlalchemy.orm import sessionmaker
    engine = engine_from_config(settings, 'sqlalchemy.')
    Session = sessionmaker(bind=engine)
    return Session()


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    if 'DATABASE_URL' in os.environ:
        settings['sqlalchemy_url'] = os.environ['DATABASE_URL']
    secret = os.environ.get('AUTH_SECRET', 'somesecret')
    config = Configurator(settings=settings,
                          authentication_policy=AuthTktAuthenticationPolicy(secret),
                          authorization_policy=ACLAuthorizationPolicy(),
                          default_permission='view', )
    config.include('pyramid_jinja2')
    config.include('.models')
    config.include('.routes')
    config.scan()
    return config.make_wsgi_app()
