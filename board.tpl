<title>SetGame</title>
<div class=topbar>
<h3>Set Game</h3>
</div>
<div class=score>
<p>Score: {{game.players[uid].score}} pts</p>
</div>
<div class=board>
%for i, p in enumerate(game.positions):
	<div class=card>
	<a href="/play/{{game_id}}/{{uid}}/{{i}}">{{repr(p)}}</a>
	</div>
	<br>
%end
</div>
<div class=noset><a href="/noset/{{game_id}}/{{uid}}">no set</a></div>
<div class=positions>
%if game.players[uid].hand:
	<h2>Your Hand:</h2>
%for i, p in enumerate(game.players[uid].hand):
	<div class=card>{{repr(p)}}</div>
%end
</div>
