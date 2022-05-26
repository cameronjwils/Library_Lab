from db.run_sql import run_sql

from models.author import Author
from models.book import Book
import repositories.author_repository as author_repository

def delete_all():
    sql = "DELETE  FROM books"
    run_sql(sql)

def save(task):
    sql = "INSERT INTO tasks (description, user_id, duration, completed) VALUES (?, ?, ?, ?) RETURNING *"
    values = [task.description, task.user.id, task.duration, task.completed]
    results = run_sql(sql, values)
    id = results[0]['id']
    task.id = id
    return task

def select_all():
    books = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = author_repository.select(row['user_id'])
        book = Book(row['title'], author, row['id'])
        books.append(book)
    return books