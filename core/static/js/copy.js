function copy(event) {
    var target = event.target || event.srcElement;
    var copyText = target.parentElement.parentElement.parentElement.parentElement.children[0];
    copyText.select();
    copyText.setSelectionRange(0, 99999);
    document.execCommand("copy");

    var tooltip = target.parentElement.parentElement.children[1];
    tooltip.innerHTML = "Copied"
  }