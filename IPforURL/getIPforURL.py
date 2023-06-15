#Python program that takes URLs from a CSV file, pings them, and stores the IP address against the URL in a separate CSV file
#author: Kshitij
#github: https://github.com/krrysis

import csv
import socket

def ping(url):
    try:
        ip = socket.gethostbyname(url)
        return ip
    except:
        return "Error"

with open('urls.csv', 'r') as f:
    reader = csv.reader(f)
    urls = list(reader)

with open('ip_addresses.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for url in urls:
        writer.writerow([url[0], ping(url[0])])