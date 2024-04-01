const account_button = document.getElementsByClassName('cu-account-button')[0];
const user_type_list = document.getElementById('id_user_type');

account_button.addEventListener('click', function () {
    if (user_type_list.style.display === 'none' ||  user_type_list.style.display === '') {
        user_type_list.style.display = 'block';
    }
    else {
        user_type_list.style.display = 'none';
    }
})
