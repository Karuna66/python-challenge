import re

with open('paragraph_2.txt','r') as rf:

	read_txt = rf.read()

	word_count = len(re.findall(r'\w+', read_txt))

	sen_count =len(re.findall(r'\.', read_txt))

	sentence_pat = re.compile(r'([^.!?]+[.!?]+)')
	word_pat = re.compile(r'(\S+)')

	sentences = sentence_pat.findall(read_txt)
	
	sen_length=0
	for matches in sentences:
		sen_wd_length = word_pat.findall(matches)
		sen_length +=len(sen_wd_length)
	
	average_sentence_length = sen_length/sen_count
	

	words = word_pat.findall(read_txt)

	average_word_length = sum([len(word) for word in words])/len(words)
	
	print("Paragraph Analysis")
	print("-----------------")
	print(f'Approximate Word Count: {word_count}')
	print(f'Approximate Sentence Count: {sen_count}')
	print(f'Average Letter Count: {average_word_length:.1f}')
	print(f'Average Sentence Length: {average_sentence_length}')