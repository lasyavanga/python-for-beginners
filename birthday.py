from datetime import datetime

name = input('Enter name: ')
date_of_birth = input('Enter DOB (mm-dd-yyyy): ')
birthday = datetime.strptime(date_of_birth, '%m-%d-%Y')
print(f"{name}, {birthday.month} (month), {birthday.day} (day), {birthday.year} (year)")