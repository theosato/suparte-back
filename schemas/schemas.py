from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema
import json 
import os

from models.models import *

################################################## S C H E M A ##################################################

class ItemSchema(ModelSchema):
   
    class Meta:
        # Fields to expose
        fields = ('name', 'description', 'price', 'author', 'photo')


item_schema = ItemSchema()
items_schema = ItemSchema(many=True)

class PedidoSchema(ModelSchema):

    itens = fields.Nested(ItemSchema, many=True)

    class Meta:
        # Fields to expose
        fields = ('id', 'data', 'codigo', 'status', 'user_id')


pedido_schema = PedidoSchema()
pedidos_schema = PedidoSchema(many=True)

class UserSchema(ModelSchema):
    
    pedidos = fields.Nested(PedidoSchema, many=True)

    class Meta:
        # Fields to expose
        fields = ('nome', 'email', 'cpf', 'endereco', 'telefone', 'artista')


user_schema = UserSchema()
users_schema = UserSchema(many=True)
# A list of author objects