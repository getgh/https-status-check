import json
import socket
import requests
import sys
import time

 def load_domains(json_file): # Loads the list of domains from a JSON file
    try:
        with open(json_file, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading JSON file: {e}")
        return []

def get_ip_address(domain): # Tries to convert a domain name (like example.com) into an IP address
    try:
        ip_list = socket.getaddrinfo(domain, None, socket.AF_INET)  # IPv4 try
        return ip_list[0][4][0]  
    except socket.gaierror:
        return "Unreachable"
#2
```py
def get_status_code(domain):  
    try:
        response = requests.get(f"http://{domain}", timeout=5) #tiemout=parameter
        return response.status_code
    except requests.RequestException:
        return "Failed"

# check connection latency
def get_tcp_latency(ip):
    start_time = time.time()
    try:
        sock = socket.create_connection((ip, 80), timeout=5)
        latency = round((time.time() - start_time) * 1000, 2)  # Convert to ms
        return f"{latency} ms"
    except socket.timeout:
        return "Connection Timeout"
    except socket.error:
        return "Connection Failed"
```
<@696448936864383017>

if len(sys.argv) < 2:
    print("Usage: python script.py <JSON_FILENAME>")
    sys.exit(1)

json_file = sys.argv[1]

# main
def check_domains(json_file):
    """Check and display domain connectivity status using TCP latency."""
    domain_data = load_domains(json_file)

    if not domain_data:
        print("No domain data found.")
        return

    print(f"{'Country':<25} {'Domain':<20} {'IP Address':<20} {'Status Code':<15} {'TCP Latency':<15}")
    print("=" * 100)

    for entry in domain_data:
        country = entry.get("country_name", "Unknown")
        domain = entry.get("domain", "Unknown")

        ip_address = get_ip_address(domain)
        status_code = get_status_code(domain) if ip_address != "Unreachable" else "Skipped"
        tcp_latency = get_tcp_latency(ip_address) if ip_address != "Unreachable" else "Skipped"

        print(f"{country:<25} {domain:<20} {ip_address:<20} {status_code:<15} {tcp_latency:<15}")

    print("=" * 100)
    print("Process Completed.")
    print("=" * 100)

check_domains(json_file)
