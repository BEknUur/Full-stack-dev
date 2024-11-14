import socket
def check_port(ip,port):
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(1)
    result=sock.connect_ex((ip,port))
    if result==0:
        print(f"Port {port}on {ip} is open")
    else:
        print(f"Port {port} on {ip}is closed")
    sock.close()

check_port('127.0.0.1',22)
check_port('127.0.0.1',80)
check_port('127.0.0.1',3306)
