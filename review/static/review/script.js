// JavaScript source code

//creates a flip-card for each concept and appends it to the .middle section of the index html
//removed from use as it did not work with s3
function appendConcept(question, key) {
    var card = document.createElement("div");
    card.setAttribute("class", "flip-card");
    var cardInner = document.createElement("div");
    cardInner.setAttribute("class", "flip-card-inner");
    var cardFront = document.createElement("div");
    cardFront.setAttribute("class", "flip-card-front");
    var content = document.createElement("img");
    content.setAttribute("class", "content");
    content.setAttribute("src", question);
    cardFront.appendChild(content);
    cardInner.appendChild(cardFront);
    var cardBack = document.createElement("div");
    cardBack.setAttribute("class", "flip-card-back");
    var answer = document.createElement("img");
    answer.setAttribute("class", "answer");
    answer.setAttribute("src", key);
    cardBack.appendChild(answer);
    cardInner.appendChild(cardBack);
    card.appendChild(cardInner);
    document.getElementById("review").appendChild(card);
}

/*adds the links for old content to the drop-menu*/
//removed from use as it did not work with s3
function appendLink(conceptName, question, answer) {
    var link = document.createElement("a");
    node = document.createTextNode(conceptName);
    link.addEventListener("click", showSelectedConcept.bind(null, question, answer));
    link.setAttribute("class", "review-links")
    link.appendChild(node);
    document.getElementById("drop-menu").appendChild(link);
}

/*sets the image on the selected question overlay and causes the overlay to display */
function showSelectedConcept(question, answer) {
    document.getElementById("selected-question").setAttribute("src", question);
    document.getElementById("selected-key").setAttribute("src", answer);
    window['selected-concept-wrapper'].style.display = "grid";
} 

function hideSelectedConcept() {
    window['selected-concept-wrapper'].style.display = "none";
}

/* toggles the drop-menu on and off */
function openMenu() {
    if (window['drop-menu'].style.display == "none") {
        window['drop-menu'].style.display = "flex";
        window['topic-menu'].setAttribute("class", "open")
    } else {
        window['drop-menu'].style.display = "none";
        window['topic-menu'].setAttribute("class", "closed")
    }
}

/*closes the drop-menu if a click is registered anywhere except the menu*/
function closeMenu(elementId) {
    if (elementId != 'drop-menu') {
        window['drop-menu'].style.display = "none";
        window['topic-menu'].setAttribute("class", "closed")
    }
}
