import os
from flask import Flask, jsonify
from subprocess import call
app = Flask(__name__)

@app.route("/test")
def writeLine():
	data = open("testdata.json",'r')
	json = data.read()
	return json

@app.route('/music')
def playSong():
	call(["mkdir","New folder"])
	call(["mpc-hc","darkmatter.mp3"])
	return "Playing now..."


if __name__ == "__main__":
    app.run(host='192.168.1.216')