import csv
import os

from collections import Counter

with open('election_data.csv','r') as rf:
	csv_reader = csv.DictReader(rf)

	#print (csv_reader.fieldnames)
	total_votes = 0
	cand_list=[]

	for i in csv_reader:
		total_votes += 1
		cand_list.append(i['Candidate'])
# to count the occurences
final_list=Counter(cand_list)

with open('election_data.txt','w') as wf:
		wf.write(f' Election Results\n')
		print(f' Election Results')
		wf.write(f'--------------------------------------------\n')
		print(f'--------------------------------------------')
		wf.write(f'Total votes: {total_votes}\n')
		print(f'Total votes: {total_votes}')
		wf.write(f'--------------------------------------------\n')
		print(f'--------------------------------------------')

		winner = 0

		for k,v in final_list.items():

			wf.write(f' {k}: {v/total_votes*100:.03f}%   ({v})\n')
			print(f' {k}: {v/total_votes*100:.03f}%   ({v})')
			if v > winner:
				cand_winner = k
				winner = v
		wf.write(f'--------------------------------------------\n')
		print(f'--------------------------------------------')

		wf.write(f'Winner is : {cand_winner}\n')
		print(f'Winner is : {cand_winner}')
		wf.write(f'--------------------------------------------\n')
		print(f'--------------------------------------------')
