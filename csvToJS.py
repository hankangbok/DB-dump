import csv
result=[]
with open("assets.csv", "rb") as f:
    eachline='var dataSet = [';
    reader=csv.reader(f, delimiter=",")
    for i, line in enumerate(reader):
        eachline+=str(line)+","
        #print '{},'.format(line)
        #print eachline
    #remove the last comma
    eachline=eachline[:-1]
    #Add in a closing bracket for the dataset
    eachline+="]"
    print eachline
