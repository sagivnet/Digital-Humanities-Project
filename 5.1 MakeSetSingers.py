songs_set = set()
data_file_paths_hardcoded = ['data4.txt',
'data12.txt',
'data6.txt',
'data11.txt',
'data5.txt',
'data19.txt',
'data13.txt',
'data18.txt',
'data3.txt']
data_file_paths = list()
num_of_datas = input('Number of datas to use (out of 9): ')
try:
	num_of_datas = int(num_of_datas)
except:
	print("Number.")
	exit(1)
if num_of_datas not in range(0, 10):
	print('0 - 9')
	exit(1)
for i in range(num_of_datas):
	data_file_paths.append(data_file_paths_hardcoded[i])
	#data_file_paths.append(input('Data file: '))
for data_file_path in data_file_paths:
	for x in ([line.rstrip('\n') for line in open(data_file_path)]):
		if x > '\n':
			songs_set.add(x)
print('Num of songs:', len(songs_set))
export = input("Export to a file?<y/n>: ")
if export == 'y':
	file_path = input("File path: ")
	with open(file_path, 'w') as f:
		for song in songs_set: #song = singer\tsong actually
			f.write(song + '\n')
print('Done')