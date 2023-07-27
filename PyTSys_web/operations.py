from flask import jsonify, redirect, request, url_for
from PyTSys_web import app
from PyTSys_web.mainRoutes import *

#############################################################################################
# Datas #
@app.route('/datas/get<numberData>/download/',  methods=["GET", "POST"])
def downloadData(numberData=-1):
    nData = thisDataExist(numberData)
    if nData == None:
        return messagePage(('Error trying saving data: '+str(nData)))

    downloadCSVName = myUser.myDatas[nData].Name
    downloadCSV = myUser.myDatas[nData]
    downloadCSV = downloadCSV.Data.to_csv(index=False)
    theDownload = download(downloadCSV, downloadCSVName, 'text/csv')
    return theDownload if theDownload is not None else messagePage(('Error saving data nº'+str(nData)))

@app.route('/datas/get<numberData>/operate/name/',  methods=["GET", "POST"])
def operateDataNewName(numberData=None):
    if request.method == 'POST':
        nlog = ''
        nData = thisDataExist(numberData)
        if nData == None:
            ret = {'response': False, 'err': 'Not valid data to operate', 'newLog': nlog}
            return jsonify(ret)
        newName = request.json.get('newName')
        myUser.myDatas[nData].Name = newName
        nlog = addLog('Renamed Data '+str(nData)+' to '+newName)
        ret = {'response': True, 'err': 'Operation denied', 'newLog': nlog}
        return jsonify(ret)
    
    else:
        return redirect(url_for('theDataPage',numberData = numberData))

#############################################################################################
# Pipelines #
@app.route('/pipelines/get<numberPipeline>/operate/name/',  methods=["GET", "POST"])
def operatePipelineNewName(numberPipeline=None):
    if request.method == 'POST':
        nlog = ''
        nPipe = thisPipeExist(numberPipeline)
        if nPipe == None:
            ret = {'response': False, 'err': 'Not valid pipeline to operate', 'newLog': nlog}
            return jsonify(ret)
        
        newName = request.json.get('newName')
        myUser.myPipelines[nPipe].Name = newName
        nlog = addLog('Renamed Pipe '+str(nPipe)+' to '+newName)
        ret = {'response': True, 'err': 'Operation done', 'newLog': nlog}
        return jsonify(ret)
    
    else:
        return redirect(url_for('thePipelinePage',numberPipeline = numberPipeline))

@app.route('/pipelines/get<numberPipeline>/operate/steps/add/',  methods=["GET", "POST"])
def operatePipelineAddStep(numberPipeline=-1):
    if request.method == 'POST':
        nPipe = thisPipeExist(numberPipeline)
        if nPipe == None:
            ret = {'response': False, 'err': 'Not valid pipeline to operate', 'newLog': nlog}
            return jsonify(ret)
          
        try:
            position = int(request.json.get('position'))
        except Exception:
            ret = {'response': response, 'err': err, 'newLog': nlog}
            return jsonify(ret)

        theTr = request.json.get('theAddStep')
        if myUser.addStep(mTr.getTransformation(theTr),position, nPipe) == None:
            response = False
            err = 'Error, denied operation'
            nlog = addLog('Error adding pipe '+str(nPipe)+' step '+theTr+' position '+str(position))
        else:
            response = True
            err = 'Operation done'
            nlog = addLog('Add Pipe '+str(nPipe)+' step '+theTr+' position '+str(position))
        
        ret = {'response': response, 'err': err, 'newLog': nlog}
        return jsonify(ret)
    
    else:
        return redirect(url_for('thePipelinePage',numberPipeline = numberPipeline))

@app.route('/pipelines/get<numberPipeline>/operate/steps/',  methods=["GET", "POST"])
def operatePipelineStep(numberPipeline=None):
    if request.method == 'POST':
        nlog = ''
        nPipe = thisPipeExist(numberPipeline)
        if nPipe == None:
            ret = {'response': False, 'err': 'Not valid pipeline to operate', 'newLog': nlog}
            return jsonify(ret)

        op = request.json.get('op')
        arg = int(request.json.get('arg'))
        if op == 'MOVUP':
            response = myUser.moveStep(arg, (arg-1), nPipe)
        elif op == 'MOVDOWN':
            response = myUser.moveStep(arg, (arg+1), nPipe)
        elif op == 'DEL':
            response = myUser.delStep(arg, nPipe)
        else:
            nlog = addLog('Error: '+op+' failed on pipeline '+str(nPipe))
            ret = {'response': False, 'err': 'Operation not found', 'newLog': nlog}
            return jsonify(ret)

        if response:
            nlog = addLog(op+' Pipe '+str(nPipe)+' step '+str(arg))
            err = 'Operation done'
        else:
            nlog = addLog('Error, denied operation: '+op+' Pipe '+str(nPipe)+' step '+str(arg))
            err = 'Error, denied operation'
        ret = {'response': response, 'err': err, 'newLog': nlog}
        return jsonify(ret)
    
    else:
        return redirect(url_for('thePipelinePage',numberPipeline = numberPipeline))

@app.route('/pipelines/get<numberPipeline>/operate/',  methods=["GET", "POST"])
def operatePipelineOperate(numberPipeline=None):
    if request.method == 'POST':
        nlog = ''
        nPipe = thisPipeExist(numberPipeline)
        if nPipe == None:
            ret = {'response': False, 'err': 'Not valid pipeline to operate', 'newLog': nlog}
            return jsonify(ret)

        op = request.json.get('op')
        args = request.json.get('args')
        if op == 'DEL':
            response = myUser.delPipeline(nPipe)
        elif op == '_______':
            print('')
        elif op == '_______':
            print('')
        else:
            nlog = addLog('Error: '+op+' failed on pipeline '+str(nPipe))
            ret = {'response': False, 'err': 'Operation not found', 'newLog': nlog}
            return jsonify(ret)

        if response:
            nlog = addLog(op+' Pipe '+str(nPipe))
            err = 'Operation done'
        else:
            nlog = addLog('Error, denied operation: '+op+' Pipe '+str(nPipe))
            err = 'Error, denied operation'
            
        ret = {'response': response, 'err': err, 'newLog': nlog}
        return jsonify(ret)
    
    else:
        return redirect(url_for('thePipelinePage',numberPipeline = numberPipeline))

@app.route('/pipelines/download/output',  methods=["GET", "POST"])
def downloadOutputPipeline():
    if request.method == 'POST':
        button = request.form['submit_button']
        title = request.form['title']+'_'+button
        text = request.form['text_'+button]
        isHTMLtable = True if request.form.get('check_'+button) else False

        if isHTMLtable:
            theOutput = text
            theOutput = pd.read_html(theOutput)
            theOutput = theOutput[0].to_csv(index=False)
            theDownload = download(theOutput, title, 'text/csv', True)
        else:
            theDownload = download(text, title, 'text/plain', True)

        if theDownload is None:
            msg ='Output couldn\'t be downloaded'
            err = True
            return render_template("static/messagePage.html", MSG = msg, errMSG = err, isList = isinstance(msg, list)) 
        else:
            msg ='Output downloaded sucessfully'
            err= False
            return theDownload
    else:
        return redirect(url_for('mainPipeline'))