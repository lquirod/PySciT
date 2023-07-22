/* Popup JS functions */
/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */
/*  ---- Popup settings ---- */
document.addEventListener('DOMContentLoaded', function () {
    popupBase = document.getElementById("popUpBaseDiv");
    actualPopup = null
}, false);

function popupWindow(item) {
    if (actualPopup == null) {
        actualPopup = document.getElementById(item);
        popupBase.style.display = "table-cell";
        actualPopup.style.display = "inline-block";
    }
}

function popupClose() {
    if (actualPopup != null) {
        popupBase.style.display = "none";
        actualPopup.style.display = "none";
        actualPopup = null
    }
}