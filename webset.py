from bottle import route, run, template, redirect
import setgame

game=None
game_id=9999

@route("/")
def startgame():
	global game
	game=setgame.Game(setgame.Player(7890987, "Eric"))
	return template('board', game=game, game_id=game_id)

@route("/play/<game_id:int>")
@route("/play/<game_id:int>/<card_id:int>")
def play(game_id, card_id=None):
	if card_id:
		game.players[0].pickCard(card_id)
	return template('board', game=game, game_id=game_id)

@route("/noset/<game_id:int>")
def noset(game_id):
	game.checkBoard()
	redirect("/play/" + str(game_id))

def main():
	run(host='localhost', port=8080, debug=True, reloader=True)
	pass

if __name__ == '__main__':
	main()