from datetime import datetime

from app.extends import db


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    auther = db.Column(db.String(60))
    body = db.Column(db.Text)
    add_time = db.Column(db.DateTime, default=datetime.utcnow)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))

    replay_id = db.Column(db.Integer, db.ForeignKey("comment.id"))
    replys = db.relationship("Comment", back_populates="replyd", cascade='all, delete-orphan')
    replyd = db.relationship("Comment", back_populates="replys", remote_side=[id])
