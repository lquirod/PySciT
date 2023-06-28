
from flask import redirect, render_template, url_for
from PyTSys_web import app


@app.route('/help/', methods=["GET", "POST"])
def helpPage():
    return render_template("static/help.html")

@app.route('/help/', methods=["GET", "POST"])
def messagePage(msg):
    return render_template("static/messagePage.html", MSG = msg)


@app.errorhandler(404)
def page_not_found(e):
    eMsg = '404 Page Not Found.What you were looking for is just not there.'
    # set the 404 status explicitly
    return render_template('static/messagePage.html', MSG = eMsg), 404

@app.errorhandler(405)
def method_not_allowed(e):
    eMsg = '405 Method Not Allowed The method is not allowed for the requested URL.'
    # set the 405 status explicitly
    return render_template('static/messagePage.html', MSG = eMsg), 405

