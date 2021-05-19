from app import db
from app.models.abstract import BaseModel


class Reaction(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String, nullable=False)
    team_id = db.Column(db.String, nullable=False)
    app_id = db.Column(db.String, nullable=False)
    event_id = db.Column(db.String, nullable=False, unique=True)
    voteder = db.Column(db.String, nullable=False)
    rateder = db.Column(db.String, nullable=False)
    event = db.Column(db.String, nullable=False)
    channel = db.Column(db.String, nullable=False)
    event_datetime = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return "Reaction({})".format(self.token)
