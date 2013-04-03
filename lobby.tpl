<title>SetGame</title>
<div class=topbar>
<h3>Set Games:</h3>
</div>
<div class=lobby>
%for i in games.keys():
	<div class=game>Join this game: <a href="/play/{{i}}">{{i}}</a></div>
%end

<div class=start><a href="/start">Start a new game</a></div>
</div>