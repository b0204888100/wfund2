import json
import httplib2
import logging 
from googleapiclient import discovery
from google.appengine.api import memcache
from oauth2client.appengine import AppAssertionCredentials

from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.
INSTANCE_NAME = 'hk01'
INSTANCE_NAME2 = 'hk02'
INSTANCE_ZONE = 'asia-east2-a'
PROJECT = 'continual-loop-166008'

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
    result2 = compute.instances().start(instance=INSTANCE_NAME2, zone=INSTANCE_ZONE, project=PROJECT).execute()
    logging.debug(result)
    logging.debug(result2)
    return json.dumps(result, indent=4)
    return json.dumps(result2, indent=4)
  
@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
