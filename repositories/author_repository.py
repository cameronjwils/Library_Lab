from db.run_sql import run_sql

from models.author import Author
from models.book import Book

def delete_all():
    sql = "DELETE  FROM authors"
    run_sql(sql)

def save(user):
    sql = "INSERT INTO users (name) VALUES (?) RETURNING *"
    values = [user.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    user.id = id
    return user

def select_all():
    authors = []

    sql = "SELECT * FROM authors"
    results = run_sql(sql)

    for row in results:
        author = Author(row['name'], row['id'])
        authors.append(author)
    return authors

def select(id):
    author = None
    sql = "SELECT * FROM author WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        author = Author(result['name'], result['id'] )
    return author