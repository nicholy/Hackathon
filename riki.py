import csv
import os

# for the input of the province
# city = 'Vancouver'
#  [Vancouver, [Canucks,Lions]]

with open(r"\Users\wrlee\mountainmadness\Canadateam2020.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    i = 0
    array = ["a","a","a","a","a","a","a","a"]
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {",      ".join(row)}')
           
            line_count += 1
        else:
            ##array[i] =  (row[0]+row[1]+row[2]+row[3] +row[4] +row[5] + row[6]+ row[7])
            print(f'\t{row[0]}, {row[1]} ---- {row[2]} ---- {row[3]} ---- {row[4]} ---- {row[5]} ---- {row[6]} ---- {row[7]}')
            i+=1

print (array)
