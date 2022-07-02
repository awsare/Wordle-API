import random, words, time
from flask import *

app = Flask(__name__)

@app.route('/get/', methods=['GET'])
def get():
	return {
		'Call' : 'Get',
		'Status' : 200,
		'Response' : random.choice(words.targetWords),
		'Timestamp' : time.time()
	}, 200

@app.route('/ask/', methods=['GET'])
def ask():
	word = str(request.args.get('word'))
	
	if word == "None":
		return {
			'Call': 'Ask',
			'Status' : 400,
			'Details' : 'No word provided',
			'Timestamp' : time.time()
		}, 400
		
	if len(word) != 5:
		return {
			'Call': 'Ask',
			'Status' : 400,
			'Details' : 'Word must be five letters',
			'Timestamp' : time.time()
		}, 400
		
	return {
		'Call' : 'Ask',
		'Status' : 200,
		'Response' : word in words.dictionary,
		'Timestamp' : time.time()
	}, 200

@app.route('/daily/', methods=['GET'])
def daily():
	day = request.args.get('day')
	if not day:
		return {
			'Call': 'Daily',
			'Status' : 400,
			'Details' : 'No day provided',
			'Timestamp' : time.time()
		}, 400
	
	try:
		day = int(day)
	except ValueError:
		return {
			'Call': 'Daily',
			'Status' : 400,
			'Details' : 'Day must be an integer between 1 and ' + str(len(words.targetWords)),
			'Timestamp' : time.time()
		}, 400
		
	if (day <= 0 or day > len(words.targetWords)):
		return {
			'Call': 'Daily',
			'Status' : 400,
			'Details' : 'Day must be an integer between 1 and ' + str(len(words.targetWords)),
			'Timestamp' : time.time()
		}, 400
		
	return {
		'Call' : 'Daily',
		'Status' : 200,
		'Response' : words.targetWords[day - 1],
		'Timestamp' : time.time()
	}, 200

@app.errorhandler(404)
def notFound(error):
    return "Page not found", 404

if __name__ == '__main__':
	app.run()
