from flask import Flask, render_template, redirect, request, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from models import db, Restaurant
from forms import RestaurantForm, SearchForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myapp.db'
app.config['SECRET_KEY'] = 'mysecretkey'

db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/restaurants')
def list_restaurants():
    restaurants = Restaurant.query.all()
    return render_template('restaurants.html', restaurants=restaurants)

@app.route('/restaurants/<int:id>/delete', methods=['POST'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        db.session.delete(restaurant)
        db.session.commit()
        flash('Ресторан удален успешно', 'success')
    else:
        flash('Ресторан не найден', 'danger')
    return redirect('/restaurants')

@app.route('/restaurants/<int:id>/edit', methods=['GET', 'POST'])
def edit_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        flash('Ресторан не найден', 'danger')
        return redirect('/restaurants')

    form = RestaurantForm(obj=restaurant)
    if form.validate_on_submit():
        form.populate_obj(restaurant)
        db.session.commit()
        flash('Ресторан обновлен успешно', 'success')
        return redirect('/restaurants')

    return render_template('edit_restaurant.html', form=form, restaurant=restaurant)

@app.route('/search', methods=['GET', 'POST'])
def search_restaurants():
    form = SearchForm()
    restaurants = []

    if form.validate_on_submit():
        specialization = form.specialization.data
        restaurants = Restaurant.query.filter_by(specialization=specialization).all()

    return render_template('search.html', form=form, restaurants=restaurants)

@app.route('/restaurants/add', methods=['GET', 'POST'])
def add_restaurant():
    form = RestaurantForm()
    if form.validate_on_submit():
        restaurant = Restaurant(
            name=form.name.data,
            specialization=form.specialization.data,
            address=form.address.data,
            website=form.website.data,
            phone=form.phone.data
        )
        db.session.add(restaurant)
        db.session.commit()
        flash('Ресторан добавлен успешно', 'success')
        return redirect('/restaurants')

    return render_template('add_restaurant.html', form=form)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
