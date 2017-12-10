function sendcom(){
    var token = document.getElementsByName('csrfmiddlewaretoken')[0].value;    

    var name = document.getElementById('name').value;
    var position = document.getElementById('position').value;
    var state = document.getElementById('state').value;
    var institution = document.getElementById('institution').value;
    var email = document.getElementById('email').value;
    var phone = document.getElementById('phone').value;
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    openModal();
    jQuery.ajax({
	type: "POST",
	async: true,
	url: '/freepreview/submit/',
	data: {'csrfmiddlewaretoken': token, 'name': name, 'position': position, 'state': state, 'institution': institution, 'email': email, 'phone': phone, 'username': username, 'password': password},
	
	success: function(msg)
	{
		$('body').replaceWith(msg);
	},
	error: function(err)
	{
		alert(err.responseText);
	}
    });
}

function openModal() {
        document.getElementById('modal').style.display = 'block';
        document.getElementById('fade').style.display = 'block';
}

function closeModal() {
    document.getElementById('modal').style.display = 'none';
    document.getElementById('fade').style.display = 'none';
}
