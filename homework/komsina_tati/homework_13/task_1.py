from datetime import datetime, timedelta
import os

base_path = os.path.dirname(__file__)

homework_path = os.path.dirname(os.path.dirname(base_path))
eugene_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')


def change_dates(eugene_file_path):
    with open(eugene_file_path, 'r') as data_file:
        lines = data_file.readlines()

    current_date = datetime.now()

    for i, line in enumerate(lines, 1):

        start = line.find('. ') + 2

        date_string = line[start:start + 26]

        date_original = datetime.strptime(date_string.strip(), '%Y-%m-%d %H:%M:%S.%f')

        if i == 1:
            new_date = date_original + timedelta(days=7)
            print(new_date.strftime('%Y-%m-%d %H:%M:%S.%f'))

        elif i == 2:
            days = ["понедельник", "вторник", "среда", "четверг",
                    "пятница", "суббота", "воскресенье"]
            print(days[date_original.weekday()])

        elif i == 3:
            days_from_today = (current_date - date_original).days
            print(days_from_today)


change_dates(eugene_file_path)
