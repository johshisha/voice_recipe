function get_max_id(class_name){
	return document.getElementsByClassName(class_name).length
}

id = 1
max_id = get_max_id('steps');
stop_flag = false;



// change html element
function change_steps(order){
	// alert(id);
	main_id = id;
	main = document.getElementById(main_id).outerHTML;
	if(order == 'next'){
		id += 1;
	}else if(order == 'back'){
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
}

// recognize input voice using web_speech_api
function vr_function() {
    window.SpeechRecognition = window.SpeechRecognition || webkitSpeechRecognition;
    var recognition = new webkitSpeechRecognition();
    recognition.lang = 'ja';

    // restart recognize if recognition stopped
    recognition.onerror = function() {
    	// console.log('onerror');
    	if (stop_flag == true){
    		return 0;
    	}
    	vr_function();
    };
    recognition.onsoundend = function() {
    	// console.log('onsoundend');
    	if (stop_flag == true){
    		return 0;
    	}
        vr_function();
    };

    // get result of recognition
    recognition.onresult = function(event){
        var results = event.results;
        for (var i = event.resultIndex; i<results.length; i++){
        	var input = results[i][0].transcript
            console.log(input + '\n');

            // if result included 'keyword', call change step function
            if (input.match(/次/)){
                console.log('inputed next');
                change_steps('next');
            }else if(input.match(/戻/)){
            	console.log('inputed back');
                change_steps('back');
            }
        }
            
    };
    recognition.start();
}

function vr_stop(){
	if (stop_flag == false){
		stop_flag = true;
		alert('認識終了しました');
		document.getElementById('stop_btn').text = '認識再開';
	}else{
		stop_flag = false;
		alert('認識再開しました');
		document.getElementById('stop_btn').text = '認識終了';
		vr_function();
	}

}


