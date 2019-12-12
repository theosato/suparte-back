from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from dao import db, Base
import json 
import os

################################################## M O D E L S ##################################################

# pedido_item = db.Table('pedido_item',
#     db.Column('pedido_id', db.Integer, db.ForeignKey('pedidos.id'), primary_key=True),
#     db.Column('item_id', db.Integer, db.ForeignKey('itens.id'), primary_key=True)
# )

class User(Base):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=False)
    cpf = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(120), unique=True)
    endereco = db.Column(db.String(200), unique=False)
    telefone = db.Column(db.String(40), unique=False)
    artista = db.Column(db.Boolean, unique=False)
    # pedidos_id = Column(Integer, ForeignKey('pedidos.id'))
    # pedidos = db.relationship('Pedidos', backref='usuarios', lazy=True)
    # itens = db.Column(db.ARRAY(db.relationship('Item', secondary="pedido_item", lazy='subquery',
    #     backref=db.backref('pedidos', lazy=True))))
    def __init__(self, nome, email, cpf, endereco, telefone, artista):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone
        self.artista = artista
        # self.pedidos = pedidos

    def to_dict(self):
        response = {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "cpf": self.cpf,
            "endereco": self.endereco,
            "telefone": self.telefone,
            "artista": self.artista
            # "pedidos": self.pedidos
        }
        
        return response

class Item(Base):
    __tablename__ = 'itens'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False)
    description = db.Column(db.String(300), unique=False)
    price = db.Column(db.String(25), unique=False)
    author = db.Column(db.String(100), unique=False)
    photo = db.Column(db.String(500), unique=False)
    # pedido_id = db.Column(db.Integer, db.ForeignKey('pedidos.id'),
    #     nullable=False)

    def __init__(self, name, description, price, author, photo):
        self.name = name
        self.description = description
        self.price = price
        self.author = author
        self.photo = photo

    def to_dict(self):
        response = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "author": self.author,
            "photo": self.photo
        }
        
        return response

class Pedidos(Base):

    __tablename__ = 'pedidos'

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime, nullable=False)
    codigo = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(25), unique=False)
    # itens = db.Column(db.ARRAY(db.relationship('Item', secondary="pedido_item", lazy='subquery',
    #     backref=db.backref('pedidos', lazy=True))))
    # itens = db.relationship('Item', backref='pedidos', lazy=True)

    def __init__(self, data, codigo, status, user_id):
        self.data = data
        self.codigo = codigo
        self.status = status
        self.user_id = user_id
        # self.itens = itens

    def to_dict(self):
        response = {
            "id": self.id,
            "user_id": self.user_id,
            # "itens": self.itens,
            "data": self.data,
            "codigo": self.codigo,
            "status": self.status
        }
        
        return response
