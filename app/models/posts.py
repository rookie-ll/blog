from datetime import datetime

from app.extends import db


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rid = db.Column(db.Integer, index=True, default=0)
    content = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    u_id = db.Column(db.Integer, db.ForeignKey("users.id"))
