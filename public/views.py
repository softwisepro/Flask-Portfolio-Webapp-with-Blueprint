from flask import render_template
from . import public

@public.route('/')
def index():
    developer = 'EricKweyunga'
    template_name = 'layout/portfolio.html'
    return render_template(template_name, developer=developer)

@public.route('/404')
def error_page():
    template_name = '404/404.html'
    return render_template(template_name)