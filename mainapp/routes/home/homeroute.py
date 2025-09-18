from flask import render_template, Blueprint, request

homeapp = Blueprint( 'homeroutes', __name__,
                      static_folder='static',
                      template_folder='templates')

@homeapp.route('/')
def home():
    return render_template('home.html')