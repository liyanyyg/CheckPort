import socket
def check_port(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('127.0.0.1', port)) == 0

ports = [80, 443, 8080, 3000]
for p in ports:
    status = "占用" if check_port(p) else "空闲"
    print(f"端口 {p}: {status}")
