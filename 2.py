import socket
import threading
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0',2222))
s.listen(10)

def server(conn):
    while True:
        data = conn.recv(1024)
        if not data: break
        if data == b"close": break
        conn.send(data)
    conn.close()


while True:
    conn, addr = s.accept()
    t = threading.Thread(target=server, args=(conn, ))
    t.start()
s.close()
