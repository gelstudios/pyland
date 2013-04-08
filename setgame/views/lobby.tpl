<!DOCTYPE html>
<html>
<head>
<title>SetGame</title>
<link rel="stylesheet" type="text/css" href="static/style.css">
</head>

<body>

<div class=topbar>
<h3>Set Games:</h3>
</div>

<div class=lobby>
%for i in games.keys():
	<div class=game>game:{{i}} players: ### <a class=button href="/play/{{i}}">Join</a></div>
%end
</div>

<div class=start><a href="/start">Start a new game</a></div>

</body>
</html>