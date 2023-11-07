/* Base JS functions */
/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */
/*  ---- Log settings ---- */
/*  ---- Initial check ---- */
document.addEventListener('DOMContentLoaded', function () {
    if (sessionStorage.getItem("BlockLog")) {
        toggleLogSection()
        document.getElementById('checkLog').checked = true;
    }
}, false);
/*  ---- Log block check toggle ---- */
function checkBlock(element) {
    if (element.checked) {
        sessionStorage.setItem("BlockLog", true);
    }
    else {
        sessionStorage.removeItem('BlockLog');
    }
}
/*  ---- Log toggle button ---- */
function toggleLogSection() {
    var section = document.getElementById('SideLog');
    var text = document.getElementById('buttonSideLog');
    if (section.classList.contains('hidden')) {
        section.classList.remove('hidden');
        section.classList.remove('visuallyHidden');
        text.textContent = 'Log view (Shown)';
    } else {
        section.classList.add('visuallyHidden');
        section.classList.add('hidden');
        text.textContent = 'Log view (Hidden)';
        document.getElementById('checkLog').checked = false;
        sessionStorage.setItem("BlockLog", false);
    }
}
/*  ---- Add log ---- */
function addViewLog(text = null) {
    if (text != '' || text != null) {
        var theLog = document.getElementById('LogView');
        var addlog = document.createElement('p');
        var timelog = document.createElement('span');
        timelog.classList.add('boldText');
        timelog.innerHTML = text[0]
        addlog.appendChild(timelog);

        var br = document.createElement("br");
        addlog.appendChild(br.cloneNode(true));

        var ptext = document.createTextNode(text[1]);
        addlog.appendChild(ptext);

        theLog.insertBefore(addlog, theLog.firstChild);
    }
}
