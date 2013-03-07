import bottle
import pymongo
import os
from bottle import route, request, post

@route('/')
def index():
	try:
		connection = pymongo.MongoClient('localhost', 27017) # try get db connection
	except ConnectionFailure:
		return 'Sorry! We could not connect to the database'
	db = connection['test'] # get our test db
	bbs = db.bbs # get our bbs colleWe ction
	#message = bbs.find_one() #get a message
	messages = bbs.find() #get all the messages!
	content = []
	for message in messages:
		content.append( '<b>poster: %s</b>' % message.get('account','Anon') + '<br>' + '<b>status: %s</b>' % message.get('status','new') + '<br>' + '<b>message: %s</b>' % message.get('msg', '...') + '<br><br>' )
	return content + ['<br><form action="/postmsg" method="post"> Account: <input type="text" name="account"><br>Message: <input type="text" name="message"><br><input type="submit" formmethod="post" formaction="/postmsg" value="post my message"></form>']

#@route('/postmsg', method='POST')
@post
def postmsg():
	account = request.forms.get('account')
	message = request.forms.get('message')
	#get post data
	post_data = {'account':account,'msg':message, 'status':'new'}
	try:
		connection = pymongo.MongoClient('localhost', 27017) # try get db connection
	except:
		return 'Sorry! We could not connect to the database'
	db = connection['test'] # get our test db
	bbs = db.bbs # get our bbs colleWe ction
	bbs.save(post_data)
	return 'yay thanks for posting!' #post_data

@route('/users')
@route('/users/')
def login():
	body = 'this is some txt, pretend you see a fake login page'
	return t2html( body, 'body')

@route('/users/<userid>')
def user( userid ):
	if userid == None:
		return 'this is the a fancy login page'
	else:
		return t2html( 'hello ' + userid, 'body') + t2html('/message', 'link')

def t2html( text, tag ):
	if tag == 'link':
		return '<a href="' + text + '">' + text + '</a>'
	else:
		return '<' + tag + '>' + text + '</' + tag + '>'

def main():
	bottle.run(host='localhost', port=8080, debug=True, reloader=True)
	pass

if __name__ == '__main__':
	main()