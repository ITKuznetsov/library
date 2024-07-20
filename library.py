import json
import os

from book import Book


class Library:
    def __init__(self, filepath="library.json"):
        self.filepath = filepath
        self.books = self.load_books()

    def load_books(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Book.from_dict(book) for book in data]
        return []

    def save_books(self):
        with open(self.filepath, "w", encoding="utf-8") as file:
            json.dump([book.to_dict() for book in self.books],
                      file, ensure_ascii=False, indent=4)

    def add_book(self, title, author, year):
        book = Book(title, author, year)
        self.books.append(book)
        self.save_books()
        return book

    def delete_book(self, book_id):
        book = self.find_book_by_id(book_id)
        if book:
            self.books.remove(book)
            self.save_books()
            return True
        return False

    def find_book_by_id(self, book_id):
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    def search_books(self, title=None, author=None, year=None):
        results = []
        for book in self.books:
            if (title and title.lower() in book.title.lower()) or \
               (author and author.lower() in book.author.lower()) or \
               (year and year == book.year):
                results.append(book)
        return results

    def display_books(self):
        return self.books

    def update_status(self, book_id, status):
        book = self.find_book_by_id(book_id)
        if book:
            book.status = status
            self.save_books()
            return True
        return False
