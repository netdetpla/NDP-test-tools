import socket


def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', 10201))
    s.listen(1)
    while True:
        client_sock, client_addr = s.accept()
        recv_json = b''
        while True:
            buf = client_sock.recv(1024)
            if buf:
                recv_json += buf
            else:
                break
        client_sock.close()
        print('receive json: ' + recv_json.decode())


if __name__ == '__main__':
    server()
