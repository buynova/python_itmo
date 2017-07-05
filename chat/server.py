import argparse
from datetime import datetime
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

"""
Режим работы:
    - прослушивание входящих соединений
        - висеть постоянно и ждать запроса от клиента
    - вернуть текущее время
        - по факту работать просто как обычный скрипт

echo-server.py listen --ip 192.168.11.1 --port 1234
echo-server.py gettime --city Saint-Petersburg
"""


def gettime(city):
    print('Узнать текущее время в городе:', city)


def listen(ip, port):
    with socket(AF_INET, SOCK_STREAM) as s:  # IPv4 TCP Socket
        s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        s.bind((ip, port))  # заняли указанный адрес
        s.listen(1)  # ставим сокет на прослушивание входящих соединений

        while 1:
            conn, addr = s.accept()  # принимает входящее соединение

            with conn:
                # чтение данных из клиентского сокета
                data = conn.recv(2048)
                data = data.decode('utf-8').strip()
                answer = '{now:%Y-%m-%d %H:%M:%S} [{addr}] - {msg}'.format(
                    now=datetime.now(),
                    addr=addr,
                    msg=data
                )
                answer = answer.encode('utf-8')
                conn.send(answer)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Echo-сервер')
    subparsers = parser.add_subparsers()

    parser_gettime = subparsers.add_parser('gettime', help='Текущее время', description='Узнать текущее время')
    parser_gettime.add_argument('-c', '--city', help='Город', required=True)
    parser_gettime.set_defaults(callback=gettime)

    parser_listen = subparsers.add_parser('listen', help='Запустить сервер', description='Запустить сервер времени')
    parser_listen.add_argument('-i', '--ip', default='127.0.0.1', help='IP-адрес сервера')
    parser_listen.add_argument('-p', '--port', default=8080, type=int, help='Порт сервера')
    parser_listen.set_defaults(callback=listen)

    # vars - превращает Namespace в словарь
    arguments = vars(parser.parse_args())

    callback = arguments.pop('callback')  # удаляем из словаря ссылку на функцию
    callback(**arguments)
