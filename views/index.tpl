<!doctype html>
<html>
 <head>
 		<meta charset="utf-8">
    <!-- adding  script files -->
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.0/jquery.min.js"></script>

    <!-- adding  css files -->
    <!-- <link type="text/css" href="{{url('static_file', filepath='index.css')}}" rel="stylesheet"> -->

  </head>
  <body>
    <h1>CookpadのレシピURLを入力！</h1>

    <form method="POST" action="/recipe/making"> <!-- 要変更：決め打ちしている -->
      <p>URL: <input type="text" name="recipe_url"></p>
      <input type="submit" value="このレシピで作る！">
    </form>
  </body>

</html>
