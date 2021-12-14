//this will create a local store on user's browser if it doesn't exists
if(!localStorage.getItem('counter')){
    localStorage.setItem('counter', 0);
}

function count(){
    let counter = localStorage.getItem('counter');
    counter ++;
    document.querySelector('h1').innerHTML = counter;
    localStorage.setItem('counter', counter);
}
//driver code
document.addEventListener('DOMContentLoaded', function(){
        document.querySelector('button').onclick = count;
        document.querySelector('h1').innerHTML = localStorage.getItem('counter');
    });