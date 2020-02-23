import csv
import os
import yaml

# for the input of the province
# city = 'Vancouver'
#  [Vancouver, [Canucks,Lions]]
sports = [
    "soccer",
    "football",
    "hockey",
    "basketball",
    "baseball"
]


def returnteams(city):
    teams = []
    with open("teams.yaml", 'r') as file:
        doc = yaml.load(file)
    for index in range(len(sports)):
        if doc.get(city).get(sports[index]):
            teams.append(doc[city][sports[index]][0])
    return teams
# with open(r"\Users\wrlee\mountainmadness\Hackathon\Canadateam2020.csv") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',',quotechar = '|')
#     line_count = 0
#     i = 0
#     data = ["a","a","a","a","a","a","a","a","a"]
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {",      ".join(row)}')
            
           
#             line_count += 1
#         else:
#             data[i] =  [row[0], row[1]  + row[2], row[3], row[4], row[5], row[6], row[7] ]
#             print(f'\t{row[0]}, {row[1]} ---- {row[2]} ---- {row[3]} ---- {row[4]} ---- {row[5]} ---- {row[6]} ---- {row[7]}')
#             i+=1
# ''' i = 0 
# j = 0
# print("\n")
# while i< 9 :
#     print (data[i])
#     i+=1

# print (data[2])
#  '''
# city   = 'Vancouver'
# temp =[]
# while j<20:
#     temp  += data
    
#     if temp ==city:
#         print ('success')
#     i+= 1

# '''  '''
teams = returnteams("calgary")
print(teams)	
								
##teams = city + ": " + results