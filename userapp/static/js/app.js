

function validation(e) {
    e.preventDefault();
    var password = document.getElementById('password').value;
    var confirmPassword = document.getElementById('confirmPassword').value;
    if (password != confirmPassword) {
        document.getElementById('passError').innerHTML = 'Password do not match';
    }
}