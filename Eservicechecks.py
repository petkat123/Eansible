import wmi

# JC define the target servers and services
servers = [
    {'hostname': 'server1', 'username': 'user1', 'password': 'password1'},
    {'hostname': 'server2', 'username': 'user2', 'password': 'password2'},
    # Add more servers as needed
]

services_to_check = ['ServiceName1', 'ServiceName2']  # Replace with actual service names

def check_service_status(server, username, password, service_name):
    try:
        connection = wmi.WMI(server, user=username, password=password)
        service = connection.Win32_Service(Name=service_name)
        if service:
            status = service[0].State
            print(f"Service '{service_name}' on {server} is {status}.")
        else:
            print(f"Service '{service_name}' not found on {server}.")
    except Exception as e:
        print(f"Failed to connect to {server} or retrieve service status. Error: {e}")

for srv in servers:
    for service in services_to_check:
        check_service_status(srv['hostname'], srv['username'], srv['password'], service)
