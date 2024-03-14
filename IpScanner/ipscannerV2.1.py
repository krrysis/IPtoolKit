#This scans IPs and returns which of them can be pinged
#author: Kshitij
#github: https://github.com/krrysis

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

    # Write results to a CSV file
    with open('host_status.csv', 'w', newline='') as csvfile:
        fieldnames = ['Hostname', 'Status']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for host in online_hosts:
            writer.writerow({'Hostname': host, 'Status': 'Online'})
        for host in offline_hosts:
            writer.writerow({'Hostname': host, 'Status': 'Offline'})

        # Write overall status counts
        writer.writerow({'Hostname': 'Total Online', 'Status': len(online_hosts)})
        writer.writerow({'Hostname': 'Total Offline', 'Status': len(offline_hosts)})

if __name__ == "__main__":
    main()
    input("Press ENTER to exit.")

