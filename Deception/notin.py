# Ask the user for input
user_input = input("Please paste a bunch of IPs, each on a new line:\n")

# Split the input into a list of IPs
ip_list = user_input.split()

# Format the output string
output = f"attacker.ip not in {ip_list}"

# Print the output
print(output)

# Pause to prevent the command prompt from closing automatically
input("Press Enter to exit...")
