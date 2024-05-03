"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, Planets, Favorite_Planets, Favorite_People
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

####################END POINTS: ########################################

####################################################################GET /user

@app.route('/user', methods=['GET'])
def get_users():

    all_users = User.query.all()
    users = list(map(lambda element:element.serialize(), 
    all_users))

    return jsonify(users), 200

####################################################################GET /user/<int:user_id>

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    return jsonify(user.serialize()), 200

####################################################################GET /user/<int:user_id>

@app.route('/people', methods=['GET'])
def get_people():

    all_people = People.query.all()
    people = list(map(lambda element:element.serialize(), 
    all_people))
   
    return jsonify(people), 200
####################################################################GET /user/<int:user_id>

@app.route('/people/<int:people_id>', methods=['GET'])
def get_person(people_id):
    person = People.query.filter_by(id=people_id).first()
    return jsonify(person.serialize()), 200
####################################################################GET /planets

@app.route('/planets', methods=['GET'])
def get_planets():

    all_planets = Planets.query.all()
    planets = list(map(lambda element:element.serialize(), 
    all_planets))
   
    return jsonify(planets), 200
####################################################################GET /planets/<int:planet_id>

@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    planet = Planets.query.filter_by(id=planet_id).first()
    return jsonify(planet.serialize()), 200
####################################################################GET /favorites/planet

@app.route('/favorites/planets/<int:favorite_id>', methods=['GET'])
def get_favorite_planets(favorite_id):
    all_favorite_planets = Favorite_Planets.query.filter_by(id=favorite_id).all()
    results = list(map(lambda element:element.serialize(), all_favorite_planets))

    return jsonify(results), 200
####################################################################GET /user/<int:user_id>/favorites

@app.route('/user/<int:user_id>/favorite_planets', methods=['GET'])
def get_user_favorite_planets(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({"error": "User not found"}), 404

    favorite_planets = [favorite_planets.serialize() for favorite_planets in user.favorite_planets]
    return jsonify(favorite_planets), 200

####################################################################GET /user/<int:user_id>/favorites

@app.route('/user/<int:user_id>/favorite_people', methods=['GET'])
def get_user_favorite_people(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({"error": "User not found"}), 404

    favorite_people = [favorite_people.serialize() for favorite_people in user.favorite_people]
    return jsonify(favorite_people), 200

####################################################################GET /favorites/people

@app.route('/favorites/people/<int:favorite_id>', methods=['GET'])
def get_favorite_people(favorite_id):
    all_favorite_people = Favorite_People.query.filter_by(id=favorite_id).all()
    results = list(map(lambda element:element.serialize(), all_favorite_people))

    return jsonify(results), 200

####################################################################POST /favorites/planet

@app.route('/favorites/planets', methods=['POST'])
def add_favorite_planet():
    print(request.get_json())
    user_id = request.get_json()['user_id']
    planet_id = request.get_json()['planet_id']

    favorite_planets = Favorite_Planets(user_id = user_id, planets_id = planet_id)
    db.session.add(favorite_planets)
    db.session.commit()

    response_body = {
       'message': 'Se agrego planeta favorito'
    }

    return jsonify(response_body), 200

####################################################################POST /favorites/people

@app.route('/favorites/people', methods=['POST'])
def add_favorite_people():
    print(request.get_json())
    user_id = request.get_json()['user_id']
    people_id = request.get_json()['people_id']

    favorite_people = Favorite_People(user_id = user_id, people_id = people_id)
    db.session.add(favorite_people)
    db.session.commit()

    response_body = {
       'message': 'La persona se agregó a favoritos'
    }

    return jsonify(response_body), 200

####################################################################DELETE /favorites/planet
@app.route('/favorites/people/delete/<int:people_id>', methods=['DELETE'])
def delete_favorite_people(people_id):
    delete = Favorite_People.query.filter_by(id=people_id).first()

    if delete:
        
        db.session.delete(delete)
        db.session.commit()

        response_body = {
           'message': 'La persona se eliminó de favoritos correctamente'
        }
        return jsonify(response_body), 200
    else:
        response_body = {
           'message': 'El favorito no existe'
        }
        return jsonify(response_body), 404
    
####################################################################DELETE /favorites/people

@app.route('/favorites/planet/delete/<int:planet_id>', methods=['DELETE'])
def delete_favorite_planet(planet_id):
    delete = Favorite_Planets.query.filter_by(id=planet_id).first()

    if delete:
        
        db.session.delete(delete)
        db.session.commit()

        response_body = {
           'message': 'El planeta se eliminó de favoritos correctamente'
        }
        return jsonify(response_body), 200
    else:
        response_body = {
           'message': 'El favorito no existe'
        }
        return jsonify(response_body), 404
    
####################################################################


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
