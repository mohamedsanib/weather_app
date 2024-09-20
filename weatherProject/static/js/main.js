let searchImg = document.querySelector('#search_img');
searchImg.addEventListener('click', ()=>{
    let searchBox = document.querySelector('.search_box');
    let style = window.getComputedStyle(searchBox).getPropertyValue('visibility');
    if(style === 'hidden'){
        searchBox.style.visibility = 'visible';
        searchBox.style.opacity = '1';

    }else{
        searchBox.style.visibility = 'hidden';
        searchBox.style.opacity = '0';
    }
})