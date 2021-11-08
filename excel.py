import csv
with open("Sample-Spreadsheet-10-rows.csv","r" ,encoding="unicode_escape") as f:
    csvfile=csv.reader(f)
    d={}
    for line in csvfile:
        d[line[2]]=0
    print(list(d.keys()))








