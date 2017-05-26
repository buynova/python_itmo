# distribution
# файл-манифест

from setuptools import setup

"""
name                - название пакета
url                 - адрес сайта с пакетом
version             - версия пакета (0.0.0)

description         - краткое описание пакета
author              - автор пакета
author_email        - email автора
license             - лицензия

packages            - список пакетов
py_modules          - список модулей вне пакета
scripts             - скрипты
install_requires    - зависимости
"""

setup(
    name='mega-math',
    url='github.com',
    version='1.0.0',
    description='Расширенный математический модуль',
    author='Margarita Buynova',
    author_email='coralfruit@gmail.com',
    license='BSD',
    packages=['mega_math'],
    py_modules=[],
    scripts=[],
    install_requires=[
        'Flask'
    ]
)


# pip - python index package
# pypi.org - туда выкладывать свои пакеты
