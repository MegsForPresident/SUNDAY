import csv
import os
dict = {}
yes = False
os.chdir("Data")
if os.path.exists('commands.csv'):
    with open("commands.csv","r") as reader:
        dict = csv.DictReader(reader,delimiter=',')
else:
    with open("commands.csv","w") as writer:
        csv.DictWriter(writer,fieldnames=dict) 
        writer.close()
        yes = True
while True:
    if yes:
        print("You don't have any Commands, Have Some of your favourtie commands extracted.")    
        break     