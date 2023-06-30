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
    var mov = document.getElementById('movStep');
    var del = document.getElementById('delStep');
    var buttonModify = document.getElementById('toggleModify');
    if (mov.classList.contains('Darker')) {
        mov.classList.remove('Darker');
        del.classList.remove('Darker');
        buttonModify.value = 'Modify enabled';
        modify = true;
    } else {
        mov.classList.add('Darker');
        del.classList.add('Darker');
        buttonModify.value = 'Modify disabled';
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
    if (modify == true) {
        $.ajax({
            data: { operation: operation, arg: arg }, //, etiquetas: etiquetasCheck},
            url: 'BD/getProductosBusqueda.php',
            type: 'post',
            beforeSend: function () {
                toggleModify();
            },
            success: function (respuesta) {
                toggleModify();
                if (respuesta != true) {
                    var text = document.getElementById('errPipeSection');
                    text.textContent = respuesta;
                }
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                toggleModify();
                var text = document.getElementById('errPipeSection');
                text.textContent = " Status: " + textStatus + "<br>Error: " + errorThrown;
            }
        });
    }
}
