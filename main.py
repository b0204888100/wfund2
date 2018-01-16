import json
import httplib2
import logging 
from googleapiclient import discovery
from google.appengine.api import memcache
from oauth2client.contrib.appengine import AppAssertionCredentials

from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.
INSTANCE_NAME = 'instance-1'
INSTANCE_ZONE = 'asia-east1-b'
PROJECT = 'maximal-port-187809'

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'

@app.route('/vm/start')
def start_vm():
    credentials = AppAssertionCredentials(scope='https://www.googleapis.com/auth/compute')
    http = credentials.authorize(httplib2.Http())
    compute = discovery.build('compute', 'v1', http=http)
    
    # Start the VM!
    result = compute.instances().start(instance=INSTANCE_NAME, zone=INSTANCE_ZONE, project=PROJECT).execute()
    logging.debug(result)
    return json.dumps(result, indent=4)
    
@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
