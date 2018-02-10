$(function () {
    var name_error = false;
    var pwd_error = false;

    if ({{ error_name }}==1){
        $('.user_error').html('用户名错误').show();
    }
    if ({{ error_pwd }}==1){
        $('.pwd_error').html('密码错误').show();
    }

    $('.name_input').blur(function () {
        check_user_name();
    });

    $('.pass_input').blur(function () {
        check_pwd();
    });

    function check_user_name() {
        if ($('.name_input').val().length == 0) {
            $('.user_error').html('请输入用户名').show();
            name_error = true;
        } else {
            $('.user_error').hide();
            name_error = false;
        }
    }

    function check_pwd() {
        if ($('.pass_input').val().length == 0) {
            $('.pwd_error').html('请输入密码').show();
            pwd_error = true;
        } else {
            $('.pass_input').hide();
            pwd_error = false;
        }
    }

    $('.form_input').submit(function () {
        check_user_name();
        check_pwd();

        if (name_error == false && pwd_error == false) {
            return true;
        } else {
            return false;
        }

    });
})