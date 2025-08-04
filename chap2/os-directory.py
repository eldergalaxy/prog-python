import os 


directory = os.path.dirname(os.path.abspath(__file__))
file_name='dir-test.txt'
file_path = os.path.join(directory, file_name)


with open(file_path, 'w') as file:
    file.write('the os module is cool')

with open(file_path, 'r') as file:
    message = file.read()


print(message)