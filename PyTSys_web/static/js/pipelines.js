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
/*  ---- Pipeline operations ---- */
function changeNamePipeline() {
    newName = document.getElementById('newName').value.trim()
    // window.alert("Hey "+newName)
    if (newName != '' && newName != document.getElementById('thePipeName').innerHTML.trim()) {
        $.ajax({
            data: JSON.stringify({ newName: newName }),
            contentType: 'application/json',
            url: '/operate/pipeline/' + numPipe + '/name/',
            type: 'post',
            beforeSend: function () {
                text.textContent = 'Renaming pipeline...';
            },
            success: function (ret) {
                if (ret.response) {
                    text.textContent = '';
                    document.getElementById('thePipeName').textContent = newName
                } else {
                    text.textContent = ret.err;
                }
                addViewLog(ret.newLog);
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                toggleModify();
                text.textContent = " Status: " + textStatus + "; Error: " + errorThrown;
            }
        });
    } else {
        text.textContent = "The new name can't be empty";
    }
}
/*  ---- Step operations (add) ---- */
function addStepToPipe() {
    var position = document.getElementById("position").value
    var theAddStep = document.querySelector('input[name="addStepTr"]:checked').value;
    // window.alert('Got the '+theAddStep+' in pos '+position)
    $.ajax({
        contentType: 'application/json',
        url: '/operate/pipeline/' + numPipe + '/addStep/',
        data: JSON.stringify({ position: position, theAddStep: theAddStep }),
        type: 'post',
        beforeSend: function () {
            popupClose()
            text.textContent = 'Adding new step...';
        },
        success: function (ret) {
            if (ret.response) {
                text.textContent = 'Done, updating changes... ';
                location.reload();
            } else {
                text.textContent = ret.err;
            }
            addViewLog(ret.newLog);
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            text.textContent = " Status: " + textStatus + "; Error: " + errorThrown;
        }
    });
};
/*  ---- Step operations (move, delete) ---- */
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
    // var msg = "En applyChanges, op: " + op + " y arg: " + arg + " / "
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
        location.reload();
    }
    else {
        ret = { 'response': False, 'err': 'Operation not found' }
        addViewLog('Error: ' + op + ' failed')
    }
}
function operateStep(operation, arg) {
    // window.alert(operation+", "+arg)
    if (modify == true) {
        if (operation != 'DEL' || (operation == 'DEL' && confirm("Are you sure you want to delete step " + arg + "?")))

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
                    addViewLog(ret.newLog)
                },
                error: function (XMLHttpRequest, textStatus, errorThrown) {
                    toggleModify();
                    text.textContent = " Status: " + textStatus + "; Error: " + errorThrown;
                }
            });
    }
}
function operatePipeline(operation, arg) {
    // window.alert(operation+", "+arg)
    if (modify == true) {
        if (operation != 'DEL' || (operation == 'DEL' && confirm("Are you sure you want to delete the pipelines " + numPipe + "?")))
            $.ajax({
                // data: { op: operation, arg: arg }, //, etiquetas: etiquetasCheck},
                data: JSON.stringify({ op: operation, arg: arg }), //, etiquetas: etiquetasCheck},
                contentType: 'application/json',
                url: '/operate/pipeline/' + numPipe + '/operate/',
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
                    addViewLog(ret.newLog);
                    toggleModify();
                },
                error: function (XMLHttpRequest, textStatus, errorThrown) {
                    toggleModify();
                    text.textContent = " Status: " + textStatus + "; Error: " + errorThrown;
                }
            });
    }
}
