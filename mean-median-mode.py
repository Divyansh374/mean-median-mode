import csv
from collections import Counter

# Please add the location of the file on your respective computer
with open("F:\WhiteHatJr Projects\PRO-C104\SOCR-HeightWeight.csv", newline="") as f: 
    reader = csv.reader(f)
    file_data = list(reader)
    
file_data.pop(0)
newData=[]

for i in range(len(file_data)):
    n_num = file_data[i][1]
    newData.append(float(n_num))

n = len(newData)

#Mean
total = 0

for x in newData:
    total+=x

mean = total/n

print("Mean ->", mean)

# Median
newData.sort()

if n%2 == 0:
    median1 = float(newData[n//2])
    median2 = float(newData[n//2-1])
    median = (median1 + median2)/2
else:
    median = newData[n//2]

print("Median ->", median)

# Mode

data = Counter(newData)

modeDataForRange = {"50-60": 0, "60-70": 0, "70-80": 0}

for height, occurence in data.items():
    if 50<float(height)<60:
        modeDataForRange["50-60"] += occurence
    elif 60<float(height)<70:
        modeDataForRange["60-70"] += occurence
    elif 70<float(height)<80:
        modeDataForRange["70-80"] += occurence
        
modeRange, modeOccurence = 0, 0

for range, occurence in modeDataForRange.items():
    if occurence>modeOccurence:
        modeRange, modeOccurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
        
mode = float((modeRange[0] + modeRange[1])/2)

print("Mode ->", mode)