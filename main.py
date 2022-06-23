import json, random, words
from flask import *

app = Flask(__name__)

@app.route('/get/', methods=['GET'])
def get():
	return json.dumps({'Get': random.choice(words.targetWords)})

@app.route('/ask/', methods=['GET'])
def ask():
	word = str(request.args.get('word'))
	return json.dumps({'Ask': word in words.dictionary})

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=81)