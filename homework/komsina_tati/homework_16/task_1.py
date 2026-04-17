import mysql.connector as mysql
import os
import dotenv
import csv

dotenv.load_dotenv()

csv_file_path = "/Users/tanya/PycharmProjects/komsina/homework/eugene_okulik/Lesson_16/hw_data/data.csv"

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=int(os.getenv('DB_PORT')),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor()

with open(csv_file_path, newline='') as csv_data_file:
    csv_data = csv.DictReader(csv_data_file)
    for line in csv_data:
        query = '''
            SELECT s.name, s.second_name, g.title, b.title, s2.title, l.title, m.value
            FROM students s
            INNER JOIN `groups` g ON s.group_id = g.id
            INNER JOIN books b ON s.id = b.taken_by_student_id
            INNER JOIN marks m ON m.student_id  = s.id
            INNER JOIN lessons l ON l.id = m.lesson_id
            INNER JOIN subjects s2 ON s2.id = l.subject_id
            WHERE s.name = %s AND second_name = %s
            AND g.title = %s AND b.title = %s
            AND s2.title = %s
            AND l.title = %s AND m.value = %s;
        '''
        values = (
            line['name'], line['second_name'], line['group_title'],
            line['book_title'], line['subject_title'],
            line['lesson_title'], line['mark_value']
        )
        cursor.execute(query, values)
        result = cursor.fetchone()
        if result is None:
            value = list(line.values())
            print(
                f"В БД нет данных по:\n"
                f"Student: {line['name']} {line['second_name']}, "
                f"group: {line['group_title']}, "
                f"book: {line['book_title']}, "
                f"subject: {line['subject_title']}, "
                f"lesson: {line['lesson_title']}, "
                f"mark: {line['mark_value']}"
            )

db.close()
