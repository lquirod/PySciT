from flask import redirect, render_template, url_for, make_response
from PyTSys_web import app
from markupsafe import Markup
from datetime import datetime

def download(text, name, type, err = ''):
    try:
        response = make_response(text)
        cd = 'attachment; filename='+name
        response.headers['Content-Disposition'] = cd
        response.mimetype = type
        return response
    except Exception:
        return messagePage(('Error saving '+err))

logs = []

def addLog(msg):
    date = datetime.now().strftime("%m/%d/%Y, %H:%M- ")
    newLog = [date, msg]
    logs.insert(0, newLog)
    return newLog

@app.route('/download/logs/', methods=["GET", "POST"])
def downloadLogs():
    downloadName = datetime.now().strftime("%m-%d-%Y_%H-%M")
    logText = [' '.join(elem) for elem in logs]
    return download( "\n".join(reversed(logText)), 'log_'+downloadName, 'text/plain', 'the logs')

@app.context_processor
def logFuction():
    return dict(LOG=logs)

@app.route('/help/', methods=["GET", "POST"])
def helpPage():
    return render_template("static/help.html")

@app.route('/msg/', methods=["GET", "POST"])
def messagePage(msg=None, err = True):
    print('baia '+msg+' y err is '+str(err))
    if msg == None or msg == '':
        return redirect(url_for('homePage'))
    else:
        return render_template("static/messagePage.html", MSG = msg, errMSG = err)


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

