/* Base JS functions */
/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */
/*  ---- Log settings ---- */
/*  ---- Log block check ---- */
document.addEventListener('DOMContentLoaded', function () {
    // window.alert( sessionStorage.getItem("BlockLog"))
    if (sessionStorage.getItem("BlockLog")) {
        // window.alert("A true!!")
        toggleLogSection()
        document.getElementById('checkLog').checked = true;
    }
}, false);
/*  ---- Log block check toggle ---- */
function checkBlock(element) {
    // window.alert(element.checked)
    if (element.checked) {
        sessionStorage.setItem("BlockLog", true);
        // window.alert("Cambiado a true")
    }
    else {
        // sessionStorage.setItem("BlockLog", false);
        sessionStorage.removeItem('BlockLog');
        // window.alert("Cambiado a false")
    }
    // window.alert( sessionStorage.getItem("BlockLog"))
}
/*  ---- Log toggle button ---- */
function toggleLogSection() {
    var section = document.getElementById('SideLog');
    var text = document.getElementById('buttonSideLog');
    if (section.classList.contains('hidden')) {
        section.classList.remove('hidden');
        setTimeout(function () {
            section.classList.remove('visuallyHidden');
        }, 5);
        text.textContent = 'Log view (Shown)';
    } else {
        section.classList.add('visuallyHidden');
        section.addEventListener('transitionend', function (e) {
        }, {
            capture: false,
            once: true,
            passive: false
        });
        section.classList.add('hidden');
        text.textContent = 'Log view (Hidden)';
        sessionStorage.setItem("BlockLog", false);
    }
}
/*  ---- Add log ---- */
function addViewLog(text = null) {
    if (text != '' || text != null) {
        var theLog = document.getElementById('LogView');
        var addlog = document.createElement('p');
        addlog.innerHTML = text[0]+text[1];
        // window.alert(text)
        theLog.appendChild(addlog);
    }
}

