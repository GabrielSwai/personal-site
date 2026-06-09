from flask import render_template, Blueprint, request
from mainapp.services import tone_parser

homeapp = Blueprint( 'homeroutes', __name__,
                      static_folder='static',
                      template_folder='templates')

@homeapp.route('/')
def home():
    return render_template('home.html')

# @homeapp.route('/worlds-best-mom')
# def mom():
#     return render_template('worlds-best-mom.html')

@homeapp.route('/tone-parser', methods=['GET', 'POST'])
def extract_tones():
    raw_phrases = request.form.get("phrases", "")
    default_tone = request.form.get("default_tone", "L")
    results = tone_parser.parse_phrases(
        raw_phrases=raw_phrases,
        default_tone=default_tone,
    )

    return render_template(
        "tone-parser.html",
        results=results,
        original_input=raw_phrases,
        default_tone=default_tone
    )