function get_max_id(class_name){
	return document.getElementsByClassName(class_name).length
}

id = 1
max_id = get_max_id('steps');

$(function() {
	// ボタンクリック
	$('.btn').click(function(e) {
		// alert(id);
		main_id = id;
		main = document.getElementById(main_id).outerHTML;
		if(this.id == 'next'){
			id += 1;
		}else if(this.id == 'back'){
			id -= 1;
		}
		if(id > max_id){
			alert('this is last step');
			id = max_id;
		}else if(id < 1){
			alert('this is initial step');
			id = 1;
		}
		sub_id = id;
		sub = document.getElementById(sub_id).outerHTML;
	    document.getElementById(main_id).outerHTML = sub;

	    steps = document.getElementsByClassName("sub-div")[0].getElementsByClassName('steps')
	    for (var i = 0; i < steps.length; i++) {
	    	if(steps[i].id == sub_id){
	    		steps[i].outerHTML = main;
	    		break;
	    	}
	    }
		
	});
});

