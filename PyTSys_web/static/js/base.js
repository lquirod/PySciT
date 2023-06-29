/* Base JS functions */
/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */
/*  ---- Log settings ---- */
/*  ---- Log block check ---- */
document.addEventListener('DOMContentLoaded', function () {
    // window.alert( sessionStorage.getItem("BlockLog"))
    if (sessionStorage.getItem("BlockLog")) {
        // window.alert("A true!!")
        toggleSection('SideLog')
        document.getElementById('checkLog').checked = true;
    }
}, false);

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
function toggleSection(section) {
    var section = document.getElementById(section);
    var text = document.getElementById('buttonSideLog');
    if (section.classList.contains('hidden')) {
        section.classList.remove('hidden');
        setTimeout(function () {
            section.classList.remove('visuallyHidden');
        }, 5);
        text.textContent = 'Log view (Shown)'
    } else {
        section.classList.add('visuallyHidden');
        section.addEventListener('transitionend', function (e) {
        }, {
            capture: false,
            once: true,
            passive: false
        });
        section.classList.add('hidden');
        text.textContent = 'Log view (Hidden)'
    }
}