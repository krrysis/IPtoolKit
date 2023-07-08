#Take csv file, put all your domains and ip into it, this will output the expiry date for it
#author: Kshitij
#github: https://github.com/krrysis

import ssl
import OpenSSL
import datetime
import csv

def get_SSL_Expiry_Date (host, port):
    cert = ssl.get_server_certificate ((host, port))
    x509 = OpenSSL.crypto.load_certificate (OpenSSL.crypto.FILETYPE_PEM, cert)
    expiry_date = x509.get_notAfter().decode('utf-8')
    expiry_date_obj = datetime.datetime.strptime(expiry_date, '%Y%m%d%H%M%SZ')
    formatted_expiry_date = expiry_date_obj.strftime('%d-%m-%Y')
    return(formatted_expiry_date)

#get_SSL_Expiry_Date ("121.244.93.46", 443)
with open('output.csv', mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['IP Address', 'SSL Expiry Date'])
    with open('input.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            ip_address = row[0]
            port = 443
            writer.writerow([ip_address, get_SSL_Expiry_Date(ip_address, port)])
