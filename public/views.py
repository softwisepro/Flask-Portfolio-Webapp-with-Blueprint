import sqlite3
from flask import render_template, request
from . import public

@public.route('/', methods = ['POST', 'GET'])
def index():
    developer = 'EricKweyunga'
    template_name = 'layout/portfolio.html'
    return render_template(template_name, developer=developer)




