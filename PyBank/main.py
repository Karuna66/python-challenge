import os
import csv

with open('budget_data.csv','r') as rf:

	csv_reader = csv.DictReader(rf)

	
	total_month =0
	total_pro_loss = 0
	ave_chg=[]
	great_date=[]
	
	for i in csv_reader:
	
		total_month +=1
		total_pro_loss += int(i['Profit/Losses'])
		ave_chg.append(int(i['Profit/Losses']))
		great_date.append(i['Date'])
		
	
	
	average_ch=[]

	i=1

	while i < len(ave_chg):

		ave_chg_count = ave_chg[i] - ave_chg[i-1]
		average_ch.append(ave_chg_count)
		i+=1

	ave_chg_final = sum(average_ch)/len(average_ch)

	great_incre = max(average_ch)
	great_decre = min(average_ch)

	new_list = zip(average_ch,great_date[1:])

	for i in new_list:
		if i[0] == great_incre:
			great_inc_date =i[1]
		if i[0] == great_decre:
			great_dec_date =i[1]


	
with open('budget_data.txt','w') as wf:
		
			wf.write('Financial Analysis\n')
			wf.write("............................................\n")
			wf.write(f'Total month: {total_month}\n')
			wf.write(f'Total: ${total_pro_loss}\n')
			wf.write(f'Average Change : ${ave_chg_final:.02f}\n')
			wf.write(f'Greatest Increase in Profits: {great_inc_date}  (${great_incre})\n')
			wf.write(f'Greatest Decrease in Profits: {great_dec_date}  (${great_decre})\n')

			print('Financial Analysis')
			print("............................................")
			print(f'Total month: {total_month}')
			print(f'Total: ${total_pro_loss}')
			print(f'Average Change :  ${ave_chg_final:.02f}')
			print(f'Greatest Increase in Profits: {great_inc_date}  (${great_incre})')
			print(f'Greatest Decrease in Profits: {great_dec_date}  (${great_decre})')
