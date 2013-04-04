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
<link rel="stylesheet" type="text/css" href="style.css">
<div class=lobby>
%for i in games.keys():
	<div class=game>Join this game: <a href="/play/{{i}}">{{i}}</a></div>
%end

<div class=start><a href="/start">Start a new game</a></div>
</div>
</body>
</html>