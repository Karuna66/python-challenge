import csv
import datetime

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

with open('employee_new_data.csv','w',newline='') as wf:
        fieldnames = ['Emp ID','First Name','Last Name','DOB','SSN','State']
        csv_writer = csv.DictWriter(wf,fieldnames=fieldnames,delimiter=',')

        csv_writer.writeheader()

        with open('employee_data.csv','r') as rf:
                csv_reader = csv.DictReader(rf)

                for i in csv_reader:
                        out_row ={}
                        out_row['Emp ID'] =i['Emp ID']
                        out_row['First Name'],out_row['Last Name'] = i['Name'].split(' ')
                        out_row['DOB'] = i['DOB']
                        out_row['SSN'] = "XXX-XX-" + i['SSN'][slice(7,12)]

                       

                        for k,v in us_state_abbrev.items():
				
                                if i['State'].strip() == k:
                                        out_row['State'] = v
                                
			                     
                        csv_writer.writerow(out_row)
