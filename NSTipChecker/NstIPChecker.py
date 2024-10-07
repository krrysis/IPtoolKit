import csv
import ipaddress
import os

# Function to load tool IPs from nst.csv
def load_tool_ips():
    tool_ips = []
    try:
        with open('nst.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                tool_ips.append(row[0])
    except FileNotFoundError:
        print("Error: nst.csv file not found")
        exit(1)
    return tool_ips

# Function to check if an IP belongs to the tool
def ip_in_tool(ip, tool_ips):
    for tool_ip in tool_ips:
        if '/' in tool_ip:
            if ipaddress.ip_address(ip) in ipaddress.ip_network(tool_ip):
                return True
        else:
            if ip == tool_ip:
                return True
    return False

def check_single_ip(tool_ips):
    ip = input("Enter the IP address: ")
    if ip_in_tool(ip, tool_ips):
        print(f"{ip} belongs to the tool.")
    else:
        print(f"{ip} does not belong to the tool.")

def check_csv_file(tool_ips):
    input_file = "ips.csv"
    output_file = "output.csv"
    
    if not os.path.isfile(input_file):
        print("Error: ips.csv file not found")
        return
    
    with open(input_file, mode='r') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        writer.writerow(["IP Address", "Belongs to Tool"])
        
        for row in reader:
            ip = row[0]
            belongs_to_tool = ip_in_tool(ip, tool_ips)
            writer.writerow([ip, belongs_to_tool])
    
    print(f"Output written to {output_file}")

def main():
    tool_ips = load_tool_ips()
    
    while True:
        print("Choose an option:")
        print("1. Input a single IP address")
        print("2. Use the default CSV file (ips.csv) with multiple IP addresses")
        choice = input("Enter 1 or 2: ")
        
        if choice == '1':
            check_single_ip(tool_ips)
        elif choice == '2':
            check_csv_file(tool_ips)
        else:
            print("Invalid choice. Please enter 1 or 2.")
        
        restart = input("Press Enter to run the program again or type 'no' to exit: ")
        if restart.lower() == 'no':
            break

if __name__ == "__main__":
    main()
