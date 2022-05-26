from flask import Flask, render_template, request, redirect
from repositories import book_repository, author_repository
from models.book import Book

from flask import Blueprint

library_blueprint = Blueprint("books", __name__)