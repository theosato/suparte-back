from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import json 
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)

class User(db.Model):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=False)
    cpf = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(120), unique=True)
    endereco = db.Column(db.String(200), unique=False)
    telefone = db.Column(db.String(40), unique=False)
    artista = db.Column(db.Boolean, unique=False)

    def __init__(self, nome, email, cpf, endereco, telefone, artista):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone
        self.artista = artista

    def to_dict(self):
        response = {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "cpf": self.cpf,
            "endereco": self.endereco,
            "telefone": self.telefone,
            "artista": self.artista
        }
        
        return response

class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('nome', 'email', 'cpf', 'endereco', 'telefone', 'artista')


user_schema = UserSchema()
users_schema = UserSchema(many=True)


# endpoint to create new user
@app.route("/user", methods=["POST"])
def add_user():
    nome = request.json['nome']
    email = request.json['email']
    cpf = request.json['cpf']
    endereco = request.json['endereco']
    telefone = request.json['telefone']
    artista = request.json['artista']

    new_user = User(nome, email, cpf, endereco, telefone, artista)

    db.session.add(new_user)
    db.session.commit()
    
    response = new_user.to_dict()
    return response 

# endpoint to show all users
@app.route("/user", methods=["GET"])
def get_user():
    all_users = User.query.all()
    dict_result = {}
    for entry in all_users:
        user_dict = entry.to_dict()
        dict_result[user_dict['id']] = user_dict

    return json.loads(json.dumps(dict_result))

# endpoint to get user detail by id
@app.route("/user/<id>", methods=["GET"])
def user_detail(id):
    user = User.query.get(id)
    response = user.to_dict()
    return response 

# endpoint to update user
@app.route("/user/<id>", methods=["PUT"])
def user_update(id):
    user = User.query.get(id)

    if 'nome' in request.json.keys():
        user.nome = request.json['nome']
    
    if 'email' in request.json.keys():
        user.email = request.json['email']

    if 'cpf' in request.json.keys():
        user.cpf = request.json['cpf']

    if 'endereco' in request.json.keys():
        user.endereco = request.json['endereco']

    if 'telefone' in request.json.keys():
        user.telefone = request.json['telefone']
    
    if 'artista' in request.json.keys():
        user.artista = request.json['artista']  

    db.session.commit()
    return user_schema.jsonify(user)

# endpoint to delete user
@app.route("/user/<id>", methods=["DELETE"])
def user_delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()

    return user_schema.jsonify(user)


if __name__ == '__main__':
    app.run(debug=True)