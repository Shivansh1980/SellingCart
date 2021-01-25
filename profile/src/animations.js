import $ from 'jquery'
var isAlpha = function (ch) {
    return /^[A-Z]$/i.test(ch);
}
function addSpansToText(classname) {
    var realClassName = classname
    //now we add . to make it selector
    var dot = "."
    classname = dot + classname
    //use the selector here
    var textParent = document.querySelector(classname);
    var text = String(textParent.innerText);
    $(classname).html('');
    
    for (var i = 1; i <= text.length; i++){
        if (text[i-1] == ' ') {
            textParent.append(" ");
            continue;
        }
        var spanElement = document.createElement('span');
        var id = realClassName + String(i);
        spanElement.setAttribute('id', id);
        spanElement.innerText = text[i - 1];
        textParent.appendChild(spanElement);
    }
    return text;
}

function animateText(classname, animationName = "bounce",animationTime=2, colorValue = 5, changeColor = false) {
    var text = addSpansToText(classname);
    console.log(text)
    var sizeOfText = text.length;
    var calcTime = animationTime / sizeOfText;
    var temp = 0;
    for (var i = 1; i <= sizeOfText; i++){
        if (text[i-1] != ' ') {
            var id = "#" + classname + String(i);
            if (changeColor) {
                $(id).css({
                    'color': `rgba(${colorValue + 10 * i},${colorValue + 20 * i},250)`
                })
            }
            $(id).css({
                'animation': animationName,
                'animation-duration': String(temp) + "s",
                'animation-timing-function': 'linear',
            })
            temp += calcTime
        }
    }
}

function addHtmlToClass(classname, html) {
    classname = "." + classname;
    $(classname).html(html)
}
function getPositionById(id) {
    id = "#" + id;
    alert($(id).position());
    return $(id).position();
}
export { animateText, addSpansToText, addHtmlToClass}