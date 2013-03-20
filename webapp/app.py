import bottle
import pymongo
import os
from bottle import route, request, get, post, template

#database names:
DBNAME = 'tinybbs'

#i think this needs db connection class? lots of repetition going on here

def db_init():
	try:
		connection = pymongo.MongoClient('localhost', 27017) # try get db connection
	except ConnectionFailure:
		print 'Sorry! We could not connect to the database %s', DBNAME
	try:
		connection['test'].db.bbs
	except:
		#create a collection called bbs in the database defined above
		print 'could not access bbs collection in %s', DBNAME
		pass
	pass


@route('/')
def index():
	try:
		connection = pymongo.MongoClient('localhost', 27017) # try get db connection
	except ConnectionFailure:
		return 'Sorry! We could not connect to the database'
	db = connection['test'] # get our test db
	bbs = db.bbs # get our bbs collection
	#message = bbs.find_one() #get a message
	docs = bbs.find() #get all the messages!
	print repr(docs)
	return template('index', messages=docs) 

@route('/postmsg')
#@post('/postmsg')
def postmsg():
#	account = request.forms.get('account')
#	message = request.forms.get('message')
	#get post data with request.forms.get
#get 'get parameters' with request.query.get
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
	return template('yay thanks for posting!') + bottle.redirect('/') #add bottle.redirect to root

@get('/login')
def login_page():
	return template('login',)

@route('/login', method='POST')
def auth_user():
	user = request.forms.get('u')
	passwd = request.forms.get('p')

@route('/users')
@route('/users/<userid>')
def user( userid=None ):
	if userid == None:
		return bottle.redirect('/')
	else:
		return 'hello ' + userid

def main():
	db_init()
	bottle.run(host='localhost', port=8080, debug=True, reloader=True)
	pass

if __name__ == '__main__':
	main()