from datetime import datetime

my_date = "Jan 15, 2023 - 12:05:33"
python_date = datetime.strptime(my_date, "%b %d, %Y - %H:%M:%S")
print(python_date)
month = python_date.strftime("%B")
print(month)
new_date = python_date.strftime("%d.%m.%Y, %H:%M")
print(new_date)
