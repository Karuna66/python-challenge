import os
import csv

with open('budget_data.csv','r') as rf:

	csv_reader = csv.DictReader(rf)

	great_incre =0
	great_decre = 0
	total_month =0
	total_pro_loss = 0
	ave_chg=[]
	
	for i in csv_reader:
	
		total_month +=1
		total_pro_loss += int(i['Profit/Losses'])
		ave_chg.append(int(i['Profit/Losses']))

		if int(i['Profit/Losses']) > great_incre:
			great_incre = int(i['Profit/Losses']) 
			great_inc_date = i['Date']

		if int(i['Profit/Losses']) < great_decre:
			great_decre = int(i['Profit/Losses'])
			great_dec_date = i['Date']
	
	
	average_ch=[]
	i=1
	while i < len(ave_chg):
		ave_chg_count = ave_chg[i] - ave_chg[i-1]
		average_ch.append(ave_chg_count)
		i+=1

	ave_chg_final = sum(average_ch)/len(average_ch)

	
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
