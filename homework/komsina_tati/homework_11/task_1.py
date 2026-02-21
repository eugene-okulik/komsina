from abc import abstractmethod


class Book:
    page_material = 'paper'
    text_exists = True

    def __init__(self, title, author, pages_cnt, ISBN, is_reserved):
        self.title = title
        self.author = author
        self.num_pages = pages_cnt
        self.ISBN = ISBN
        self.is_reserved = False

    def reserve(self):
        self.is_reserved = True

    def print_details(self):
        print(
            f'Название: {self.title}, автор: {self.author}, страниц: {self.num_pages}, материал: {self.page_material}',
            end='')
        if self.is_reserved:
            print(', зарезервирована')
        else:
            print()


book_1 = Book('Идиот', 'Достоевский', '550', '1234567890123', False)
book_2 = Book('Чапаев и пустота', 'Пелевин', '400', '1234567890124', False)
book_3 = Book('День опричника', 'Сорокин', '350', '1234567890125', False)
book_4 = Book('Рассказ служанки', 'Этвуд', '450', '1234567890126', False)
book_5 = Book('1984', 'Оруэлл', '280', '1234567890127', False)

book_3.is_reserved = True

book_1.print_details()
book_2.print_details()
book_3.print_details()
book_4.print_details()
book_5.print_details()


class Textbook(Book):
    def __init__(self, title, author, num_pages, isbn, subject, group, has_exercises, is_reserved):
        super().__init__(title, author, num_pages, isbn, is_reserved)
        self.subject = subject
        self.group = group
        self.has_exercises = has_exercises

    def print_details(self):
        print(
            f'Название: {self.title}, автор: {self.author}, страниц: {self.num_pages}, предмет: {self.subject}, класс: {self.group}',
            end='')
        if self.is_reserved:
            print(', зарезервирована')
        else:
            print()


textbook_1 = Textbook('Алгебра', 'Арефьева', 300, '1234567890128', "Математика", 9, True, False)
textbook_2 = Textbook('Геометрия', 'Латотина', 270, '1234567890128', "Математика", 11, True, False)
textbook_3 = Textbook('Химия', 'Кузьменкова', 410, '1234567890128', "Химия", 10, True, False)

textbook_1.reserve()

textbook_1.print_details()
textbook_2.print_details()
textbook_3.print_details()
