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
      <div class="main-div">
        <div class="main-content">
        	<div class="steps" id="1">
	          <img class="step-img" src="{{url('static_file', filepath='images/1.jpg')}}" alt="img">
	          <p class="step-text">text1</p>
          </div>
        </div>
      </div>
      <div class="sub-div">
        <div class="steps" id="2">
          <img class="step-img" src="{{url('static_file', filepath='images/2.jpg')}}" alt="img">
          <p class="step-text">text2</p>
        </div>
        <div class="steps" id="3">
          <img class="step-img" src="{{url('static_file', filepath='images/3.jpg')}}" alt="img">
          <p class="step-text">text3</p>
        </div>
        <div class="steps" id="4">
          <img class="step-img" src="{{url('static_file', filepath='images/4.jpg')}}" alt="img">
          <p class="step-text">text4</p>
        </div>
        <div class="steps" id="5">
          <img class="step-img" src="{{url('static_file', filepath='images/5.jpg')}}" alt="img">
          <p class="step-text">text5</p>
        </div>
        <div class="steps" id="6">
          <img class="step-img" src="{{url('static_file', filepath='images/6.jpg')}}" alt="img">
          <p class="step-text">text6</p>
        </div>
      </div>
    </div>
    <button class="btn" id="back">前！！</button>
    <button class="btn" id="next">次！！</button>
    <p>{{recipe_url}}</p>
  </body>

  <!-- load js -->
  <script src="{{url('static_file', filepath='steps.js')}}"></script>
</html>