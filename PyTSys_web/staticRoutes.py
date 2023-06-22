
from flask import render_template
from PyTSys_web import app


@app.route('/help/')
def helpPage():
    return render_template("help.html")

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

