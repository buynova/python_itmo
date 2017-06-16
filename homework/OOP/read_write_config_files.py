"""
=====================
Функциональный подход
=====================

При таком подходе в модуле main могут находиться только основные функции read_params() и write_params(),
а внутри них будут вызываться соотвествующие каждому формату функции.
Эти конкретные функции (read_json_params, read_xml_params и т.д.) могут находиться в другом модуле,
причем организовать структуру этих модулей можно разными способами, например, группировать функции по действию
(запись, чтение), либо по формату (тогда в модуле каждого формата будет функция чтения и функция записи).

Примерная структура пакета (1):
- main.py
  - read_params()
  - white_params()
- json_actions.py
  - read_json_params()
  - write_json_params()
- xml_actions.py
  - read_xml_params()
  - write_xml_params()
- <some_format>_actions.py
...

(2):
- main.py
  - read_params()
  - white_params()
- read_formats.py
  - read_json_params()
  - read_xml_params()
  - ...
- write_formats.py
  - write_json_params()
  - write_xml_params()
  - ...

"""

def read_params(source):
    file_format =  ''# узнать формат файла конфига
    if file_format == 'json':  # к примеру, формат файла - json
        return read_json_params(source)  # вызов соответствующей функции
    elif file_format == 'xml':
        return read_xml_params(source)
    # и так далее, можно добавлять форматы

def white_params(source, params):
    file_format =  ''# узнать формат файла конфига
    if file_format == 'json':  # к примеру, формат файла - json
        write_json_params(source_params)
    # и т.д.


"""
==========
Подход ООП
==========

Думаю, можно реализовать похожий механизм: на каждый формат создавать свой класс с действиями "чтение" и "запись"
В таком случае в конечном итоге может получиться много разных классов.
Если это нежелательно, можно создать два класса: Reader и Writer, а в каждом из них свой метод для каждого формата.
"""

class Reader(object):

    def read_config(self, source):
        file_format = ''  # здесь определяем формат (например, с помощью регулярного выражения или сплита)
        if file_format == 'json':
            return self.read_json_params(source)
        elif file_format == 'xml':
            return self.read_xml_params(source)

    def read_json_params(self, source):
        # some actions
        return params

    def read_xml_params(self, source):
        # some actions
        return params

    # и т.д.


class Writer(object):

    def write_config_params(self, source, params):
        file_format = ''  # здесь определяем формат (например, с помощью регулярного выражения или сплита)
        if file_format == 'json':
            self.write_json_params(source, params)
        elif file_format == 'xml':
            self.write_xml_params(source, params)

    def write_json_params(self, source, params):
        # some actions

    def write_xml_params(self, source, params):
        # some actions

    # и т.д.


Writer.write_config_params(source, params)
print(Reader.read_config(source))

