import uuid


class Book:
    def __init__(self, title, author, year, status="в наличии"):
        self.id = str(uuid.uuid4())
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }

    @staticmethod
    def from_dict(data):
        book = Book(data["title"], data["author"], data["year"], data["status"])
        book.id = data["id"]
        return book
