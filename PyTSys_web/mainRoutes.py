from flask import jsonify, redirect, render_template, request, url_for
from PyTSys_web import app
from PyTSys_web.mainWeb import *
from PyTSys_web.staticRoutes import *

# if __name__ == "__main__":
#     from waitress import serve
#     serve(app, host="0.0.0.0", port=8080)
# Now you can start your production-ready server with python app.py.

# shell
# python app.py
# The server will be accessible at http://localhost:8080.

#############################################################################################
# Some useful functions #
def thisDataExist(numberData=None, total = None):
    if total == None:
        total = len(myUser.myDatas)
    try:
        nData = int(numberData)
        if total == 0 or nData < 0 and total < nData :
            return None
        else:
            return nData
    except Exception:
        return None

def thisPipeExist(numberPipeline=None, total = None):
    if total == None:
        total = len(myUser.myPipelines)
    try:
        nPipe = int(numberPipeline)
        if total == 0 or nPipe < 0 and total < nPipe :
            return None
        else:
            return nPipe
    except Exception:
        return None

#############################################################################################
# Routes #
@app.route('/')
@app.route('/home/')
def homePage():
    return render_template("home.html", Name = myUser.Name, numPipes = len(myUser.myPipelines), numDatas = len(myUser.myDatas))

@app.route('/ConfigurationList/', methods=["GET", "POST"])
def List():
    return render_template("static/ConfigurationList.html", 
                           allTr = mTr.getTransformationsList(), allALG= mAlg.getAlgorithmsList())

########### Data routes ###########
@app.route('/datas/', methods=["GET", "POST"])
def mainData():
    return render_template("mainDatas.html", Datas = myUser.myDatas)

@app.route('/datas/new/',  methods=["GET", "POST"])
def addAData():
    err = []    
    if request.method == 'POST':
        if request.form.get('checkHasCols'):
            checkHasCols = True
        else:
            checkHasCols = False
        theFile = request.files.get('loadFile')
        return addADataLoad(theFile, checkHasCols, True)

    return render_template("createData.html", loaded = False, errors = err)

@app.route('/datas/new/load',  methods=["GET", "POST"])
def addADataLoad(theFile = None, checkHasCols = True, SaveData = False):
    # if request.method == 'POST':
    if SaveData:
        if theFile is None:
            redirect(url_for('addAData'))

        checkHasCols = 0 if checkHasCols else None
        err = []
        try:
            theData = pd.read_csv(theFile, header=checkHasCols)
        except Exception:
            return render_template("createData.html", loaded = False,
                                   errors = 'Error loading data, check the file is not empty')

        theDataJSON = theData.to_json(orient = 'split')
        if theData.empty:
            return render_template("createData.html", loaded = False, errors = 'The data file is empty')
        maxLen = len(theData.index)
        loadNameFile = theFile.filename
        return render_template("createData.html", loaded = True, theData = theData.head(min(20, len(theData.index))), theDataJSON=theDataJSON, newName = loadNameFile, maxLen = maxLen, errors = err)       
    else:
        getChecks = request.json.get('checkCols')
        nData = ''
        nlog = ''
        err = ''
        if len(getChecks):
            newName = request.json.get('newName')
            nameCols = request.json.get('nameCols')
            theDataJSON = request.json.get('theData')
            theData = pd.read_json(theDataJSON, orient ='split').iloc[: , getChecks].copy()
            theData.columns = nameCols
            nData = myUser.createData(theData, newName) -1
            nlog = addLog('Created data '+str(nData)+': '+newName)
            res = True
        else:
            err = 'No columns selected'
            res = False
        ret = {'response': res, 'err': err, 'numData': nData, 'newLog': nlog}
        return jsonify(ret)


@app.route('/datas/get<numberData>/',  methods=["GET", "POST"])
@app.route('/datas/get<numberData>/<plain>',  methods=["GET", "POST"])
def theDataPage(numberData=None, plain=''):
    name = ''
    err = []
    nData = thisDataExist(numberData)
    if nData is None:
        if request.method == 'POST' and plain=='plain':
            ret = {'response': False,
                   'err': 'Error getting the data, it seems that the data you want to access does not exist'}
            return jsonify(ret)
        return messagePage('It seems that the data you want to access does not exist')
    
    theDataPage = myUser.myDatas[nData]
    if request.method == 'POST' and plain=='plain':
        if theDataPage.getNameCols():
            ret = {'response': True, 'selectColsData': theDataPage.getNameCols()}
        else:
            ret = {'response': False, 'err': 'This data has no data'}
        return jsonify(ret)
    
    return render_template("theData.html", theData = theDataPage, numData = numberData, newName = name, errors = err)

########### Pipelines routes ###########
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
        newPipe = str(myUser.addPipeline(mAlg.getAlgorithmPipe(alg, name))-1)
        addLog("Created pipeline "+newPipe+", "+alg+": "+name)
        return redirect(url_for('thePipelinePage',numberPipeline = newPipe))


    return render_template("createPipeline.html",  allALG= mAlg.getAlgorithmsList(), newName = name, errors = err)

@app.route('/pipelines/get<numberPipeline>/',  methods=["GET", "POST"])
def thePipelinePage(numberPipeline=None):
    nPipe = thisPipeExist(numberPipeline)
    if nPipe is None:
        return messagePage('It seems that the pipeline you want to access does not exist')

    thePipeline = myUser.myPipelines[nPipe]
    return render_template("thePipeline.html", thePipeline = thePipeline, numPipe = numberPipeline, allTr = mTr.getTransformationsList(), datasNames = list(myUser.getMyDatasNames().values()))

@app.route('/pipelines/get<numberPipeline>/parameters/',  methods=["GET", "POST"])
def thePipelineParametersPage(numberPipeline=None):
    nPipe = thisPipeExist(numberPipeline)
    if nPipe is None:
        return messagePage('It seems that the pipeline you want to access does not exist')

    thePipeline = myUser.myPipelines[nPipe]
    return render_template("thePipelineParameters.html", thePipeline = thePipeline, numPipe = numberPipeline)

