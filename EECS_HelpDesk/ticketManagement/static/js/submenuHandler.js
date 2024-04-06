function submenuHandler (event){
    let submenuStatus = event.target.nextElementSibling.style.display

    if(submenuStatus === 'flex'){
        event.target.nextElementSibling.style.display = 'none'
    }

    else{
        event.target.nextElementSibling.style.display = 'flex'
    }
}