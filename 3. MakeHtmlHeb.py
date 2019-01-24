import urllib.request
from codecs import encode

uniSearch = "'\\xd"
engSearch = '"'
engSearch2 = "'"

contents = urllib.request.urlopen(input('Enter url: ')).read().decode() #"http://localhost:8080/topic/0"

f = open('data.txt', 'w')

ignore_list = ['LyricsTxtDotted', 'all']

ahrefS = contents.find('<a href')
ahrefS = contents.find('<a href', ahrefS + 1)
while ahrefS != -1:
	ahrefE = contents.find('<a href', ahrefS + 1)
	line = contents[ahrefS:ahrefE]

	# uniIndex = line.find(uniSearch)
	# engIndex = line.find(engSearch)
	startIndex = line.find("'")
	startIndex2 = line.find('"')
	endIndex = 0
	endIndex2 = 0
	ignore = False
	flag = 0
	tab_count = 0

	while startIndex != -1 or startIndex2 != -1:
		if startIndex2 == -1 or (startIndex < startIndex2 and startIndex != -1):
			flag = 0
			endIndex = line.find("'", startIndex + 1)
			if endIndex != -1:
				if startIndex2 != -1 and (startIndex2 > startIndex and startIndex2 < endIndex): # means there's a "" in the text (exmp: etze"l)
					flag = 3
				text = line[startIndex + 1:endIndex]
				for ignore_text in ignore_list:
					if text == ignore_text:
						ignore = True
						break
				if ignore:
					ignore = False
				else:
					if '.txt' in text:
						text = text[:text.find('.txt')]
					if text[0] == '\\': # uni
						text = encode(text.encode().decode('unicode_escape'),"raw_unicode_escape").decode()
					elif '\\x' in text:
						ind = text.find('\\x')
						text = text[:ind] + encode(text[ind:].encode().decode('unicode_escape'),"raw_unicode_escape").decode()
					#print(text)

					#CHEAT:
					if text == 'שבק ס':
						text = 'שב"ק ס\''
					elif text == 'שבק מיוזיק':
						text = 'שב"ק מיוזיק'
					elif text == 'רועי ציקי ארד':
						text = 'רועי צ\'יקי ארד'

					if tab_count == 0:
						f.write('\n' + text)
						tab_count += 1
					else:
						f.write('\t' + text)
			else:
				flag = -1
		elif startIndex == -1 or (startIndex > startIndex2 and startIndex2 != -1):
			flag = 1
			endIndex2 = line.find('"', startIndex2 + 1)
			if endIndex2 != -1:
				if startIndex != -1 and (startIndex > startIndex2 and startIndex < endIndex2): # means there's a ' in the text (exmp: gin'gi)
					flag = 2
				text = line[startIndex2 + 1:endIndex2]
				for ignore_text in ignore_list:
					if text == ignore_text:
						ignore = True
						break
				if ignore:
					ignore = False
				else:
					if '.txt' in text:
						text = text[:text.find('.txt')]
					if text[0] == '\\': # uni
						text = encode(text.encode().decode('unicode_escape'),"raw_unicode_escape").decode()
					elif '\\x' in text:
						ind = text.find('\\x')
						text = text[:ind] + encode(text[ind:].encode().decode('unicode_escape'),"raw_unicode_escape").decode()
					#print(text)

					#CHEAT:
					if text == 'שבק ס':
						text = 'שב"ק ס\''
					elif text == 'שבק מיוזיק':
						text = 'שב"ק מיוזיק'
					elif text == 'רועי ציקי':
						text = 'רועי צ\'יקי'

					if tab_count == 0:
						f.write('\n' + text)
						tab_count += 1
						#print('\n' + text)
					else:
						f.write('\t' + text)
						#print('\t' + text)
			else:
				flag = -2
		if flag == 0:
			startIndex = line.find("'", endIndex + 1)
		elif flag == 1:
			startIndex2 = line.find('"', endIndex2 + 1)
		elif flag == -1:
			startIndex = -1
		elif flag == -2:
			startIndex2 = -1
		elif flag == 2:
			startIndex2 = line.find('"', endIndex2 + 1)
			startIndex = line.find("'", endIndex2 + 1)
		elif flag == 3:
			startIndex = line.find('"', endIndex + 1)
			startIndex2 = line.find("'", endIndex + 1)
		
		#print('Start index:', startIndex, 'Start index2:',startIndex2, 'flag:',flag,'tab_count:',tab_count)

	ahrefS = ahrefE
f.close()
print('Done')