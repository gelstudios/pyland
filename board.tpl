<!DOCTYPE html>
<html>
<head>
<title>SetGame</title>
<link rel="stylesheet" type="text/css" href="static/style.css">
</head>

<body>

<div class=topbar>
<h3>Set Game</h3>
</div>

<div class=score>
<p>Your Score: {{game.players[uid].score}} pts</p>
</div>

<div class=board>
%for i, p in enumerate(game.positions):
	<div class=card>
	<a href="/play/{{game_id}}/{{uid}}/{{i}}">
		<span class=number>{{p.number}}</span> {{p.color}} :: {{p.shape}} :: {{p.fill}} ::
	</a>
	</div>
%end
</div>

<div class=noset><p><a href="/noset/{{game_id}}/{{uid}}">no set</a></p></div>

<div class=hand>
%print "hand in template: " + repr(game.players[uid].hand)
	<p>Your Hand:</p>
%for i, p in enumerate(game.players[uid].hand):
	<div class=card>{{repr(p)}}</div>
%end
</div>

<div class=scoreboard>
<p>Players:</p>
%for i in game.players.keys():
	%j=game.players[i]
	<div class=player><p>Name: {{j.name}} ({{j.uid}}) Score: {{j.score}} pts</p></div>
%end
</div>

</body>
</html>
