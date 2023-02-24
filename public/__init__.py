from flask import Blueprint

public = Blueprint('public', import_name='public', template_folder='templates', static_folder='static')

from . import views