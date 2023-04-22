$(document).ready(function() {
    // check if username is available
    $('#username').on('change keyup blur', function() {
        var username = $(this).val();
        $.ajax({
            url: '/api2/accounts/',
            type: 'GET',
            data: {username: username},
            success: function(response) {
                var taken = false;
                $.each(response, function(index, user) {
                    if (user.username === username) {
                        taken = true;
                        return false; // exit the loop
                    }
                });
                if (taken) {
                    $('#error').text('Username already taken.');
                    $('#registerbtn').prop('disabled', true);
                } else {
                    $('#error').text('');
                    $('#registerbtn').prop('disabled', false);
                }
            }
        });
    });
    // check if email is available
    $('#email').on('change keyup blur', function() {
        var email = $(this).val();
        $.ajax({
            url: '/api2/accounts/',
            type: 'GET',
            data: {email: email},
            success: function(response) {
                var taken = false;
                $.each(response, function(index, user) {
                    if (user.email === email) {
                        taken = true;
                        return false; // exit the loop
                    }
                });
                if (taken) {
                    $('#error').text('Username already taken.');
                    $('#registerbtn').prop('disabled', true);
                } else {
                    $('#error').text('');
                    $('#registerbtn').prop('disabled', false);
                }
            }
        });
    });

});