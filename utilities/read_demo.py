"This will be deleted"

import pandas

csv = pandas.read_csv(filepath_or_buffer="../test_data/test_invalid_login_data.csv",delimiter=";")

print(csv)

print(csv.loc[0])

#print(csv.values.tolist())

list=[]
for i in csv.index:
    print(csv.loc[i].tolist())
    list.append(csv.loc[i].tolist())

print(list)