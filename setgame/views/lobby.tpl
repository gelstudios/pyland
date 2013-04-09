<!DOCTYPE html>
<html>
<head>
<title>SetGame</title>
%#<link rel="stylesheet" type="text/css" href="static/style.css">
<link href="/static/bootstrap/css/bootstrap.min.css" rel="stylesheet" media="screen">
</head>


<body>
<script src="http://code.jquery.com/jquery.js"></script>

<div class="navbar navbar-inverse navbar-fixed-top">
<h3>Set Games:</h3>
</div>

<div class="container">
<div class=lobby>
%for i in games.keys():
	<div class=game>game:{{i}} players: ### <a class=button href="/play/{{i}}">Join</a></div>
%end
</div>

<div class=start><a href="/start">Start a new game</a></div>

</div>
</body>
</html>