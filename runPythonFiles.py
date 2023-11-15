filename = 'public_ip_address_create_customized_values.py'

with open(filename, 'r') as file:
    exec(file.read())

filename2 = 'network_interface_create.py'

with open(filename2, 'r') as file:
    exec(file.read())

filename3 = 'virtual_machine_create_with_ssh_authentication.py'

with open(filename3, 'r') as file:
    exec(file.read())