from bottle import route, run, template, redirect
import random
import setgame

game=None
games={}

@route("/")
def lobby():
	global games
	return template('lobby', games=games)

@route("/start")
def startgame():
	global games
	game_id=hash(random.random())
	uid=hash(random.random())
	player=setgame.Player(uid,"PlayerName")
	game=setgame.Game(player)
	games[game_id]=game
	return template('board', game=game, game_id=game_id, uid=uid)

@route("/play/<game_id:int>")
@route("/play/<game_id:int>/<uid:int>")
@route("/play/<game_id:int>/<uid:int>/<card_id:int>")
def play(game_id, uid=None, card_id=None):
	game=games[game_id]
	if uid:
		player=game.players[uid]
		if card_id!=None:
			player.pickCard(card_id)
	else:
		uid=hash(random.random())
		player=setgame.Player(uid,"PlayerName")
		game.addPlayers(player)
	return template('board', game=game, game_id=game_id, uid=uid)

@route("/noset/<game_id:int>/<uid:int>")
def noset(game_id,uid):
	game=games[game_id]
	game.checkBoard()
	redirect("/play/" + str(game_id) + "/" + str(uid))

@route("/admin")
def admin():
	status={}
	status["games"]=games.keys()
	#for g in status["games"]:
	#	status["games"][g]["players"]=games[g].players
	#	status["games"][g]["deck"]=len(games[g].deck)
	return status

def main():
	run(host='localhost', port=8080, debug=True, reloader=True)
	pass

if __name__ == '__main__':
	main()