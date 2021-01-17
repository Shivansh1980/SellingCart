import $ from 'jquery'

function addSpansToText(classname) {
    var dot = "."
    classname = dot + classname
    console.log(classname)
    var textParent = document.querySelector(classname);
    var text = String(textParent.innerText);
    $(classname).html('');
    
    for (var i = 1; i <= text.length; i++){
        var spanElement = document.createElement('span');
        spanElement.setAttribute('id', String(i));
        spanElement.innerText = text[i-1];
        textParent.appendChild(spanElement);
    }
    return text.length;
}

function animateText(classname) {
    var sizeOfText = addSpansToText(classname);
    for (var i = 1; i <= sizeOfText; i++){
        var id = "#" + String(i)
        $(id).css({
            'font-size': '30px',
            'animation': 'bounce',
            'animation-duration': '4s',
            'color':'red'
        });
    }

}
export {animateText, addSpansToText}