# Класс библеотеки
class Library:
    def __init__(self) -> None:
        self.__lst_books = []
        self.__lst_members = []
    
    @property
    def lst_books(self):
        for i in self.__lst_books:
            print(i.__str__())
    
    @property
    def lst_members(self):
        for i in self.__lst_members:
            print(i.name, i.id)
    
    # сеттер списка с книгами в библиотеке для добавления новой книги
    def add_book(self, new_book) -> None:
        self.__lst_books.append(new_book)
    
    # сеттер списка с посетителями для добавления нового человека
    def register_member(self, member) -> None:
        self.__lst_members.append(member)
        
    # вывод описания библеотеки
    def __str__(self) -> str:
        return f'Library with {len(self.__lst_books)} books and {len(self.__lst_members)} members'

# Класс создания книг
class Book:
    def __init__(self, title, author, isbn, from_library: Library) -> None:
            self.title = title
            self.author = author
            self.isbn = isbn # Идентификатор книги
            self.available = True 
            from_library.add_book(self) # добавляем книгу в библеотеку(как объект)
     
            
    # изменяем состояние книги
    def change_available(self):
        self.available = not self.available
     
    # Красивый вывод книги при вызове экземпляра         
    def __str__(self) -> str:
         return f'Название: {self.title}. Автор: {self.author}. Доступна: {'Да'if self.available else 'Нет'}'

# Класс посетителся библиотеки
class LibraryMember:
    num_of_member = 0 # Счетчик для айдишника
    
    def __init__(self, name, lib: Library) -> None:
        self.name = name
        self.id = self.num_of_member
        LibraryMember.num_of_member += 1
        self.__borrowed_books = [] # Список взятых книг постетителем
        lib.register_member(self) # Передаем библеотеке нашего постетителя(как объект) 
    
    # геттер списка книг
    @property
    def borrowed_books(self):
        return self.__borrowed_books
    
    # берем книгу из библеотеки
    def borrow_book(self, book: Book) -> None:
        if book.available:
            self.__borrowed_books.append(book)
            book.change_available()
        else:
            print('Книга занята')
    
    # возращаем книгу
    def return_book(self, book: Book) -> None:
        if book in self.borrowed_books:
            self.__borrowed_books.remove(book)
            book.change_available()
        else:
            print('У вас нет этой книги')
    
    # красивый вывод пользователя и всех его книг
    def __str__(self) -> None:
        print(f'{self.name}(ID: {self.id}) borrowed:')
        for b in self.__borrowed_books:
            print(b.__str__())
            

# создадим библеотеку, две книги и троих посетителей
lib = Library()
b1 = Book('1984', 'Джордж Оруелл', 1243214, lib)
b2 = Book('Красная таблетка', 'Андрей Курпатов', 934218, lib)
m1 = LibraryMember('Oleg', lib)
m2 = LibraryMember('Olga', lib)
m3 = LibraryMember('Max', lib)

# выведем участников и книги в библиотеке
print(lib.__str__(), '\n')
lib.lst_members
print()
lib.lst_books
print()

m4 = LibraryMember('Stepan', lib) # создаем нового участника
m4.borrow_book(b1) # берем книгу 1984

# выводим все снова, и как видим все данные обновились
print(lib.__str__(), '\n')
lib.lst_members
print()
lib.lst_books
print()

# Вернем книгу
m4.return_book(b1)
lib.lst_books
print()

# пусть олег возьмет книгу, а потом ее попробует взять ольга
m1.borrow_book(b1)
print()
m1.__str__()

print()
m2.borrow_book(b1) # как видим книгу взять не получается