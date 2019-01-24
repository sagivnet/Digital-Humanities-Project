import os
dir_in_path = os.path.join(os.path.expanduser('~'), 'lemlda', 'Lyrics')
dir_out_path = os.path.join(os.path.expanduser('~'), 'lemlda', 'LyricsTxt')

if not os.path.exists(dir_out_path):
	os.makedirs(dir_out_path)
	
for root, dirs, files in os.walk(dir_in_path):
	for a_dir in dirs:
		out_dir = os.path.join(dir_out_path, a_dir)
		if not os.path.exists(out_dir):
			os.makedirs(out_dir)
	for file in files:
		if not file.endswith('.xml'):
			continue
		file_path = os.path.join(root, file)
		file_out_path = dir_out_path + '/' + file_path[len(dir_in_path):-3] + 'txt'
		f_in = open(file_path, "r")
		f_out = open(file_out_path, "w")
		while True:
			line = f_in.readline()
			if not line:
				break
			if "<l>" in line:
				line = line.strip()[3:-4]
				f_out.write(line + "\n")
		f_in.close()
		f_out.close()
		print("Done with file:", file)

print("Finished.")
