from flask import render_template
from app import app
import os


@app.template_filter('autoversion')
def autoversion_filter(filename):
    fullpath = os.path.join('app/',filename[1:])
    try:
        timestamp = str(os.path.getmtime(fullpath))
    except OSError:
        return filename
    newfilename = "{0}?v={1}".format(filename,timestamp)
    return newfilename

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', title='Home')

@app.route("/faq")
def faq():
    return render_template('faq.html', title="FAQs")

@app.route("/projects")
def projects():
    return render_template('projects.html', title="Projects")