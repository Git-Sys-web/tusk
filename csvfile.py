import csv
with open('mycsv.csv','w',encoding='UTF8',newline='') as f:
    writer =csv.writer(f)
    writer.writerow(['name','age','marks'])
    writer.writerows([['maidhili',25,50],['apoorva',25,50]])

