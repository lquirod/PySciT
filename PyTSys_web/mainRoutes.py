from flask import redirect, render_template, request, url_for
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

@app.route('/')
@app.route('/home/')
def homePage():
    return render_template("home.html", Name = myUser.Name, numPipes = len(myUser.myPipelines), numDatas = len(myUser.myDatas))

@app.route('/ConfigurationList/', methods=["GET", "POST"])
def List():
    return render_template("static/ConfigurationList.html", 
                           allTr = mTr.getTransformationsList(), allALG= mAlg.getAlgorithmsList())

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
        return addADataLoad(theFile, checkHasCols)

    return render_template("createData.html", loaded = False, errors = err)

@app.route('/datas/new/load/',  methods=["GET", "POST"])
def addADataLoad(theFile = None, checkHasCols = True):
    if theFile is None:
        redirect(url_for('addAData'))
    if checkHasCols:
        checkHasCols = 0
    else:
        checkHasCols = None

    err = []
    
    # name = request.form['newName']
    # theFile = request.files.get('loadFile')
    theData = pd.read_csv(theFile, header=checkHasCols)
    if theData.empty:
        return render_template("createData.html", loaded = False, errors = 'The data file is empty')
    maxLen = min(50, len(df. index))
    # loadNameFile = request.form['loadFile']
    # theFile = request.files.get('loadFile')
    loadNameFile = theFile.filename
    # previewData = pd.read_csv(loadNameFile)
    # alg = request.form['selectAlg']
    # return redirect(url_for('success',name = user))
    # err =['nombre es '+name,
    #     'alg es '+alg
    # ]
    # newPipe = mAlg.getAlgorithmPipe(alg, name)
    # if request.method == 'POST':
    #     name = request.form['newName']
    #     # loadNameFile = request.form['loadFile']
    #     # loadNameFile = request.files.get('loadFile')
    #     # previewData = pd.read_csv(loadNameFile)
    #     # mimetype = loadNameFile.content_type

    # else:
    #     return redirect(url_for('addAData'))

    return render_template("createData.html", loaded = True, theData = theData, newName = loadNameFile, maxLen = maxLen, errors = err)


@app.route('/datas/get<numberData>/',  methods=["GET", "POST"])
def theDataPage(numberData=None):
    total = len(myUser.myDatas)
    name = ''
    err = []
    try:
        nData = int(numberData)
        if total == 0 or nData < 0 and total < nData :
            return messagePage('It seems that the data you want to access does not exist, '+
                               'data not in range.')
        else:
            theDataPage = myUser.myDatas[nData]

    except Exception:
        return messagePage('It seems that the data you want to access does not exist, '+
                               'not valid data.')
    
    return render_template("theData.html", theData = theDataPage, numData = numberData, newName = name, errors = err)


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
    total = len(myUser.myPipelines)
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
    
    return render_template("thePipeline.html", thePipeline = thePipelinePage, numPipe = numberPipeline)

