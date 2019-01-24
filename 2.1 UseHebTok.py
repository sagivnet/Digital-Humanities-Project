import os
import subprocess

dir_in_path = os.path.join(os.path.expanduser('~'), 'lemlda', 'LyricsTxt')
dir_out_path = os.path.join(os.path.expanduser('~'), 'lemlda', 'LyricsTxtTokenized')
delimeter = ''

if not os.path.exists(dir_out_path):
	os.makedirs(dir_out_path)
	
for root, dirs, files in os.walk(dir_in_path):
	for a_dir in dirs:
		if "'" in a_dir or '"' in a_dir:
			a_dir_new = a_dir.replace('"', '').replace("'", '')
			os.rename(os.path.join(root, a_dir), os.path.join(root, a_dir_new))
			a_dir = a_dir_new
		out_dir = os.path.join(dir_out_path, a_dir)
		if not os.path.exists(out_dir):
			os.makedirs(out_dir)
	for file in files:
		print("Working on:", os.path.join(root, file))
		if "'" in file and '"' in file:
			file_temp = file.replace("'", '\'').replace('"', '\"')
			#os.rename(os.path.join(root, file), os.path.join(root, file_temp))
			file = file_temp
		elif "'" in file or "'" in root:
			delimeter = '"'
		elif '"' in file or '"' in root:
			delimeter = "'"
		else:
			delimeter = "'"
		out_path =  dir_out_path + root[len(dir_in_path):] + '/' + file
		ret_val = subprocess.call('python3.7 ./hebtokenizer.py' + ' < ' + delimeter + os.path.join(root, file) + delimeter + ' > ' + delimeter + out_path + delimeter, shell=True)
		if ret_val != 0:
			print("Error, exiting..")
			exit(1)
		print("Done")
print("Finished.")