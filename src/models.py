from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorites = db.Column(db.String(120), unique=False, nullable=False)
   # favorite_planets = db.relationship('Favorite_Planets', backref='user', lazy='true')
   # favorite_people = db.relationship('Favorite_People', backref='user', lazy='true')
                                      


    def __repr__(self):
        return '<Users %r>' % self.usersname

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "password": self.password,
            "is_active": self.email,
            "favorites": self.favorites
            # do not serialize the password, its a security breach
        }
    
class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    last_name = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<People %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            
            # do not serialize the password, its a security breach
        }  

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    size = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Planets %r>' % self.name
        
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "size": self.size,

            
            # do not serialize the password, its a security breach
        }
   
class Favorite_People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    last_name = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Planets %r>' % self.name
        
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "size": self.size,
            
            # do not serialize the password, its a security breach
        }
    
class Favorite_Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Planets %r>' % self.name
        
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "size": self.size,
            
            # do not serialize the password, its a security breach
        }
