from flask import Flask, app
from PyTSys.MoreFunctions import *

class hola():

    @app.route('/')
    @app.route('/home/')
    def process():
        return "hello"

# @app.route("/kill")
# def kill():
#     id = request.args.get("id")
#     x = registrar.get(id)
#     x.close()
#     registrar.remove(id)
#     return render_template("killed.html")
