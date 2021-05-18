function copy(event) {
    const copyText = document.getElementById("copy-input");
  
    /* Select the text field */
    copyText.select();
    copyText.setSelectionRange(0, 99999); /* For mobile devices */
  
    /* Copy the text inside the text field */
    document.execCommand("copy");
  
    const tooltip = document.getElementById("copy-content");

    let element = event.target;
    while (element.tagName != 'BUTTON') {
        element = element.parentNode;
    }
    element.style.backgroundColor = "#f0b356";
    tooltip.innerHTML = "Copied to Clipboard";
}

function specificCopy(textToCopy, elementID) { 
    const el = document.createElement('textarea');
    el.value = textToCopy;
    document.body.appendChild(el);
    el.select();
    document.execCommand('copy');
    document.body.removeChild(el);

    const stringToChangeBackTo = document.getElementById(elementID).textContent;
    const elementToChange = document.getElementById(elementID);
    elementToChange.textContent = "Copied to Clipboard";
    setTimeout(() => { 
        document.getElementById(elementID).textContent = stringToChangeBackTo;
    }, 3000);
}


