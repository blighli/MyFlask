$(document).ready(function() {

	//------------- Login page simple functions -------------//
 	$("html").addClass("loginPage");

 	wrapper = $(".login-wrapper");
 	barBtn = $("#bar .btn");


	//check if user is change remove avatar
	var userField = $("input#user");



	//------------- Validation -------------//
	$("#login-form").validate({ 
		/*
                 * rules: {
			user: {
				required: true,
				minlength: 1
			}, 
			password: {
				required: true,
				minlength: 1
			}
		}, 
		messages: {
			user: {
				required: "Please provide a username",
				minlength: "Username must be at least 3 characters long"
			},
			password: {
				required: "Please provide a password",
				minlength: "Your password must be at least 5 characters long"
			}
		},
                */
		submitHandler: function(form){
	        var btn = $('#loginBtn');
	        btn.removeClass('btn-primary');
	        btn.addClass('btn-danger');
	        btn.text('Authenticating ...');
	        btn.attr('disabled', 'disabled');
	        setTimeout(function () {
	        	form.submit();
	        }, 100);
		}
		/*,
		submitHandler: function(form){
	        var btn = $('#loginBtn');
	        btn.removeClass('btn-primary');
	        btn.addClass('btn-danger');
	        btn.text('Authenticating ...');
	        btn.attr('disabled', 'disabled');
	        setTimeout(function() {
	        	btn.removeClass('btn-danger');
	        	btn.addClass('btn-success');
	        	btn.text('User find ...');
	        }, 500);
	        setTimeout(function () {
	        	form.submit();
	        }, 1000);
		}
		*/
	});

});