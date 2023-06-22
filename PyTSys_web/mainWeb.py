# from flask import Flask, app
# from PyTSys.MoreFunctions import *
from flask import render_template
from PyTSys_web import app


@app.route('/')
@app.route('/home/')
def homePage():
    return render_template("home.html")

@app.route('/index.php/')
def aa():
    return "Hello leti"
# @app.route("/kill")
# def kill():
#     id = request.args.get("id")
#     x = registrar.get(id)
#     x.close()
#     registrar.remove(id)
#     return render_template("killed.html")
