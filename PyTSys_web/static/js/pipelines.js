/* Pipelines JS functions */
/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */
/*  ---- Initial settings ---- */
document.addEventListener('DOMContentLoaded', function () {
    // window.alert( sessionStorage.getItem("BlockLog"))
    modify = false;
    text = document.getElementById('errPipeSection');
}, false);

/*  ---- Modify toggle button ---- */
function toggleModify(element) {
    // window.alert(element.checked)
    if (element.checked) {
        modify = true;
        // window.alert("Cambiado a true")
    } else {
        modify = false;
        // window.alert("Cambiado a false")
    }
}
function toggleModify() {
    var mov = document.getElementsByName('movStep');
    var del = document.getElementsByName('delStep');
    var buttonModify = document.getElementById('toggleModify');
    if (mov[0].classList.contains('Darker')) {
        for (var i = 0; i < mov.length; i++)
            mov[i].classList.remove('Darker');

        for (var i = 0; i < del.length; i++)
            del[i].classList.remove('Darker');

        buttonModify.classList.remove('b4');
        buttonModify.classList.add('b3');
        buttonModify.textContent = 'Modify enabled';
        modify = true;
    } else {
        for (var i = 0; i < mov.length; i++)
            mov[i].classList.add('Darker');

        for (var i = 0; i < del.length; i++)
            del[i].classList.add('Darker');

        buttonModify.classList.remove('b3');
        buttonModify.classList.add('b4');
        buttonModify.textContent = 'Modify disabled';
        modify = false;
    }
}
/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */
/*  ---- Step operations ---- */
function switchAlg(from, to) {
    var fromTR = document.getElementById("TR-" + from);
    var toTR = document.getElementById("TR-" + to);
    if (fromTR.classList.contains('boldText')) {
        fromTR.classList.remove("boldText");
        toTR.classList.add("boldText");
    } else if (toTR.classList.contains('boldText')) {
        toTR.classList.remove('boldText');
        fromTR.classList.add('boldText');
    }
}

function moveupName(arg) {
    var from = arg.toString();
    var to = (parseInt(arg) - 1).toString();
    var fromCOL = document.getElementById("COL-" + from);
    var toCOL = document.getElementById("COL-" + to);
    toCOL.innerHTML = fromCOL.innerHTML;
    switchAlg(from, to);
}

function applyChangesStep(op, arg) {
    var msg = "En applyChanges, op: " + op + " y arg: " + arg + " / "
    if (op === "MOVUP" || op === "MOVDOWN") {
        if (op.valueOf() == "MOVUP") {
            var from = arg.toString();
            var to = (parseInt(arg) - 1).toString();
        } else {
            var from = arg.toString();
            var to = (parseInt(arg) + 1).toString();
        }
        var fromCOL = document.getElementById("COL-" + from);
        var toCOL = document.getElementById("COL-" + to);
        var COL = fromCOL.innerHTML;
        fromCOL.innerHTML = toCOL.innerHTML;
        toCOL.innerHTML = COL;
        switchAlg(from, to);
    }
    else if (op == 'DEL') {
        // // text.textContent = 'DEL';
        // var rowDel = document.getElementById("TR-" + arg);
        // var parent = rowDel.parentNode;
        // var total = parent.childElementCount;
        // if (rowDel != parent.lastElementChild) {
        //     var i;
        //     for (i = (parseInt(arg) + 1); i < (total - 1); i++) {
        //         moveupName(i)
        //     }
        //     rowDel = parent.childNodes.item(i);
        // } else {
        //     // text.textContent = 'else';
        //     rowDel = parent.childNodes.item(parseInt(arg) - 1);
        // }
        // text.textContent = Array.from(rowDel.parentNode.children).indexOf(rowDel)
        // // rowDel.remove();
        // // text.textContent = i+'<- i and '+(parent.childElementCount-1);
        // // var newNum = 
        // // parent.lastElementChild.id = 'TR-';
        // // parent.lastElementChild.onclick = function () { Foo(param); };
        // // document.getElementById("a").onclick = function () { Foo(param); };

        location.reload();
    }
    else {
        ret = { 'response': False, 'err': 'Operation not found' }
        addLog('Error: ' + op + ' failed')
    }
    // msg = msg + '/ FIN / '
    // text.textContent = msg;
}
function operateStep(operation, arg) {
    // window.alert(operation+", "+arg)
    if (modify == true) {
        if( operation != 'DEL' || (operation == 'DEL' && confirm("Are you sure you want to delete step "+arg+"?"))) 

        $.ajax({
            // data: { op: operation, arg: arg }, //, etiquetas: etiquetasCheck},
            data: JSON.stringify({ op: operation, arg: arg }), //, etiquetas: etiquetasCheck},
            contentType: 'application/json',
            url: '/operate/pipeline/' + numPipe + '/steps/',
            type: 'post',
            beforeSend: function () {
                toggleModify();
                text.textContent = 'Operating, wait please...';
            },
            success: function (ret) {
                if (ret.response) {
                    text.textContent = '';
                    applyChangesStep(operation, arg);
                } else {
                    text.textContent = ret.err;
                }
                toggleModify();
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                toggleModify();
                text.textContent = " Status: " + textStatus + "; Error: " + errorThrown;
            }
        });
    }
}
