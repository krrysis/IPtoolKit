import csv

# Open the CSV file
with open('output.csv', 'r') as file:
    # Create a reader object
    reader = csv.reader(file)

    # Create a list to store the IP addresses
    ip_list = []

    # Iterate over each row in the CSV file
    for i, row in enumerate(reader):
        # Skip the first row (header)
        if i == 0:
            continue

        # Extract the IP address from the row
        ip_address = row[0]

        # Append the IP address to the list
        ip_list.append(ip_address)

# Open the output file
with open('output.txt', 'w') as file:
    # Write the IP addresses to the file, separated by commas
    file.write(','.join(ip_list))

