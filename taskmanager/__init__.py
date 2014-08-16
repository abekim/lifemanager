from flask import Flask, render_template, jsonify, request
from flask.ext.mongoengine import MongoEngine

# initialize app
app = Flask(__name__)

# configurations

# enable to allow debugging
app.debug = True

app.config["MONGODB_SETTINGS"] = {
    'DB': 'Tasks'
}

if not app.debug:
    import logging
    stream_handler = logging.StreamHandler()
    app.logger.addHandler(stream_handler)
    app.logger.setLevel(logging.DEBUG)

# initialize db
db = MongoEngine(app)

# import models
from taskmanager.models import Task

# routes
@app.route("/")
def hello():
    return render_template("index.html", title="Welcome", tasks=Task.objects())

@app.route("/new", methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        app.logger.info("New task, \"%s\" added", request.form['description'])
        description = request.form['description']

        t = Task(description=description)

        t.save()
    return jsonify(data=t)
