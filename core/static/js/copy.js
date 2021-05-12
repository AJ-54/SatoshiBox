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