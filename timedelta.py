from datetime import datetime, timedelta
today = datetime.now()
print('Today is: ' + str(today))

fifteen_days = timedelta(days=23, weeks=2, hours=5, minutes=12, seconds=13)
fifteen_days_ago = today + fifteen_days
print('Twenty-Three days after is: ' + str(fifteen_days_ago))