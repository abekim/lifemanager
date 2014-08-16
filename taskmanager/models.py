from taskmanager import db

class Task(db.Document):
    description = db.StringField(required=True)
    completed = db.BooleanField(default=False)
