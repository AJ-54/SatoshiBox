let file = document.getElementById('file');
file.addEventListener('change', function(e) {
    let val = "";
    let size = 0;
    let limit_exceeded=false;
    for(var i=0; i< e.target.files.length; i++){
        val += e.target.files[i].name;
        size += e.target.files[i].size;
        val += ", ";
    }
    val = val.slice(0,-2);
    size/=1000000;
    if(size>5){
      file.setCustomValidity('Total size exceeds 5mb');
      file.reportValidity();
    }
    else{
      file.setCustomValidity('');
    }
    document.getElementById('value').innerHTML = "Selected " + val;
    document.getElementById('size').innerHTML = "Total size: " + size + ' MB';
});
