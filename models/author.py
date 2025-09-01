from src.database import db

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    nationality = db.Column(db.String(100), nullable=False)
    birth_year = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Author {self.name}>'


