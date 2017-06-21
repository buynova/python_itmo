from datetime import datetime

from pony.orm import Database, Required, Optional, Set, sql_debug

db = Database()


class Category(db.Entity):
    """Категория товара."""
    parent = Optional('Category', reverse='children')
    children = Set('Category', reverse='parent')
    title = Required(str)
    description = Optional(str)
    products = Set('Product')


class Product(db.Entity):
    """Товар магазина."""
    title = Required(str)
    category = Required(Category)
    price = Required(float)
    description = Optional(str)
    article = Required(int)
    comments = Set('Comment')
    order_items = Set('OrderItem')


class Customer(db.Entity):
    """Покупатель."""
    name = Required(str)
    email = Required(str)
    phone = Required(str)
    login = Required(str)
    password = Required(str)
    address = Optional(str)  # может быть сущностью
    comments = Set('Comment')
    orders = Set('Order')
    cart = Optional('Cart')


class Comment(db.Entity):
    """Комментарий."""
    product = Required(Product)
    customer = Required(Customer)
    text = Required(str)
    rating = Optional(int)
    created = Optional(datetime)


class OrderItem(db.Entity):
    """Одна позиция в заказе."""
    product = Required(Product)
    order = Required('Order')
    amount = Optional(int)


class Order(db.Entity):
    """Заказ."""
    customer = Required(Customer)
    order_items = Set(OrderItem)
    created = Optional(datetime)
    promo_code = Optional(str)
    histories = Set('OrderLog')


class Status(db.Entity):
    """Статус заказа."""
    name = Required(str)
    order_logs = Set('OrderLog')


class OrderLog(db.Entity):
    """История изменения заказа."""
    order = Required(Order)
    status = Required(Status)
    created = Optional(datetime)  # дата изменения статуса


class Cart(db.Entity):
    """Корзина."""
    customer = Required(Customer)
    products = Required(str)  # сериализованный объект


sql_debug(True)
db.bind('sqlite', 'shop.sqlite', create_db=True)
db.generate_mapping(create_tables=True)
