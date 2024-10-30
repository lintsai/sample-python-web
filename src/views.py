from flask import Blueprint, render_template

main_view = Blueprint('main_view', __name__)

@main_view.route('/')
def index():
    return render_template('index.html')