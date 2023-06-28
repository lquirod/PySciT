from flask import redirect, render_template, request, url_for
from PyTSys_web import app
from PyTSys_web.mainWeb import *

# myUser = user.UserActions('Cherished User')
# mTr = M.TR.ManageTransformations()
# mAlg = M.ALG.ManageAlgorithms()


@app.route('/')
@app.route('/home/')
def homePage():
    return render_template("home.html", Name = myUser.Name)

@app.route('/ConfigurationList/', methods=["GET", "POST"])
def List():
    allTr = mTr.getTransformationsList()
    return render_template("static/ConfigurationList.html", 
                           allTr = mTr.getTransformationsList(), allALG= mAlg.getAlgorithmsList())

@app.route('/datas/', methods=["GET", "POST"])
def mainData():
    allTr = mTr.getTransformationsList()
    return render_template("mainDatas.html", Datas = myUser.myDatas)

@app.route('/pipelines/', methods=["GET", "POST"])
def mainPipeline():
    allTr = mTr.getTransformationsList()
    return render_template("mainPipelines.html", Pipelines = myUser.myPipelines)

@app.route('/pipelines/new/',  methods=["GET", "POST"])
def addAPipeline():
    name = ''
    err = []

    if request.method == 'POST':
        name = request.form['newName']
        alg = request.form['selectAlg']
        # return redirect(url_for('success',name = user))
        # err =['nombre es '+name,
        #     'alg es '+alg
        # ]
        # newPipe = mAlg.getAlgorithmPipe(alg, name)
        newPipe = myUser.addPipeline(mAlg.getAlgorithmPipe(alg, name))
        return redirect(url_for('thePipelinePage',numberPipeline = str(newPipe-1)))


    return render_template("createPipeline.html",  allALG= mAlg.getAlgorithmsList(), newName = name, errors = err)

@app.route('/pipelines/get<numberPipeline>/',  methods=["GET", "POST"])
def thePipelinePage(numberPipeline=None):
    total = len(myUser.myPipelines)
    name = ''
    err = []
    try:
        nPipe = int(numberPipeline)
        if total == 0 or nPipe is None or nPipe < 0 or total < nPipe :
            return None
        else:
            thePipelinePage = myUser.myPipelines[nPipe]
    except Exception:
        return redirect(url_for('mainPipeline'))
            

    return render_template("thePipeline.html",  allALG= mAlg.getAlgorithmsList(), thePipeline = thePipelinePage, numPipe = numberPipeline, newName = name, errors = err)

