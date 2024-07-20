from library import Library


class LibraryApp:
    def __init__(self):
        self.library = Library()

    def run(self):
        while True:
            print("1. Добавить книгу")
            print("2. Удалить книгу")
            print("3. Найти книгу")
            print("4. Показать все книги")
            print("5. Изменить статус книги")
            print("6. Выйти")
            choice = input("Выберите действие: ")
            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.delete_book()
            elif choice == "3":
                self.search_books()
            elif choice == "4":
                self.display_books()
            elif choice == "5":
                self.update_status()
            elif choice == "6":
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

    def add_book(self):
        try:
            title = input("Введите название: ")
            author = input("Введите автора: ")
            year = input("Введите год: ")
            if not year.isdigit():
                raise ValueError("Год должен быть числом.")
            book = self.library.add_book(title, author, year)
            print(f"Книга добавлена с ID: {book.id}")
        except ValueError as e:
            print(f"Ошибка: {e}")

    def delete_book(self):
        try:
            book_id = input("Введите ID книги для удаления: ")
            if not self.library.delete_book(book_id):
                raise ValueError("Книга не найдена.")
            print("Книга удалена.")
        except ValueError as e:
            print(f"Ошибка: {e}")

    def search_books(self):
        title = input("Введите название для поиска (или оставьте пустым): ")
        author = input("Введите автора для поиска (или оставьте пустым): ")
        year = input("Введите год для поиска (или оставьте пустым): ")
        results = self.library.search_books(title, author, year)
        if results:
            for book in results:
                print(book.to_dict())
        else:
            print("Книги не найдены.")

    def display_books(self):
        books = self.library.display_books()
        if books:
            for book in books:
                print(book.to_dict())
        else:
            print("В библиотеке нет книг.")

    def update_status(self):
        try:
            book_id = input("Введите ID книги для изменения статуса: ")
            status = input("Введите новый статус (в наличии/выдана): ")
            if status not in ["в наличии", "выдана"]:
                raise ValueError("Некорректный статус. "
                                 "Используйте 'в наличии' или 'выдана'.")
            if not self.library.update_status(book_id, status):
                raise ValueError("Книга не найдена.")
            print("Статус книги обновлён.")
        except ValueError as e:
            print(f"Ошибка: {e}")
