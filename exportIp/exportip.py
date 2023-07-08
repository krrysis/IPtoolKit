#take a text fine, paste all the text you want, it'll identify all the ip addresses from it and put it into csv file for you, how convenient
#author: Kshitij
#github: https://github.com/krrysis
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
