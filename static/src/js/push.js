odoo.define('pragmatic_push_notifications.push_notification', function(require){
	function set_onesignal_active_app(app_id){
		var OneSignal = window.OneSignal || [];
		  OneSignal.push(function() {
		    OneSignal.init({
		      appId: app_id,
		      autoRegister: false,
		      notifyButton: {
		        enable: true,
		      },
		    });
		  });
	}
	$.ajax({
		url : '/check_active_app',
		async: false,
		type : 'GET'
	}).done(function(response){
		if(response != '0'){
			set_onesignal_active_app(response)
		}
	});
});//odoo define