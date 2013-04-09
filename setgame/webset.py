from bottle import route, run, template, redirect, static_file, error
import random
import setgame

games={}

def draw(card):
	jcard={}
	jcard[color]=card.color
	jcard[number]=card.number
	jcard[shape]=card.shape
	jcard[fill]=card.fill
	return jcard

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
	return template('board', game=game, game_id=game_id, uid=uid, draw=draw)

@route("/play/<game_id:int>")
@route("/play/<game_id:int>/<uid:int>")
@route("/play/<game_id:int>/<uid:int>/<card_id:int>")
def play(game_id, uid=None, card_id=None):
	if game_id in games:
		game=games[game_id]
	else:
		redirect("/")
	if uid in game.players:
		player=game.players[uid]
		print "hand in player obj: " + repr(player.hand)
		if card_id != None:
			player.pickCard(card_id)
	else:
		uid=hash(random.random())
		player=setgame.Player(uid,"PlayerName")
		game.addPlayers(player)
	return template('board', game=game, game_id=game_id, uid=uid, draw=draw)

@route("/noset/<game_id:int>/<uid:int>")
def noset(game_id, uid):
	game=games[game_id]
	game.checkBoard()
	redirect("/play/" + str(game_id) + "/" + str(uid))

@route("/admin")
def admin():
	status={}
	status["games"]=games.keys()
	return status

@route("/static/<filepath:path>")
def static(filepath):
    return static_file(filepath, root="./static/")

def main():
	run(host='localhost', port=8080, debug=True, reloader=True)

if __name__ == '__main__':
	main()