/* Pipelines JS functions */
/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */
/*  ---- Initial settings ---- */
document.addEventListener('DOMContentLoaded', function () {
    modify = false;
    text = document.getElementById('errPipeSection');
    popupText = document.getElementById('errPopupSection');
    popupOptions = [];
    actualOperation = null;
    actualOutput = false;
    errDataSelector=  document.getElementById('errDataSelector');
}, false);

/*  ---- Modify toggle button ---- */
function toggleModify(element) {
    if (element.checked) {
        modify = true;
    } else {
        modify = false;
    }
}
function toggleModify(mode = true) {
    var mov = document.getElementsByName('movStep');
    var del = document.getElementsByName('delStep');
    var buttonModify = document.getElementById('toggleModify');
    if (mov[0].classList.contains('Darker')) {
        if (mode) {
            for (var i = 0; i < mov.length; i++)
                mov[i].classList.remove('Darker');

            for (var i = 0; i < del.length; i++)
                del[i].classList.remove('Darker');

            buttonModify.classList.remove('b4');
            buttonModify.classList.add('b3');
            buttonModify.textContent = 'Modify enabled';
            modify = true;
        }
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
/*  ---- Change pipeline ---- */
function changePipeline(operation) {
    var yesOperate = false
    var newName = ''
    if (operation == 'Renaming') {
        newName = document.getElementById('newName').value.trim()
        if (newName != '' && newName != document.getElementById('thePipeName').innerHTML.trim())
            yesOperate = true;
        else
            text.textContent = "The new name can't be empty";
    }

    if (operation == 'Deleting' && confirm("Are you sure you want to delete the pipelines " + numPipe + "?"))
        yesOperate = true

    if (yesOperate) {
        $.ajax({
            data: JSON.stringify({ op: operation, newName: newName }),
            contentType: 'application/json',
            url: '/pipelines/get' + numPipe + '/change',
            type: 'post',
            beforeSend: function () {
                text.textContent = operation + ' pipeline...';
            },
            success: function (ret) {
                if (ret.response) {
                    if (operation == 'Deleting')
                        window.location.replace("/pipelines");
                    if (operation == 'Renaming')
                        document.getElementById('thePipeName').textContent = newName
                }
                text.textContent = ret.err;
                addViewLog(ret.newLog);
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                toggleModify();
                text.textContent = " Status: " + textStatus + "; Error: " + errorThrown;
            }
        });
    }
}
/*  ---- Step operations (add) ---- */
function addStepToPipe() {
    var position = document.getElementById("position").value
    var theAddStep = document.querySelector('input[name="addStepTr"]:checked').value;
    $.ajax({
        contentType: 'application/json',
        url: '/pipelines/get' + numPipe + '/operate/steps/add',
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
/*  ---- operations ---- */
function applyChangesStep(op, arg) {
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
    } else if (op == 'DEL') {
        location.reload();
    } else {
        ret = { 'response': False, 'err': 'Operation not found' }
        addViewLog('Error: ' + op + ' failed')
    }
}
/*  ---- AJAX call to operate step ---- */
function operateStep(operation, arg) {
    if (modify == true) {
        if (operation != 'DEL' || (operation == 'DEL' && confirm("Are you sure you want to delete step " + arg + "?")))
            $.ajax({
                data: JSON.stringify({ op: operation, arg: arg }),
                contentType: 'application/json',
                url: '/pipelines/get' + numPipe + '/operate/steps/',
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
/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */
/*  ---- Data selector to pipeline operations ---- */
// Open selection
function popupSelectData(operation, title, options, mode = []) {
    if (popupWindow('dataSelector')) {
        document.getElementById("titleSelectData").innerHTML = title;
        actualOperation = operation;
        for (var i = 0; i < options.length; i++)
            popupOptions.push([options[i], ((typeof mode[i] === 'undefined') ? true : mode[i])])
    }
}
// Close selection
function popupClearSelectData() {
    document.getElementById("selectDataCols").innerHTML = '';
    document.getElementById("dataSelectorPreview").innerHTML = '';
    var theForm = document.getElementById("selectDataForm");
    if (theForm.childElementCount > 4)
        theForm.removeChild(theForm.lastChild);
    return theForm;
}
function pipelinePopupClose() {
    if (popupClose()) {
        popupClearSelectData().reset();
        actualOperation = null;
        popupOptions.length = 0;
        errDataSelector.textContent = '';
    }
}
// Show data selection options in a data
function selectColsDataShow(selectColsData) {
    var theOptionView = document.getElementById("selectDataCols")
    var br = document.createElement("br");
    // window.alert(popupOptions)
    for (var i = 0; i < popupOptions.length; i++) {
        let ptext = document.createTextNode(popupOptions[i][0] + ': ');
        theOptionView.appendChild(ptext);
        let theSelect = document.createElement('select');
        theSelect.name = 'selectData';

        let anOption = document.createElement('option');
        if (popupOptions[i][1]) {
            theSelect.required = 'required';
            anOption.disabled = 'disabled';
            anOption.innerHTML = 'Required';
            anOption.value = '';

        } else {
            anOption.required = false;
            anOption.disabled = false;
            anOption.innerHTML = 'None';
            anOption.value = 'None';
        }
        anOption.selected = true;
        theSelect.name = popupOptions[i][0];
        theSelect.appendChild(anOption);

        for (var j = 0; j < selectColsData.length; j++) {
            anOption = document.createElement('option');
            anOption.innerHTML = selectColsData[j]
            anOption.value = j;
            theSelect.appendChild(anOption);
        }
        theOptionView.appendChild(theSelect);
        theOptionView.appendChild(br.cloneNode(true));
    }
    var theSubmitButton = document.createElement('button');
    theSubmitButton.classList.add('aButton');
    theSubmitButton.classList.add('b4');
    theSubmitButton.classList.add('s16');
    theSubmitButton.classList.add('yesPadding');
    theSubmitButton.innerHTML = 'Accept';
    document.getElementById("selectDataForm").appendChild(theSubmitButton)
}

function selectDataChanged() {
    popupClearSelectData()
    var selectData = document.getElementById("selectData").value
    $.ajax({
        contentType: 'application/json',
        url: '/datas/get' + selectData + '/plain',
        type: 'post',
        beforeSend: function () {
            popupText.textContent = 'Getting data...';
        },
        success: function (ret) {
            if (ret.response) {
                popupText.textContent = '';
                selectColsDataShow(ret.selectColsData);
                document.getElementById("dataSelectorPreview").insertAdjacentHTML('beforeend', ret.selectData);
            } else {
                popupText.textContent = ret.err;
            }
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            popupText.textContent = " Status: " + textStatus + "; Error: " + errorThrown;
        }
    });
}
/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */
/*  ---- AJAX call to operate pipeline ---- */
function operatePipeline() {
    if (actualOperation != null) {
        var form = document.getElementById('selectDataForm');
        var theSelects = form.getElementsByTagName("select");
        var theInputs = [];
        // var paramDict = {};
        // var regExp = /\(([^)]+)\)/;
        for (let i = 0; i < theSelects.length; i++) {
            // var name = regExp.exec(theSelects[i].name);
            // if (name)
            //     paramDict[name[1]] = theSelects[i].value;
            // else
            theInputs.push(theSelects[i].value);
        }

        $.ajax({
            data: JSON.stringify({ op: actualOperation, inputs: theInputs }), //, paramDict: paramDict }),
            contentType: 'application/json',
            url: '/pipelines/get' + numPipe + '/operate',
            type: 'post',
            beforeSend: function () {
                toggleModify(false);
                text.textContent = 'Operating pipeline with ' + actualOperation + '...';
                errDataSelector.textContent = 'Operating pipeline with ' + actualOperation + '...';
            },
            success: function (ret) {
                text.textContent = '';
                if (ret.response) {
                    setOutputPipeline(actualOperation, ret.output, ret.isHTMLtable);
                    pipelinePopupClose()
                } else {
                }
                errDataSelector.textContent = ret.err;
                addViewLog(ret.newLog);
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                text.textContent = " Status: " + textStatus + "; Error: " + errorThrown;
            }
        });
    }
}
/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */
/*  ---- Manage output of pipeline operation ---- */
function setOutputPipeline(title, text, isHTMLtable = []) {
    var pipeOutput = document.getElementById("pipeOutput");
    if (!actualOutput) {
        actualOutput = true;
        pipeOutput.classList.remove('hidden');

        var closeOutput = document.createElement('button');
        closeOutput.innerHTML = 'Close';
        closeOutput.type = 'button';
        closeOutput.onclick = closeOutputPipeline;
        closeOutput.style.position = 'sticky';
        closeOutput.style.top = '0px';
        closeOutput.style.right = '0px';
        closeOutput.classList.add('aButton');
        closeOutput.classList.add('pointer');
        closeOutput.classList.add('yesPadding');
        closeOutput.classList.add('right');
        closeOutput.classList.add('b1');
        closeOutput.classList.add('s16');
        pipeOutput.appendChild(closeOutput);
    }

    var br = document.createElement("br");
    var aForm = document.createElement('form');
    aForm.action = "/pipelines/download/output";
    aForm.method = "post";
    aForm.target = "_blank"

    var addText = document.createElement('h2');
    title = new Date().toLocaleString() + '- ' + title
    addText.innerHTML = title;
    aForm.appendChild(addText);
    var theTitle = document.createElement('input');
    theTitle.type = 'hidden';
    theTitle.name = 'title';
    theTitle.value = title;
    aForm.appendChild(theTitle);

    for (let i = 0; i < text.length; i++) {
        let aHTMLtable = isHTMLtable.includes(i);
        if (aHTMLtable) {
            aForm.insertAdjacentHTML('beforeend', text[i]);
        } else {
            var addText = document.createElement('p');
            addText.innerHTML = text[i];
            aForm.appendChild(addText);
        }
        var checkTable = document.createElement('input');
        checkTable.type = 'checkbox';
        checkTable.name = 'check_' + i;
        checkTable.checked = aHTMLtable;
        checkTable.style.display = 'none'
        aForm.appendChild(checkTable);

        var theSubmitOutput = document.createElement('input');
        theSubmitOutput.type = 'hidden';
        theSubmitOutput.name = 'text_' + i;
        theSubmitOutput.value = text[i];
        aForm.appendChild(theSubmitOutput);

        let saveOutput = document.createElement('button');
        saveOutput.innerHTML = '&#8593; Save output &#8593;'
        saveOutput.classList.add('aButton');
        saveOutput.classList.add('b4');
        saveOutput.classList.add('s16');
        saveOutput.classList.add('yesPadding');
        saveOutput.classList.add('yesMargin');
        saveOutput.name = 'submit_button';
        saveOutput.value = i;
        aForm.appendChild(saveOutput)
        aForm.appendChild(br.cloneNode(true));
    }
    pipeOutput.insertBefore(aForm, pipeOutput.firstChild);
    pipeOutput.scrollIntoView({ behavior: 'smooth' });
}

function closeOutputPipeline() {
    if (actualOutput && confirm("Do you want to close the Output pipeline?\nIf you close it, your outputs will be lost. Do not forget to save things first!")) {
        var pipeOutput = document.getElementById("pipeOutput");
        pipeOutput.innerHTML = '';
        actualOutput = false;
        pipeOutput.classList.add('hidden');
    }
}
window.addEventListener('beforeunload', function (event) {
    if (actualOutput) {
        event.preventDefault();
        return (event.returnValue = "");
    }
});

/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */
/*  ---- Parameters ---- */
function parameterPopup() {
    popupWindow('Parameters');
    var setParametersForm = document.getElementById('setParametersForm');
    if (setParametersForm.childElementCount % 2 == 1) {
        setParametersForm.appendChild(document.createElement('div'))
    }
}
function parameterPopupClose() {
    document.getElementById('setParameters').reset();
    popupClose();
}
function setParameters(form) {
    var form = document.getElementById('setParameters');
    var theInputs = form.getElementsByTagName("input");
    var setParams = {};

    for (var i = 0; i < theInputs.length; i++) {
        if (theInputs[i].getAttribute("type") == "checkbox") {
            setParams[theInputs[i].name] = theInputs[i].checked;
        } else
            setParams[theInputs[i].name] = theInputs[i].value;
    }

    $.ajax({
        contentType: 'application/json',
        url: '/pipelines/get' + numPipe + '/params/',
        data: JSON.stringify({ setParams: setParams }),
        type: 'post',
        beforeSend: function () {
            text.textContent = 'Saving new data...';
        },
        success: function (ret) {
            if (ret.response) {
                text.textContent = 'Done, updating changes...';
                location.reload();
            } else {
                text.textContent = ret.err;
                parameterPopupClose();
            }
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            text.textContent = " Status: " + textStatus + "; Error: " + errorThrown;
        }
    });
};
