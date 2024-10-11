# Initialize an empty list to store IPs
ip_list = []

print("Please paste a bunch of IPs, each on a new line. Press Enter on an empty line to finish:")

# Collect IPs until a blank line is entered
while True:
    ip = input()
    if ip == "":
        break
    ip_list.append(ip)

# Format the output string with double quotes
output = f'attacker.ip not in ["' + '", "'.join(ip_list) + '"]'

# Print the output
print(output)

# Pause to prevent the command prompt from closing automatically
input("Press Enter to exit...")
