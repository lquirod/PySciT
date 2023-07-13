/* Pipelines JS functions */
/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */
/*  ---- Initial settings ---- */
document.addEventListener('DOMContentLoaded', function () {
    // window.alert( sessionStorage.getItem("BlockLog"))
    modify = false;
    text = document.getElementById('errPipeSection');
}, false);

/*  ---- Modify toggle button ---- */
function checkSaveColumn(element, num) {
    // window.alert(num)
    window.alert('dROW-'+num)
    var section = document.getElementById('dROW-'+num).value.trim()
    if (element.checked) {

        // window.alert("Cambiado a true")
        section.classList.remove('Darker');
    }
    else {
        section.classList.add('Darker');
    }
    // window.alert( sessionStorage.getItem("BlockLog"))
}
/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */
/*  ---- Pipeline operations ---- */
function changeNameData() {
    newName = document.getElementById('newName').value.trim()
    window.alert("Hey "+newName)
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
// /*  ---- Step operations ---- */
// function switchAlg(from, to) {
//     var fromTR = document.getElementById("TR-" + from);
//     var toTR = document.getElementById("TR-" + to);
//     if (fromTR.classList.contains('boldText')) {
//         fromTR.classList.remove("boldText");
//         toTR.classList.add("boldText");
//     } else if (toTR.classList.contains('boldText')) {
//         toTR.classList.remove('boldText');
//         fromTR.classList.add('boldText');
//     }
// }

// function moveupName(arg) {
//     var from = arg.toString();
//     var to = (parseInt(arg) - 1).toString();
//     var fromCOL = document.getElementById("COL-" + from);
//     var toCOL = document.getElementById("COL-" + to);
//     toCOL.innerHTML = fromCOL.innerHTML;
//     switchAlg(from, to);
// }

// function applyChangesStep(op, arg) {
//     // var msg = "En applyChanges, op: " + op + " y arg: " + arg + " / "
//     if (op === "MOVUP" || op === "MOVDOWN") {
//         if (op.valueOf() == "MOVUP") {
//             var from = arg.toString();
//             var to = (parseInt(arg) - 1).toString();
//         } else {
//             var from = arg.toString();
//             var to = (parseInt(arg) + 1).toString();
//         }
//         var fromCOL = document.getElementById("COL-" + from);
//         var toCOL = document.getElementById("COL-" + to);
//         var COL = fromCOL.innerHTML;
//         fromCOL.innerHTML = toCOL.innerHTML;
//         toCOL.innerHTML = COL;
//         switchAlg(from, to);
//     }
//     else if (op == 'DEL') {
//         location.reload();
//     }
//     else {
//         ret = { 'response': False, 'err': 'Operation not found' }
//         addLog('Error: ' + op + ' failed')
//     }
//     // msg = msg + '/ FIN / '
//     // text.textContent = msg;
// }
// function operateStep(operation, arg) {
//     // window.alert(operation+", "+arg)
//     if (modify == true) {
//         if (operation != 'DEL' || (operation == 'DEL' && confirm("Are you sure you want to delete step " + arg + "?")))

//             $.ajax({
//                 // data: { op: operation, arg: arg }, //, etiquetas: etiquetasCheck},
//                 data: JSON.stringify({ op: operation, arg: arg }), //, etiquetas: etiquetasCheck},
//                 contentType: 'application/json',
//                 url: '/operate/pipeline/' + numPipe + '/steps/',
//                 type: 'post',
//                 beforeSend: function () {
//                     toggleModify();
//                     text.textContent = 'Operating, wait please...';
//                 },
//                 success: function (ret) {
//                     if (ret.response) {
//                         text.textContent = '';
//                         applyChangesStep(operation, arg);
//                     } else {
//                         text.textContent = ret.err;
//                     }
//                     toggleModify();
//                 },
//                 error: function (XMLHttpRequest, textStatus, errorThrown) {
//                     toggleModify();
//                     text.textContent = " Status: " + textStatus + "; Error: " + errorThrown;
//                 }
//             });
//     }
// }
// function operatePipeline(operation, arg) {
//     // window.alert(operation+", "+arg)
//     if (modify == true) {
//         if (operation != 'DEL' || (operation == 'DEL' && confirm("Are you sure you want to delete the pipelines " + numPipe + "?")))
//             $.ajax({
//                 // data: { op: operation, arg: arg }, //, etiquetas: etiquetasCheck},
//                 data: JSON.stringify({ op: operation, arg: arg }), //, etiquetas: etiquetasCheck},
//                 contentType: 'application/json',
//                 url: '/operate/pipeline/' + numPipe + '/operate/',
//                 type: 'post',
//                 beforeSend: function () {
//                     toggleModify();
//                     text.textContent = 'Operating, wait please...';
//                 },
//                 success: function (ret) {
//                     if (ret.response) {
//                         text.textContent = '';
//                         applyChangesStep(operation, arg);
//                     } else {
//                         text.textContent = ret.err;
//                     }
//                     addViewLog(ret.newLog);
//                     toggleModify();
//                 },
//                 error: function (XMLHttpRequest, textStatus, errorThrown) {
//                     toggleModify();
//                     text.textContent = " Status: " + textStatus + "; Error: " + errorThrown;
//                 }
//             });
//     }
// }
