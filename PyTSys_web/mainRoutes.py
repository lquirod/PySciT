from flask import render_template
from PyTSys_web import app
from PyTSys_web.mainWeb import *

# myUser = user.UserActions('Cherished User')
# mTr = M.TR.ManageTransformations()
# mAlg = M.ALG.ManageAlgorithms()


@app.route('/')
@app.route('/home/')
def homePage():
    return render_template("home.html", Name = myUser.Name)

@app.route('/ConfigurationList/')
def List():
    allTr = mTr.getTransformationsList()
    return render_template("static/ConfigurationList.html", 
                           allTr = mTr.getTransformationsList(), allALG= mAlg.getAlgorithmsList())

@app.route('/datas/')
def mainData():
    allTr = mTr.getTransformationsList()
    return render_template("mainDatas.html", Datas = myUser.myDatas)

@app.route('/pipelines/')
def mainPipeline():
    allTr = mTr.getTransformationsList()
    return render_template("mainPipelines.html", Pipelines = myUser.myPipelines)

@app.route('/pipelines/new/')
def addAPipeline():
    allTr = mTr.getTransformationsList()
    return render_template("createPipeline.html",  allALG= mAlg.getAlgorithmsList(), Pipelines = myUser.myPipelines)
