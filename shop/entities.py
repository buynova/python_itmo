from pony.orm import Database, Required, Optional, Set

db = Database()


class Category(db.Entity):
    """Категория товара."""
    parent = Optional('Category', reverse='children')
    children = Set('Category', reverse='parent')
    title = Required(str)
    description = Optional(str)


class Product(object):
    """Товар магазина."""
    title = ''
    category = Category
    price = 0.0
    description = ''
    article = 0
    comments = []


class Customer(object):
    """Покупатель."""
    name = ''
    email = ''
    phone = ''
    login = ''
    password = ''
    address = ''  # может быть сущностью


class Comment(object):
    """Комментарий."""
    product = Product
    customer = Customer
    text = ''
    rating = 0
    created = 0
    deletable = True


class OrderItem(object):
    """Одна позиция в заказе."""
    product = Product
    amount = 0


class Order(object):
    """Заказ."""
    customer = Customer
    products = [OrderItem, OrderItem, ...]
    created = 0
    promo_code = ''


class Status(object):
    """Статус заказа."""
    name = ''


class OrderLog(object):
    """История изменения заказа."""
    order = Order
    status = Status
    created = 0  # дата изменения статуса


class Cart(object):
    """Корзина."""
    customer = Customer
    products = [OrderItem, OrderItem, ...]
