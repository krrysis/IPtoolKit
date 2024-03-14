#This scans IPs and returns which of them can be pinged
#author: Kshitij
#github: https://github.com/krrysis
#v2: implemented multi-threading

import os
import csv
import threading

def ping_host(hostname, online_hosts, offline_hosts):
    response = os.system(f"ping -n 1 {hostname} > nul")
    if response == 0:
        print('🟩', hostname)
        online_hosts.append(hostname)
    else:
        print('🟥', hostname)
        offline_hosts.append(hostname)

def main():
    hostname = []
    with open('iplist.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            hostname.append(row[0])

    online_hosts = []
    offline_hosts = []

    # Create a list of threads
    threads = []
    for host in hostname:
        thread = threading.Thread(target=ping_host, args=(host, online_hosts, offline_hosts))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    print('Total hosts:', len(hostname))
    print('Online:', len(online_hosts))
    print('Offline:', len(offline_hosts))
    print('Offline List:', offline_hosts)

if __name__ == "__main__":
    main()
    input("Press ENTER to exit.")
