import re
import csv

with open('input.txt', 'r') as f:
    text = f.read()

ip_addresses = re.findall(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', text)

with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['IP Address'])
    for ip in ip_addresses:
        writer.writerow([ip])
