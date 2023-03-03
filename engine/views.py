from flask import Blueprint, redirect

engine = Blueprint('engine', __name__)

@engine.route('/')
def home():
    return redirect('/portfolio')