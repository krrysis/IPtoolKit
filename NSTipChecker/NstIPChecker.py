import csv
import ipaddress

# List of IPs and IP ranges that belong to your tool
tool_ips = [
    "139.87.116.247", "139.87.107.37", "64.39.96.0/20", "139.87.112.0/23",
    "13.201.147.153", "13.201.237.34", "13.202.33.77", "13.232.90.170",
    "15.207.165.243", "65.0.140.209", "13.202.156.220", "13.232.233.173",
    "15.207.97.104", "3.111.211.0", "13.202.146.114", "43.205.42.83",
    "13.202.146.49", "13.233.50.176", "13.200.184.13", "13.202.51.212",
    "65.1.207.206", "3.109.105.204", "13.235.230.21", "13.202.36.214",
    "15.207.217.81", "13.202.68.193", "3.109.172.159", "35.154.200.236",
    "13.202.65.124", "13.202.77.169", "3.6.32.31", "15.207.231.29",
    "3.7.226.6", "13.201.17.99", "13.232.206.128", "13.235.165.238",
    "3.110.12.166", "3.111.240.49", "3.7.5.24", "43.205.4.85",
    "65.0.143.234", "65.1.243.243", "68.183.82.175", "134.209.146.54",
    "64.227.174.37", "64.227.142.167", "142.93.220.160"
]

def ip_in_tool(ip):
    for tool_ip in tool_ips:
        if '/' in tool_ip:
            if ipaddress.ip_address(ip) in ipaddress.ip_network(tool_ip):
                return True
        else:
            if ip == tool_ip:
                return True
    return False

def check_single_ip():
    ip = input("Enter the IP address: ")
    if ip_in_tool(ip):
        print(f"{ip} belongs to the tool.")
    else:
        print(f"{ip} does not belong to the tool.")

def check_csv_file():
    input_file = input("Enter the path to the CSV file: ")
    output_file = "output.csv"
    
    with open(input_file, mode='r') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        writer.writerow(["IP Address", "Belongs to Tool"])
        
        for row in reader:
            ip = row[0]
            belongs_to_tool = ip_in_tool(ip)
            writer.writerow([ip, belongs_to_tool])
    
    print(f"Output written to {output_file}")

def main():
    print("Choose an option:")
    print("1. Input a single IP address")
    print("2. Use a CSV file with multiple IP addresses")
    choice = input("Enter 1 or 2: ")
    
    if choice == '1':
        check_single_ip()
    elif choice == '2':
        check_csv_file()
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
