import socket
import time

def get_tcp_latency(ip):
    start_time = time.time() #check tcp
    try:
        sock = socket.create_connection((ip, 80), timeout=5)
        latency = round((time.time() - start_time) * 1000, 2)  # see in ms
        return f"{latency} ms"
    except socket.timeout:
        return "Connection Timeout"
    except socket.error:
        return "Connection Failed"
print(get_tcp_latency("50.17.247.9"))