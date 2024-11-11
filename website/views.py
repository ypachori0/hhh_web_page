# views.py
from flask import Blueprint

# blueprint file that has URLs defined
views = Blueprint('views', __name__)

# defining views

# function to go to home page
@views.route('/')
def home():
    return "<h1>Test</h1>"
