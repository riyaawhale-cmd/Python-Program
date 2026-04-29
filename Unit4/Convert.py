import json
import csv

try:
    with open('c:\Users\DELL\OneDrive\Desktop\Unit3\data_new.json','r') as json_file:
     #with open ('data_new.json','r')as json_file
     data = json.load(json_file)

    with open('output.csv','w',newline='') as csv_file:
        headers = data[0].keys()
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

    print("Conversion sucessfull!")

except FileNotFoundError:
   print("Error:data.json file not found.")
         