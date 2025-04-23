import json
import socket
import requests
import sys

def load_domains(json_file): # Loads the list of domains from a JSON file

    try:
        with open(json_file, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading JSON file: {e}")
        return []

def get_ip_address(domain): # Tries to convert a domain name (like example.com) into an IP address
    """Attempt to resolve a domain name to its IP address."""
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except socket.gaierror:
        return "Unreachable"

def get_status_code(domain): # Try to connect to the domain and get the HTTP status code (like 200, 404, etc.)
    """Attempt to get HTTP status code from the domain."""
    try:
        response = requests.get(f"http://{domain}", timeout=5)
        return response.status_code
    except requests.RequestException:
        return "Failed"

if len(sys.argv) < 2:
    print("Usage: python script.py <JSON_FILENAME>")
    sys.exit(1)

json_file = sys.argv[1]

def check_domains(json_file): # Main function to check each domain and print the results
    """Check and display domain connectivity status."""
    domain_data = load_domains(json_file)

    if not domain_data:
        print("No domain data found.")
        return

    # Print table headers
    print(f"{'Country':<25} {'Domain':<20} {'IP Address':<20} {'Status Code':<15}")
    print("=" * 85)

    for entry in domain_data:
        country = entry.get("country_name", "Unknown")
        domain = entry.get("domain", "Unknown")

        ip_address = get_ip_address(domain)
        status_code = get_status_code(domain) if ip_address != "Unreachable" else "Skipped"

        # Print the results in a formatted row
        print(f"{country:<25} {domain:<20} {ip_address:<20} {status_code:<15}")

check_domains(json_file)