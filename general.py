import os

def create_project_dir(directory):
	if not os.path.exists(directory):
		print('Creating Project '+ directory)
		os.makedirs(directory)

def create_data_files(directory_name, fileName, data):
	f = directory_name+fileName

	if not os.path.isfile(f):
		write_file(f, data)

def write_file(path, data):
	f = open(path, 'w')
	f.write(data)
	f.close()


def add_data_to_file(path, data):
	with open(path, 'a') as file:
		file.write(data+'\n')


def delete_file_content(path):
	with open(path, 'w'):
		pass

def read_file_content(path):
	content = []
	with open(path, 'r') as f:
		data = f.read()
		content.append(data)

	return content

