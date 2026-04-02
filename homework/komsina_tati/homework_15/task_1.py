import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

insert_query_student = "INSERT INTO students (name, second_name) VALUES (%s, %s)"
values = ('Bruce', 'Banner')
cursor.execute(insert_query_student, values)
student_id = cursor.lastrowid

insert_query_books = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
values = [('how to prevent crime2', student_id), ('how to save the world2', student_id)]
cursor.executemany(insert_query_books, values)

insert_query_groups = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
values = ('superhero2', 'april 2026', 'april 2027')
cursor.execute(insert_query_groups, values)
group_id = cursor.lastrowid

update_student_group_query = "UPDATE students SET group_id = %s WHERE id = %s"
values = (group_id, student_id)
cursor.execute(update_student_group_query, values)

insert_subjects_query = "INSERT INTO subjects (title) VALUES (%s)"
subjects = ['superhero subject 3', 'superhero subject 4']
subject_ids = {}
for subject in subjects:
    values = (subject,)
    cursor.execute(insert_subjects_query, values)
    subject_ids[subject] = cursor.lastrowid

insert_lesson_query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
lesson_ids = {}
for subject_name, subject_id in subject_ids.items():
    lessons = [
        f'Введение в {subject_name}',
        f'Продвинутый курс {subject_name}'
    ]

    lesson_ids[subject_name] = []

    for lesson_title in lessons:
        lesson_data = (lesson_title, subject_id)
        cursor.execute(insert_lesson_query, lesson_data)

        lesson_id = cursor.lastrowid
        lesson_ids[subject_name].append({
            'title': lesson_title,
            'id': lesson_id
        })

insert_marks_query = "INSERT INTO marks (student_id, lesson_id, value) VALUES (%s, %s, %s)"
for subject_name, lessons in lesson_ids.items():
    for lesson in lessons:
        lesson_id = lesson['id']
        grade_value = 9 if lesson_id % 2 == 0 else 10

        values = (student_id, lesson_id, grade_value)
        cursor.execute(insert_marks_query, values)

db.commit()

# Все оценки студента
print("\nОценки о студента ")
cursor.execute("SELECT value FROM marks WHERE student_id = %s", (student_id,))
print(cursor.fetchall())

# Все книги, которые находятся у студента
print("\nКниги студента ")
cursor.execute("SELECT title FROM books WHERE taken_by_student_id = %s", (student_id,))
print(cursor.fetchall())

# Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий и предметов (всё одним запросом с использованием Join)
print("\nИнформация о студенте ")
final_query = '''
SELECT s.name, s.second_name, s.group_id, g.title, g.start_date, g.end_date, b.title, m.value, l.title, s2.title
FROM students s
JOIN `groups` g ON s.group_id = g.id
JOIN books b ON s.id = b.taken_by_student_id
JOIN marks m ON m.student_id = s.id
JOIN lessons l ON l.id = m.lesson_id
JOIN subjects s2 ON s2.id = l.subject_id
WHERE s.id = %s
'''
cursor.execute(final_query, (student_id,))
print(cursor.fetchall())

db.close()
