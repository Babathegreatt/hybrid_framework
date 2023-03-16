"This will be deleted"

import pandas

csv = pandas.read_csv(filepath_or_buffer="../test_data/test_invalid_login_data.csv",delimiter=";")

# print(csv)
#
# print(csv.loc[0])
#
# #print(csv.values.tolist())
#
# list=[]
# for i in csv.index:
#     print(csv.loc[i].tolist())
#     list.append(csv.loc[i].tolist())
#
# print(list)
#
# df = pandas.read_excel(io="../test_data/Orange_test_data.xlsx",sheet_name="test_add_valid_employee")
#
# print(df.loc[0])
#
# print(df.get(["User Name","Password"]))

"""Read the Json file"""
di = pandas.read_json(path_or_buf="../test_data/data.json",typ="dictionary")

print(di["browser"])