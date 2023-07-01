/* Pipelines JS functions */
/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */
/*  ---- Initial settings ---- */
document.addEventListener('DOMContentLoaded', function () {
    // window.alert( sessionStorage.getItem("BlockLog"))
    modify = false;
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

function operateStep(operation, arg) {
    if (modify == true) {

    }
}
function operateStep(operation, arg) {
    // window.alert(operation+", "+arg)
    if (modify == true) {
        $.ajax({
            // data: { op: operation, arg: arg }, //, etiquetas: etiquetasCheck},
            data: JSON.stringify({ op: operation, arg: arg }), //, etiquetas: etiquetasCheck},
            
            contentType: 'application/json',
            url: '/operate/pipeline/'+numPipe+'/steps/',
            type: 'post',
            beforeSend: function () {
                toggleModify();
            },
            success: function (respuesta, msg) {
                toggleModify();
                if (respuesta) {
                }else{
                    var text = document.getElementById('errPipeSection');
                    text.textContent = msg;
                }
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                toggleModify();
                var text = document.getElementById('errPipeSection');
                text.textContent = " Status: " + textStatus + "; Error: " + errorThrown;
            }
        });
    }
}
