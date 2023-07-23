/* Datas JS functions */
/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */
/*  ---- Initial settings ---- */
document.addEventListener('DOMContentLoaded', function () {
    // window.alert( sessionStorage.getItem("BlockLog"))
    modify = false;
    text = document.getElementById('errDataSection');

}, false);
/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */
/*  ---- Save Data settings ---- */
/*  ---- Modify column checkbox ---- */
function checkSaveColumn(element, num) {
    // window.alert(num)
    var section = document.getElementsByName('COL-' + num)
    // window.alert('got ' + element.checked + ' COL-' + num+'and size is '+section.length)
    if (element.checked) {
        for (var i = 0; i < section.length; i++)
            section[i].classList.remove('Darker');
    }
    else {
        for (var i = 0; i < section.length; i++)
            section[i].classList.add('Darker');
    }
    // window.alert( sessionStorage.getItem("BlockLog"))
}
/*  ---- Data operations ---- */
function saveDataLoaded() {
    var checkCols = [];
    var nameCols = []
    var allCheckCols = document.getElementsByName('checkCols');
    var allNameCols = document.getElementsByName('reNameCol[]');
    for (var i = 0; i < allCheckCols.length; i++) {
        if (allCheckCols[i].checked) {
            checkCols.push(i);
            nameCols.push(allNameCols[i].value);
        }
    }
    var newName = document.getElementById('newName').value.trim()
    $.ajax({
        contentType: 'application/json',
        url: '/datas/new/load',
        data: JSON.stringify({ theData: theData, newName: newName, checkCols: checkCols, nameCols: nameCols }),
        type: 'post',
        beforeSend: function () {
            text.textContent = 'Saving new data...';
        },
        success: function (ret) {
            if (ret.response) {
                text.textContent = 'Done, redirecting to new data ' + ret.numData + '...';
                window.location.replace("/datas/get" + ret.numData);
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
/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */
/*  ---- Data operations ---- */
function changeNameData() {
    newName = document.getElementById('newName').value.trim()
    // window.alert("Hey " + newName)
    if (newName != '' && newName != document.getElementById('theDataName').innerHTML.trim()) {
        $.ajax({
            data: JSON.stringify({ newName: newName }),
            contentType: 'application/json',
            url: '/operate/data/' + numData + '/name/',
            type: 'post',
            beforeSend: function () {
                text.textContent = 'Renaming data...';
            },
            success: function (ret) {
                if (ret.response) {
                    text.textContent = '';
                    document.getElementById('theDataName').textContent = newName
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
function saveDataFile(allFile, num) {
    $.ajax({
        contentType: 'application/json',
        url: '/download/data/'+num,
        type: 'post',
        beforeSend: function () {
            text.textContent = 'Saving new data...';
        },
        success: function (ret) {
            if (ret.response) {
                text.textContent = 'Done, save you data file';
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
