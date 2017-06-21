from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, TextAreaField, FloatField, SelectField
from pony.orm import db_session

from .models import Category


class EntityField(SelectField):
    def __init__(self, entity_class, label=None, allow_empty=False, empty_text='', **kwargs):
        super().__init__(label, **kwargs)

        with db_session:
            self.choices = [(c.id, c) for c in entity_class.select()]

        if allow_empty:
            empty_value = 0 if self.coerce is int else ''
            self.choices.insert(0, (empty_value, empty_text))


class CategoryForm(FlaskForm):
    id = HiddenField()
    parent = EntityField(Category, 'Категория', allow_empty=True)
    title = StringField('Наименование')
    description = TextAreaField('Описание')
