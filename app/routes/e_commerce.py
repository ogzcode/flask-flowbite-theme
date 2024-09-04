from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required
from faker import Faker
from app.models import Product

e_commerce_routes = Blueprint('e_commerce_routes', __name__)

@e_commerce_routes.route('/e-commerce/product-list', methods=['GET'])
@login_required
def product_list():
    return render_template('pages/e-commerce/product-list.html')


@e_commerce_routes.route('/e-commerce/product-list/data', methods=['GET'])
@login_required
def product_list_data():
    PER_PAGE = 10
    search = request.args.get('search')
    sort_by = request.args.get('sort_by', "id")
    sort_order = request.args.get('sort_order', "asc")
    page = int(request.args.get('page', 1))
    start = (page - 1) * PER_PAGE
    end = start + PER_PAGE

    products = Product.query

    if search:
        products = products.filter(Product.name.ilike(f"%{search}%"))
    
    if sort_order == "asc":
        products = products.order_by(getattr(Product, sort_by).asc())

    if sort_order == "desc":
        products = products.order_by(getattr(Product, sort_by).desc())

    products = products = products.offset((page - 1) * PER_PAGE).limit(PER_PAGE).all()

    data = []

    for product in products:
        data.append({
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'stock': product.stock,
            'category': product.category,
        })

    return jsonify({
        'data': data,
        'total': Product.query.count(),
        'page': page,
        "from": start,
        "to": end,
        "headers": [
            {"text": "Name", "value": "name"},
            {"text": "Description", "value": "description"},
            {"text": "Price", "value": "price"},
            {"text": "Stock", "value": "stock"},
            {"text": "Category", "value": "category"},
        ]
    })