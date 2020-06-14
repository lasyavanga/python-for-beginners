from datetime import datetime
name = input('Enter your name: ')
birthday = input('Enter your Date of Birth (dd/mm/yyyy): ')
print('Hi ' + name )
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print('Your Date of Birth is: ')
print('Day: ' + str(birthday_date.day))
print('Month: ' + str(birthday_date.month))
print('Year: ' + str(birthday_date.year))