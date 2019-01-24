xml_data_path = '/home/osboxes/lemlda/Lyrics/'
data_path = input("Enter data file path: ")
data_lines = [line.rstrip('\n') for line in open(data_path)]
extract_file = open('extractedData.txt', 'w')
extract_file.write('Singer\tSong\tWriter\tComposer\n')
prob_num = 0
write_count = 0
for line in data_lines:
	if line <= '\n':
		continue
	line_data = line.split('\t')
	singer = line_data[0]
	song = ''
	if len(line_data) == 2:
		song = line_data[1]
	elif len(line_data) == 3:
		song = line_data[1] + ' ' + line_data[2]
	else:
		print('Problem with line:', line)
		continue

	extract_file.write(singer + '\t' + song)

	xml_data_file_path = xml_data_path + singer + '/' + song + '.xml'

	try:
		with open(xml_data_file_path, 'r') as f:
			xml_file_data = f.read()
			findIndex = xml_file_data.find('<writer>')
			if findIndex == -1:
				writer = 'missing'
			else:
				writer = xml_file_data[findIndex + len('<writer>'):xml_file_data.find('</writer>')]
			findIndex = xml_file_data.find('<composer>')
			if findIndex == -1:
				composer = 'missing'
			else:
				composer = xml_file_data[findIndex + len('<composer>'):xml_file_data.find('</composer>')]
	
		extract_file.write('\t' + writer + '\t' + composer + '\n')
		write_count += 1
	except:
		prob_num += 1
		print('Problem #' + str(prob_num), 'Path:', xml_data_file_path)

extract_file.close()
print("Written:", write_count)
print("Done")
