from flask import redirect, render_template, request, url_for
from PyTSys_web import app
from PyTSys_web.mainWeb import *
from PyTSys_web.staticRoutes import *

@app.context_processor
def logFuction():
    return dict(LOG=logs)

@app.route('/')
@app.route('/home/')
def homePage():
    return render_template("home.html", Name = myUser.Name)

@app.route('/ConfigurationList/', methods=["GET", "POST"])
def List():
    return render_template("static/ConfigurationList.html", 
                           allTr = mTr.getTransformationsList(), allALG= mAlg.getAlgorithmsList())

@app.route('/datas/', methods=["GET", "POST"])
def mainData():
    return render_template("mainDatas.html", Datas = myUser.myDatas)

@app.route('/pipelines/', methods=["GET", "POST"])
def mainPipeline():
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
        newPipe = str(myUser.addPipeline(mAlg.getAlgorithmPipe(alg, name))-1)
        addLog("Created pipeline "+newPipe+", "+alg+": "+name)
        return redirect(url_for('thePipelinePage',numberPipeline = newPipe))


    return render_template("createPipeline.html",  allALG= mAlg.getAlgorithmsList(), newName = name, errors = err)

@app.route('/pipelines/get<numberPipeline>/',  methods=["GET", "POST"])
def thePipelinePage(numberPipeline=None):
    total = len(myUser.myPipelines)
    name = ''
    err = []
    try:
        nPipe = int(numberPipeline)
        if total == 0 or nPipe < 0 and total < nPipe :
            return messagePage('It seems that the pipeline you want to access does not exist, '+
                               'pipeline not in range.')
        else:
            thePipelinePage = myUser.myPipelines[nPipe]

    except Exception:
        # return redirect(url_for('messagePage', 'It seems that the pipeline you want to access does not exist'))
        # return "gas"
        # msg=''
        # return render_template("static/messagePage.html", MSG = msg)
        return messagePage('It seems that the pipeline you want to access does not exist, '+
                               'not valid pipeline.')


    return render_template("thePipeline.html",  allALG= mAlg.getAlgorithmsList(), thePipeline = thePipelinePage, numPipe = numberPipeline, newName = name, errors = err)

