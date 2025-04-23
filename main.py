import json
import socket
import requests
import sys
import time

#1

# http code
#2

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
