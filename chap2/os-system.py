import os 

host = input('Host / IP Address to ping:')
command = (f'ping -c 1 {host}')

response=os.popen(command).read()
print(response)