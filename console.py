import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author_1 = Author("W.Shakespeare")
author_repository.save(author_1)
author_2 = Author("G.Orwell")
author_repository.save(author_2)

book_1 = Book("Othello", author_1)
book_repository.save(book_1)
book_2 = Book("Animal Farm", author_2)
book_repository.save(book_2)

pdb.set_trace()