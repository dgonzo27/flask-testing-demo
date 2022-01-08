from app import db


class Movie(db.Model):
    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(155), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    def __init__(self, title="", description=""):
        self.title = title
        self.description = description
