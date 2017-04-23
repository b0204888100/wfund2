from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.
INSTANCE_NAME = 'instance-1'
INSTANCE_ZONE = 'asia-east1-a'
PROJECT = 'esoteric-cider-165206'


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'

@app.route('/vm/start')
def start_vm():
    result = compute.instances().start(instance=INSTANCE_NAME, zone=INSTANCE_ZONE, project=PROJECT).execute()
  
@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
