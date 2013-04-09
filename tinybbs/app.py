import bottle
import pymongo
import os
from bottle import route, request, post, template

@route('/')
def index():
	try:
		connection = pymongo.MongoClient('localhost', 27017) # try get db connection
	except:
		return 'Sorry! We could not connect to the database'
	db = connection['test'] # get our test db
	bbs = db.bbs # get our bbs collection
	#message = bbs.find_one() #get a message
	docs = bbs.find() #get all the messages!
	return template('index', messages=docs) 

#@route('/postmsg', method='POST')
#fresh

@route('/postmsg')
#@post('/postmsg')
def postmsg():
#	account = request.forms.get('account')
#	message = request.forms.get('message')
	#get post data

#get 'get parameters'
	account = request.query.get('account')
	message = request.query.get('message')

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
	return template( login,)

@route('/users/<userid>')
def user( userid ):
	pass

@route("/static/<filepath:path>")
def static(filepath):
    return static_file(filepath, root="./static/")

def main():
	bottle.run(host='localhost', port=8080, debug=True, reloader=True)
	pass

if __name__ == '__main__':
	main()