from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required
from faker import Faker

dashboard_routes = Blueprint('dashboard_routes', __name__)


@dashboard_routes.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    return render_template('pages/dashboard.html')


@dashboard_routes.route('/api/sales-table', methods=['GET'])
@login_required
def sales_table_data():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    start = (page - 1) * per_page
    end = start + per_page


    fake = Faker()
    data = []
    category = ['Electronics', 'Clothing', 'Books', 'Home', 'Garden', 'Toys', 'Beauty', 'Health', 'Automotive', 'Sports']
    for _ in range(10):
        data.append({
            'name': fake.name(),
            'email': fake.email(),
            'phone': fake.phone_number(),
            'amount': fake.random_int(min=1000, max=10000),
            "product": fake.word(ext_word_list=category),
            'date': fake.date_this_year(),
        })

    return jsonify({
        'data': data,
        'total': 1000,
        'page': page,
        "from": start,
        "to": end,
    })

