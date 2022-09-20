from flask import Blueprint, render_template, request, redirect

from models.order import Order
from utils.db import db

orders = Blueprint('orders', __name__)


@orders.route('/')
def hello():
    # orders = Order.query.all()
    page = request.args.get('page', 1, type=int)
    try:
        orders = Order.query.paginate(page=page, per_page=3)
    except:
        orders = Order.query.paginate(page=1, per_page=3)
        return render_template('index.html', orders=orders)

    # if page > orders.pages:
    #     orders = Order.query.paginate(page=1, per_page=3)
    #     return render_template('index.html', orders=orders)

    # if orders is None:
    #     return render_template('orders.html', orders=[])

    for recorrer in orders.items:
        print('numero de orden', recorrer.order_number, 'id', recorrer.id)

    return render_template('index.html', orders=orders)


@orders.route('/new', methods=['POST'])
def add_order():
    order_number = request.form['order_number']
    new_order = Order(order_number)

    db.session.add(new_order)
    db.session.commit()

    return redirect('/')

# @orders.route('/buscar', methods=['GET'])
# def pagina_buscar():
#     return render_template('buscar.html')


# @orders.route('/busqueda', methods=['POST'])
# def buscar():
#     order_number = request.form['order_number']
#     print(order_number)
# consult_orders = Order.query.filter_by(order_number=order_number).first()


# def consult_order(consult_orders):
#     print("print consult_orders", consult_orders)
# return render_template('consult.html', orders=consult_orders)
