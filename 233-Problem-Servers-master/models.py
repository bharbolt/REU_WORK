from google.appengine.ext import db

class Submission(db.Model):
    student_magic_number = db.StringProperty(required=True)
    score = db.FloatProperty(required=True)
    answered_on = db.DateTimeProperty(required=True,auto_now_add=True)
    problem_id = db.IntegerProperty(required=True)
    level = db.IntegerProperty(required=True)
    type = db.StringProperty(required=True)
    answer = db.StringProperty()

class WebHomework(db.Model):
    name = db.StringProperty(required=True)
    viewable = db.BooleanProperty(required=True)
    duedate = db.DateTimeProperty(required=True)
    questions = db.TextProperty(required=True)


