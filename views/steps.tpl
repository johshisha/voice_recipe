<!doctype html>
<html>
 <head>
 		<meta charset="utf-8">
    <!-- adding  script files -->
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.0/jquery.min.js"></script>

    <!-- adding  css files -->
    <link type="text/css" href="{{url('static_file', filepath='steps.css')}}" rel="stylesheet">

  </head>
  <body>
    <div class="body">
      %i=0
      <div class="main-div">
        <div class="main-content">
        	<div class="steps" id="{{ i+1 }}">
            %step = steps[i]
	          %if step['image']:
              <img class="step-img" src="{{ step['image'] }}" alt="img">
            %end
            <p class="step-text">{{ step['text'] }}</p>
          </div>
        </div>
      </div>
      <div class="sub-div">
        %for i in range(1, len(steps)):
          %step = steps[i]
          <div class="steps" id="{{ i+1 }}">
            %if step['image']:
              <img class="step-img" src="{{ step['image'] }}" alt="img">
            %end
            <p class="step-text">{{ step['text'] }}</p>
          </div>
        %end
      </div>
    </div>
<!--     <button class="btn" id="back">前！！</button>
    <button class="btn" id="next">次！！</button> -->
    <button onclick="vr_stop();"><a  id="stop_btn">認識終了</a></button> 
    <p>{{recipe_url}}</p>
  </body>

  <!-- load js -->
  <script src="{{url('static_file', filepath='steps.js')}}"></script>

  <script>
    // start recognition
    console.log('start recognition');
    vr_function();
  </script>
</html>
