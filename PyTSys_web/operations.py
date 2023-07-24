from flask import jsonify, redirect, request, url_for
from PyTSys_web import app
from PyTSys_web.mainRoutes import *

#############################################################################################
# Datas #
@app.route('/download/data/<numberData>/',  methods=["GET", "POST"])
def downloadData(numberData=-1):
    nData = thisDataExist(numberData)
    if nData == None:
        return messagePage(('Error trying saving data: '+str(nData)))

    downloadCSVName = myUser.myDatas[nData].Name
    downloadCSV = myUser.myDatas[nData]
    downloadCSV = downloadCSV.Data.to_csv(index=False)
    theDownload = download(downloadCSV, downloadCSVName, 'text/csv')
    return theDownload if theDownload is not None else messagePage(('Error saving data nº'+str(nData)))

@app.route('/operate/data/<numberData>/name/',  methods=["GET", "POST"])
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
@app.route('/operate/pipeline/<numberPipeline>/addStep/',  methods=["GET", "POST"])
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

@app.route('/operate/pipeline/<numberPipeline>/name/',  methods=["GET", "POST"])
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

@app.route('/operate/pipeline/<numberPipeline>/steps/',  methods=["GET", "POST"])
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
            nlog = addLog('Error: '+op+' failed')
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

@app.route('/download/pipeline/output',  methods=["GET", "POST"])
def downloadOutputPipeline():
    if request.method == 'POST':
        num = request.json.get('num')
        title = request.json.get('title')
        text = request.json.get('text')
        isCSV = request.json.get('isCSV')
        err = ''
        print(num)
        print(title)
        print(text)
        print(isCSV)

        if isCSV:
            # print('\n++CSV en '+str(i)+' con contenido: '+output[1][i]+', y de nombre como: '+output[0]+'_'+str(i))
            theOutput = text
            theOutput = pd.read_html(theOutput)
            theOutput = theOutput.Data.to_csv(index=False)
            theDownload = download(theOutput, title, 'text/csv', True)
        else:
            # print('\nno CSV en '+str(i)+' con contenido: '+output[1][i]+', y de nombre como: '+output[0]+'_'+str(i))

            theDownload = download(text, title, 'text/plain', True)

        if theDownload is None:
            err = 'Error saving the output nº '+str(num+1)
            res = False
        else:
            # outputDownloads.append(theDownload)
            res = True

        ret = {'response': res, 'err': err, 'download': theDownload}
        return jsonify(ret)
 
    else:
        return redirect(url_for('mainPipeline'))