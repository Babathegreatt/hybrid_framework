import pandas

"""Mathod to convert the CSV to list"""
def get_csv_as_list(file_path):
    df = pandas.read_csv(filepath_or_buffer="../test_data/test_invalid_login_data.csv",delimiter=";")
    return df.values.tolist()


"""Method to convert the excel to list"""
def get_sheet_as_list(file_path,sheet_name) -> object:
    df = pandas.read_excel(io=file_path,sheet_name=sheet_name)
    return df.values.tolist()
