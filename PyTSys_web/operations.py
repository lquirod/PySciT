from flask import jsonify, redirect, render_template, request, url_for
from PyTSys_web import app
from PyTSys_web.mainRoutes import *
# import json, o

    # addLog("Created pipeline "+newPipe+", "+alg+": "+name)

@app.route('/operate/pipeline/<numberPipeline>/steps/',  methods=["GET", "POST"])
def operatePipelineStep(numberPipeline=None):
    print (request.method )
    if request.method == 'POST':
        total = len(myUser.myPipelines)
        try:
            nPipe = int(numberPipeline)
            if total == 0 or nPipe < 0 and total < nPipe :
                ret = {'respuesta': False, 'err': 'Not valid pipeline to operate'}
                return jsonify(ret)

        except Exception:
            ret = {'respuesta': False, 'err': 'Not valid pipeline to operate'}
            return jsonify(ret)

        op = request.json.get('op')
        arg = int(request.json.get('arg'))
        if op == 'MOVUP':
            respuesta = myUser.moveStep(arg, (arg-1), nPipe)
        elif op == 'MOVDOWN':
            respuesta = myUser.moveStep(arg, (arg+1), nPipe)
        elif op == 'DEL':
            respuesta = myUser.moveStep(arg, nPipe)
        else:
            ret = {'respuesta': False, 'err': 'Operation not found'}
            addLog('Error: '+op+' failed')
            return jsonify(ret)

        if respuesta:
            addLog(op+' Pipe '+str(nPipe)+' step '+str(arg))
        else:
            addLog('Error, denied operation: '+op+' Pipe '+str(nPipe)+' step '+str(arg))

        ret = {'respuesta': respuesta, 'err': 'Operation denied'}
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

