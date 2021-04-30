// const download_btn = document.querySelector("download__btn");

// const download_files=()=>{
     
//     const url = window.URL.createObjectURL(blob);
//     const a = document.createElement('a');
//     a.style.display = 'none';
//     a.href = url;
//     // the filename you want
//     a.download = 'todo-1.json';
//     document.body.appendChild(a);
//     a.click();
//     window.URL.revokeObjectURL(url);
    
//     alert('your files have been downloaded downloaded!'); // or you know, something with better UX...
// }


// const fetchFiles=()=>{
     
//     (async()=>{
//         try{
//         const response = await fetch(url);
//         const data= await response.json();
//         }catch(err){
//             alert('oh no!')
//         };
//     })();
// }




// download_btn.addEventListener("click",fetchFiles)