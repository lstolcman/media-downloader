import config
from flask import Flask

app = Flask(__name__)

import os
import sys
if os.environ.get('ENV') == 'prod':
    app.config.from_object('config.prod')
    print('Production mode', file=sys.stderr)
else:
    app.config.from_object('config.dev')
    print('THIS APP IS IN DEBUG MODE. YOU SHOULD NOT SEE THIS IN PRODUCTION', file=sys.stderr)
    print('THIS APP IS IN DEBUG MODE. YOU SHOULD NOT SEE THIS IN PRODUCTION', file=sys.stderr)
    print('THIS APP IS IN DEBUG MODE. YOU SHOULD NOT SEE THIS IN PRODUCTION', file=sys.stderr)
    print('export/set ENV=prod to avoid', file=sys.stderr)

print('DEBUG={}'.format(app.config['DEBUG']), file=sys.stderr)
print('TESTING={}'.format(app.config['TESTING']), file=sys.stderr)
print('ENV={}'.format(os.environ.get('ENV')), file=sys.stderr)
print('HOST={}'.format(app.config['HOST']), file=sys.stderr)
print('PORT={}'.format(app.config['PORT']), file=sys.stderr)
print('SSL_CONTEXT={}'.format(app.config['PORT']), file=sys.stderr)

from app import routes

