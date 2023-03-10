from utilities import read_utils

# test_invalid_login_data = [
#         ("saul", "saul123", "Invalid credentials"),
#         ("kim", "kim123", "Invalid credentials"),
#         ("john", "john123", "Invalid credentials"),
# ]
from utilities.read_utils import get_csv_as_list

test_add_valid_employee = [
        ("Admin", "admin123", "John","J","Wick","John Wick","John"),
        ("Admin", "admin123", "Dana","K","Cook","Dana Cook","Dana"),
]

test_invalid_login_data = get_csv_as_list("../test_data/test_invalid_login_data.csv")