import csv
def readcsv():
    with open('finaldisk.csv','r') as f:
        xx= csv.reader(f)
        #print(xx)
        #del(xx[-1])
        for i in xx:
            print(i)


print(readcsv())