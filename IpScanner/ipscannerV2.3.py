import os
import csv
import threading
import ipaddress

def ping_host(hostname, online_hosts, offline_hosts):
    response = os.system(f"ping -n 1 {hostname} > nul")
    if response == 0:
        print('🟩', hostname)
        online_hosts.append(hostname)
    else:
        print('🟥', hostname)
        offline_hosts.append(hostname)

def scan_ip_segment(ip_segment):
    online_hosts = []
    offline_hosts = []

    try:
        network = ipaddress.ip_network(ip_segment, strict=False)
        for host in network.hosts():
            thread = threading.Thread(target=ping_host, args=(str(host), online_hosts, offline_hosts))
            thread.start()

            # Introduce a delay (e.g., 0.1 seconds) between each thread
            time.sleep(0.04)  # Adjust the delay as needed

        for thread in threading.enumerate():
            if thread != threading.current_thread():
                thread.join()

        total_hosts = sum(1 for _ in network.hosts())
        if network.network_address in online_hosts:
            online_hosts.remove(network.network_address)
        if network.broadcast_address in online_hosts:
            online_hosts.remove(network.broadcast_address)

        print('Total hosts:', total_hosts)
        print('Online:', len(online_hosts))
        print('Offline:', len(offline_hosts))
        print('Offline List:')
        for host in offline_hosts:
            print(host)

        # Write results to a CSV file (you can keep this part as-is)
        # ...

    except ValueError:
        print("Invalid IP address or subnet mask. Please provide a valid CIDR notation (e.g., 192.168.95.0/24).")

def main():
    choice = input("Choose an option (1: CSV file, 2: IP and subnet mask): ")
    if choice == '1':
        # Handle CSV file (you can add your CSV processing logic here)
        with open('iplist.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                hostname = row[0]
                ping_host(hostname, online_hosts=[], offline_hosts=[])
    elif choice == '2':
        ip_segment = input("Enter IP address and subnet mask (e.g., 192.168.95.0/24): ")
        scan_ip_segment(ip_segment)
    else:
        print("Invalid choice. Please select 1 or 2.")
    input("Press ENTER to exit.")

if __name__ == "__main__":
    main()
