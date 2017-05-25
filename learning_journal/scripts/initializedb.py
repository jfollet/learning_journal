import os
import sys

import transaction
from pyramid.paster import (
    get_appsettings,
    setup_logging,
)
from pyramid.scripts.common import parse_vars

from ..models import User, password_context, Entry
from ..models import (
    get_engine,
    get_session_factory,
    get_tm_session,
)
from ..models.meta import Base


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)

    if 'DATABASE_URL' in os.environ:
        settings['sqlalchemy.url'] = os.environ['DATABASE_URL']

    engine = get_engine(settings)
    Base.metadata.create_all(engine)

    session_factory = get_session_factory(engine)

    with transaction.manager:
        dbsession = get_tm_session(session_factory, transaction.manager)

        # password = os.environ.get('ADMIN_PASSWORD', 'admin')
        # username = 'admin'
        # encrypted = password_context.encrypt(password)
        # user = User(username=username, password=encrypted)
        # dbsession.add(user)

        entry1 = Entry(title="My first python entry.", body="I learned something!")
        entry2 = Entry(title="Second Entry", body="Python give you wings!")
        entry3 = Entry(title="Third Entry", body="Python makes web creation fun!")
        dbsession.add(entry1)
        dbsession.add(entry2)
        dbsession.add(entry3)
