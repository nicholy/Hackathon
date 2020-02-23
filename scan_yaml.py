import csv
import os
import yaml
import sys

sports = [
    "soccer",
    "football",
    "hockey",
    "basketball",
    "baseball"
]

def returnteams(city):
    teams = []
    
    with open('Desktop/hackathon/teams.yaml', 'r') as file:
        doc = yaml.load(file)
    for index in range(len(sports)):
        if doc.get(city).get(sports[index]):
            teams.append(doc[city][sports[index]][0])
    return teams

