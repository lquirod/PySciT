// $('#header').height($(window).height() - $('#centralPage').height());
// document.getElementById("mydiv").setAttribute("style","display:block;cursor:pointer;cursor:hand;");
function toggleSection(section) {
    var section = document.getElementById(section);
    var text = document.getElementById('buttonSideLog');
    if (section.classList.contains('hidden')) {
        section.classList.remove('hidden');
        setTimeout(function () {
        section.classList.remove('visuallyHidden');
        }, 5);
        text.textContent='Log view (Shown)'
    } else {
        section.classList.add('visuallyHidden');    
        section.addEventListener('transitionend', function(e) {
        }, {
            capture: false,
            once: true,
            passive: false
        });
        section.classList.add('hidden');
        text.textContent='Log view (Hidden)'
    }
}