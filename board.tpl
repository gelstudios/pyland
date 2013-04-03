<title>SetGame</title>
<div class=topbar>
<h3>Set Game</h3>
</div>
<div class=score>
<p>Score: {{game.players[0].score}} pts</p>
</div>
<div class=board>
%for i, p in enumerate(game.positions):
	<div class=card>
	<a href="/play/{{game_id}}/{{str(i)}}">{{repr(p)}}</a>
	</div>
	<br>
%end
</div>
<div class=noset><a href="/noset/{{game_id}}">no set</a></div>
<div class=positions>
%if game.players[0].hand:
	<h2>Your Hand:</h2>
%for i, p in enumerate(game.players[0].hand):
	<div class=card>{{repr(p)}}</div>
%end
</div>
