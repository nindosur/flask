from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class RestaurantForm(FlaskForm):
    name = StringField('Название', validators=[DataRequired()])
    specialization = StringField('Специализация', validators=[DataRequired()])
    address = StringField('Адрес', validators=[DataRequired()])
    website = StringField('Веб-сайт')
    phone = StringField('Контактный телефон', validators=[DataRequired()])
    submit = SubmitField('Добавить ресторан')

class SearchForm(FlaskForm):
    specialization = StringField('Специализация', validators=[DataRequired()])
    submit = SubmitField('Поиск')
