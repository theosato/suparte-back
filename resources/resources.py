from flask import Flask, request, jsonify
from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import json 
import os
import app

################################################## R O U T E S ##################################################
class Resources(Resource):
############## U S E R #############
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

    ############# I T E M #############

    # endpoint to create new item
    @app.route("/item", methods=["POST"])
    def add_item():
        name = request.json['name']
        description = request.json['description']
        price = request.json['price']
        author = request.json['author']
        photo = request.json['photo']
        # pedido_id = request.json['pedido_id']

        new_item = Item(name, description, price, author, photo)

        db.session.add(new_item)
        db.session.commit()
        
        response = new_item.to_dict()
        return response 

    # endpoint to show all items
    @app.route("/item", methods=["GET"])
    def get_item():
        all_items = User.query.all()
        dict_result = {}
        for entry in all_items:
            user_dict = entry.to_dict()
            dict_result[user_dict['id']] = user_dict

        return json.loads(json.dumps(dict_result))

    # endpoint to get item detail by id
    @app.route("/item/<id>", methods=["GET"])
    def item_detail(id):
        item = Item.query.get(id)
        response = item.to_dict()
        return response 

    # endpoint to update item
    @app.route("/item/<id>", methods=["PUT"])
    def item_update(id):
        item = Item.query.get(id)
        
        if 'name' in request.json.keys():
            item.name = request.json['name']
        
        if 'description' in request.json.keys():
            item.description = request.json['description']

        if 'price' in request.json.keys():
            item.price = request.json['price']

        if 'author' in request.json.keys():
            item.author = request.json['author']

        if 'photo' in request.json.keys():
            item.photo = request.json['photo']

        db.session.commit()
        return item_schema.jsonify(item)


    # endpoint to delete item
    @app.route("/item/<id>", methods=["DELETE"])
    def item_delete(id):
        item = Item.query.get(id)
        db.session.delete(item)
        db.session.commit()

        return item_schema.jsonify(item)

    ############# P E D I D O ##############
    import random    
    # endpoint pra criar novo pedido
    @app.route("/pedido", methods=["POST"])
    def add_pedido():
        user_id = request.json['user_id']
        # itens = request.json['itens']
        codigo = random.getrandbits(30)
        data = request.json['data']
        status = request.json['status']
        
        new_pedido = Pedidos(user_id,itens)

        db.session.add(new_pedido)
        db.session.commit()
        
        response = new_pedido.to_dict()
        return response 

    # endpoint to show all pedidos
    @app.route("/pedido", methods=["GET"])
    def get_pedido():
        all_pedidos = Pedidos.query.all()
        dict_result = {}
        for entry in all_pedidos:
            pedido_dict = entry.to_dict()
            dict_result[pedido_dict['id']] = pedido_dict

        return json.loads(json.dumps(dict_result))

    # endpoint pra pegar pedido pelo id
    @app.route("/pedido/<id>", methods=["GET"])
    def pedido_detail(id):
        pedido = Pedidos.query.get(id)
        response = pedido.to_dict()
        return response 

    # endpoint pra atualizar pedido
    @app.route("/pedido/<id>", methods=["PUT"])
    def pedido_update(id):
        pedido = Pedidos.query.get(id)

        if 'user_id' in request.json.keys():
            pedido.user_id = request.json['user_id']
        
        if 'data' in request.json.keys():
            pedido.data = request.json['data']

        if 'status' in request.json.keys():    
            pedido.status = request.json['status']

        db.session.commit()
        return pedido_schema.jsonify(pedido)


    # endpoint to delete user
    @app.route("/pedido/<id>", methods=["DELETE"])
    def pedido_delete(id):
        pedido = Pedidos.query.get(id)
        db.session.delete(pedido)
        db.session.commit()

        return pedido_schema.jsonify(pedido)

    ############################################################################################################