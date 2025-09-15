class Book:
    all = []

    def __init__(self, title):
        if not isinstance(title, str) or not title.strip():
            raise Exception("Title must be a non-empty string")
        self.title = title
        Book.all.append(self)

    def __repr__(self):
        return f"Book('{self.title}')"
    
    def contracts(self):
        """Retourne tous les contrats liés à ce livre"""
        return [c for c in Contract.all if c.book == self]

    def authors(self):
        return [c.author for c in self.contracts()]


class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise Exception("Name must be a non-empty string")
        self.name = name
        Author.all.append(self)

    def __repr__(self):
        return f"Author('{self.name}')"

    # -------------------
    # Méthodes demandées
    # -------------------
    def contracts(self):
        """Retourne tous les contrats liés à cet auteur"""
        return [c for c in Contract.all if c.author == self]

    def books(self):
        """Retourne tous les livres liés à cet auteur via des contrats"""
        return [c.book for c in self.contracts()]

    def sign_contract(self, book, date, royalties):
        """Crée et retourne un nouveau contrat"""
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        """Somme des royalties de tous les contrats"""
        return sum(c.royalties for c in self.contracts()) 


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        # Validations
        if not isinstance(author, Author):
            raise Exception("author must be an instance of Author")
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        if not isinstance(date, str) or not date.strip():
            raise Exception("date must be a non-empty string")
        if not isinstance(royalties, int) or royalties < 0:
            raise Exception("royalties must be a positive integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    def __repr__(self):
        return f"Contract({self.author.name}, {self.book.title}, {self.date}, {self.royalties}%)"
    
    @classmethod
    def contracts_by_date(cls, date):
        """Retourne tous les contrats signés à une date donnée"""
        return [c for c in cls.all if c.date == date]