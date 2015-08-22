from default import db

class Institutes(db.Model):

    __tablename__ = 'institutes'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __repr__(self):
        return '<title {}'.format(self.title)
