from flask import Flask
from routes.orders import orders
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__, static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost:3306/ordersdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SQLAlchemy(app)
app.register_blueprint(orders)