from app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(120), index=True, unique=True)
    price = db.Column(db.Float)
    stock = db.Column(db.Integer)
    category = db.Column(db.String(64), index=True)

    def __repr__(self):
        return '<Product {}>'.format(self.name)
    

