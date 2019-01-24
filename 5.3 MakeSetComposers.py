songs_set = set()
data_file_paths_hardcoded = ['extractedData4.txt',
'extractedData12.txt',
'extractedData6.txt',
'extractedData11.txt',
'extractedData5.txt',
'extractedData19.txt',
'extractedData13.txt',
'extractedData18.txt',
'extractedData3.txt']
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

for data_file_path in data_file_paths:
	for x in ([line.rstrip('\n') for line in open(data_file_path)]):
		if x > '\n':
			song_data = x.split('\t') # len(song_data) should be 4: singer, song, writer, composer
			if song_data[3] != 'missing' and song_data[3] != 'לא ידוע' and 'עממי' not in song_data[3] and 'אקורדים' not in song_data[3]:
				songs_set.add(song_data[3] + '\t' + song_data[1]) # composer\tsong

print('Num of songs:', len(songs_set))
export = input("Export to a file?<y/n>: ")
if export == 'y':
	file_path = input("File path: ")
	with open(file_path, 'w') as f:
		for song in songs_set: #song = composer\tsong actually
			f.write(song + '\n')
print('Done')