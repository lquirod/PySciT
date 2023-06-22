from flask import render_template
from PyTSys_web import app
from PyTSys_web.mainWeb import *

# myUser = user.UserActions('Cherished User')
# mTr = M.TR.ManageTransformations()
# mAlg = M.ALG.ManageAlgorithms()


@app.route('/')
@app.route('/home/')
def homePage():
    myUser.Name
    
    return render_template("home.html", Name = myUser.Name)

@app.route('/ListTransformations/')
def List():
    allTr = mTr.getTransformationsList()
    return render_template("ListTransformations.html", allTr = allTr)
