#Example: Managing a Dictionary of Server Configurations and Optimizing Retrieval
server_config = {
    'server1': {'ip': '192.168.1.1', 'port': 8080, 'status': 'active'},
    'server2': {'ip': '192.168.1.2', 'port': 8000, 'status': 'inactive'},
    'server3': {'ip': '192.168.1.3', 'port': 9000, 'status': 'active'}
}

#Function for retrieval
def get_server_status(server_name):
    return server_config.get(server_name, {}).get('status', 'Server not found')

#Example usage
server_name = 'server4'
status = get_server_status(server_name)
print(f"{server_name} status: {status}")