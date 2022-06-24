import json, random, words, time
from flask import *

app = Flask(__name__)

@app.route('/get/', methods=['GET'])
def get():
	return json.dumps({'Call' : 'Get', 'Status' : 200, 'Response' : random.choice(words.targetWords), 'Timestamp' : time.time()})

@app.route('/ask/', methods=['GET'])
def ask():
	word = str(request.args.get('word'))
	if word != "None":
		return json.dumps({'Call' : 'Ask', 'Status' : 200, 'Response': word in words.dictionary, 'Timestamp' : time.time()})
	return json.dumps({'Call': 'Ask', 'Status' : 400, 'Details' : 'No word provided', 'Timestamp' : time.time()})

@app.route('/daily/', methods=['GET'])
def daily():
	day = request.args.get('day')
	if day:
		day = int(day)
		if (day > 0 and day < len(words.targetWords)):
			return json.dumps({'Call' : 'Daily', 'Status' : 200, 'Response': words.targetWords[day - 1], 'Timestamp' : time.time()})
		return json.dumps({'Call': 'Daily', 'Status' : 400, 'Details' : 'Day must be between 1 and ' + str(len(words.targetWords)), 'Timestamp' : time.time()})
	return json.dumps({'Call': 'Daily', 'Status' : 400, 'Details' : 'No day provided', 'Timestamp' : time.time()})

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=81)