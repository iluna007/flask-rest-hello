from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorite_planets = db.relationship('Favorite_Planets', backref='user', lazy=True)
    favorite_people = db.relationship('Favorite_People', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "password": self.password,
            # do not serialize the password, its a security breach
            "is_active": self.is_active,
            "favorite_planets": list(map(lambda x: x.serialize(), self.favorite_planets)),
            "Favorite_People": list(map(lambda x: x.serialize(), self.favorite_people)),
        }

    
class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    last_name = db.Column(db.String(120), unique=True, nullable=False)
    birth_day = db.Column(db.String(80))
    gender = db.Column(db.String(80))
    favorite_people = db.relationship('Favorite_People', backref='people', lazy=True)

    def __repr__(self):
        return '<People %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            "birth_day": self.birth_day,
            "gender": self.gender,            
        }  

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    size = db.Column(db.String(120), unique=True, nullable=False)
    population = db.Column(db.Integer)
    galaxy = db.Column(db.String(120))
    favorite_planets = db.relationship('Favorite_Planets', backref='planet', lazy=True)

    def __repr__(self):
        return '<Planets %r>' % self.name
        
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "size": self.size,
            "population": self.population,
            "galaxy": self.galaxy,
        }
   
class Favorite_People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'), nullable=False)

    def __repr__(self):
        return '<Favorite_People %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "people_id": self.people_id
        }
    
class Favorite_Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'), nullable=False)

    def __repr__(self):
        return '<Favorite_Planet %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planets_id": self.planets_id,
        }
