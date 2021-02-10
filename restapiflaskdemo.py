# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 10:51:23 2021

@author: SHALINICHAKRABORTY

app = express()

app.get('',())
app.post('',())
"""

import json
from flask import Flask,jsonify,request,Response,make_response
from flask_sqlalchemy import SQLAlchemy

from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields


app = Flask(__name__)

app.config['SQL_ALCHEMY_DATABASE_URI']='mysql+pymysql://admin:admin@localhost:3306/devops'

db = SQLAlchemy(app)

class Product(db.Model):
    __tablename__="pyproducts"
    productId = db.Column(db.Integer,primary_key=True)
    productName = db.Column(db.String(40))
    description = db.Column(db.String(40))
    productCode = db.Column(db.String(40))
    price = db.Column(db.Float)
    starRating=db.column(db.Float)
    imageUrl = db.Column(db.String(40))
    
    
    def create(self):
        db.session.add(self)
        db.session.commit(self)
        return self
    
    def __init__(self,productName,description,productCode,price,starRating,imageUrl):
        self.productName = productName
        self.description = description
        self.productCode= productCode
        self.price=price
        self.starRating=starRating
        self.imageUrl=imageUrl
    
    def __repr__(self):
        return "%self.productId"
    
db.create_all()

# class ProductSchema(ModelSchema):
#     class Meta(ModelSchema.Meta):
#         model = Product
#         sqla_session = db.session
#     productId = fields.Number(dump_only=True)
#     productName = fields.String(required=True)
#     description = fields.String(required= True)
#     productCode = fields.String(required= True)
#     price = fields.Number(required=True)
#     starRating = fields.Number(required=True)
#     imageUrl=fields.String(required=True)
    
# @app.route('/products',methods=['POST'])
# def createProduct():
#     data = request.get_json()
#     product_schema=ProductSchema()
#     product = product_schema.load(data)
#     result = product_schema.dump(product.create())
#     return make_respomse(jsonify({"product":result}),201)
# app.get(port=4000)

@app.route('/products/find/<productName>',method=['GET'])
def getProductsByName(productName):
    get_products=Product.query.filter_by(productName=productName)
    productSchema=ProductSchema(many=True)
    products=productSchema.dump(get_products)
    return make_response(jsonify({"product":products}),200)

app.run(port=4002)



    
    
            
    

    
    




