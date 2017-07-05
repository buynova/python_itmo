import argparse
import socket

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Клиент для Echo-сервера')

    parser.add_argument('-i', '--ip', default='127.0.0.1', help='IP-адрес серсера')
    parser.add_argument('-p', '--port', default=8080, type=int, help='Порт сервера')

    arguments = parser.parse_args()

    while 1:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((arguments.ip, arguments.port))
            data = input('Введите данные')
            s.send(data.encode('utf-8'))
            answer = s.recv(2048).decode('utf-8')
            print(answer)
