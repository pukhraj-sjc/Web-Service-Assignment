#!/usr/bin/python

# Modules
import requests
import json
import re
from flask import Flask

app = Flask(__name__)

@app.route("/")
def combine_replace():
	fetch_name = requests.get('https://api.namefake.com/')
	name = str(json.loads(fetch_name.text)['name'])
	fetch_joke = requests.get('http://api.icndb.com/jokes/random?firstName=John&lastName=Doe&limitTo=[nerdy]')
	joke = str(json.loads(fetch_joke.text)['value']['joke'])
	return re.sub("John Doe's|John Doe",name,joke)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
