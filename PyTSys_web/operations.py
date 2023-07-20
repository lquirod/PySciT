from flask import jsonify, redirect, request, url_for
from PyTSys_web import app
from PyTSys_web.mainRoutes import *
# import json, o

    # addLog("Created pipeline "+newPipe+", "+alg+": "+name)

@app.route('/download/data/<numberData>/',  methods=["GET", "POST"])
def downloadData(numberData=-1):
    done = True
    total = len(myUser.myDatas)
    try:
        nData = int(numberData)
        if total == 0 or nData < 0 and total < nData :
            done = False
    except Exception:
        return messagePage(('Error saving data '+str(nData)))

    if done == True:
        downloadCSVName = myUser.myDatas[nData].Name
        downloadCSV = myUser.myDatas[nData]
        downloadCSV = downloadCSV.Data.to_csv(index=False)
        return download(downloadCSV, downloadCSVName, 'text/csv', 'data nº'+str(nData))
    else:
        return messagePage(('Error saving data '+str(nData)))


@app.route('/operate/data/<numberData>/name/',  methods=["GET", "POST"])
def operateDataNewName(numberData=None):
    if request.method == 'POST':
        nlog = ''
        total = len(myUser.myDatas)
        try:
            nData = int(numberData)
            if total == 0 or nData < 0 and total < nData :
                ret = {'response': False, 'err': 'Not valid data to operate', 'newLog': nlog}
                return jsonify(ret)

        except Exception:
            ret = {'response': False, 'err': 'Not valid data to operate', 'newLog': nlog}
            return jsonify(ret)

        newName = request.json.get('newName')
        myUser.myDatas[nData].Name = newName
        nlog = addLog('Renamed Data '+str(nData)+' to '+newName)
        ret = {'response': True, 'err': 'Operation denied', 'newLog': nlog}
        return jsonify(ret)
    
    else:
        return redirect(url_for('theDataPage',numberData = numberData))



@app.route('/operate/pipeline/<numberPipeline>/name/',  methods=["GET", "POST"])
def operatePipelineNewName(numberPipeline=None):
    if request.method == 'POST':
        nlog = ''
        total = len(myUser.myPipelines)
        try:
            nPipe = int(numberPipeline)
            if total == 0 or nPipe < 0 and total < nPipe :
                ret = {'response': False, 'err': 'Not valid pipeline to operate', 'newLog': nlog}
                return jsonify(ret)

        except Exception:
            ret = {'response': False, 'err': 'Not valid pipeline to operate', 'newLog': nlog}
            return jsonify(ret)

        newName = request.json.get('newName')
        myUser.myPipelines[nPipe].Name = newName
        nlog = addLog('Renamed Pipe '+str(nPipe)+' to '+newName)
        ret = {'response': True, 'err': 'Operation denied', 'newLog': nlog}
        return jsonify(ret)
    
    else:
        return redirect(url_for('thePipelinePage',numberPipeline = numberPipeline))


@app.route('/operate/pipeline/<numberPipeline>/steps/',  methods=["GET", "POST"])
def operatePipelineStep(numberPipeline=None):
    # print (request.method )
    if request.method == 'POST':
        nlog = ''
        total = len(myUser.myPipelines)
        try:
            nPipe = int(numberPipeline)
            if total == 0 or nPipe < 0 and total < nPipe :
                ret = {'response': False, 'err': 'Not valid pipeline to operate', 'newLog': nlog}
                return jsonify(ret)

        except Exception:
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
        else:
            nlog = addLog('Error, denied operation: '+op+' Pipe '+str(nPipe)+' step '+str(arg))

        ret = {'response': response, 'err': 'Operation denied', 'newLog': nlog}
        return jsonify(ret)
    
    else:
        return redirect(url_for('thePipelinePage',numberPipeline = numberPipeline))




# <?php
#     require_once "baseDatosProducto.php";
		
# 	header('Content-Type: application/json');
# 	$publicado = false;
#     if (isset($_SESSION['correo']) ) {
#         $user = getUser($_SESSION['correo']);
# 		if(($user['GestorSitio']))
# 			$publicado = true;
#     }

#     // if (isset($_GET['etiquetas']) ) 
# 	// 	$etiquetas = $_GET['etiquetas'];
# 	// else
# 	// 	$etiquetas = [];

# 	$busca = $_GET['busca'];

# 	$idProductos = buscaProducto("busca", [], $publicado);
# 	// $idProductos = buscaProducto($busca, $etiquetas, $publicado);

# 	$todosProductos = getProducto($idProductos);
# 	foreach($todosProductos as &$unProducto) {
# 		$unProducto['Portada'] = getPortada($unProducto['ID']);
# 		$unProducto['Galeria'] = getGaleria($unProducto['ID']);
# 		$unProducto['Etiquetas'] = getEtiquetas($unProducto['ID']);
# 	}

# 		echo(json_encode($todosProductos));
# ?>

