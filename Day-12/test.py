def update_configuration(file_path, key, value):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        # print(lines)
    with open(file_path, 'w') as file:
        for k in lines:
            if key in k:
                file.write(f"{key}={value}\n")
            else:
                file.write(k)
                
# # Example usage
update_configuration('D:\\Sohail\\career\\DevOps\\python_devops\\Day-12\\server.conf', 'MAX_CONNECTIONS', '600')