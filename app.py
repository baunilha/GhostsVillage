# -*- coding: utf-8 -*-
import os, datetime
import re

from flask import Flask, request, render_template, redirect, abort, jsonify
import requests

# Pusher
import pusher # Pusher.com python library

# Twilio
from twilio import twiml
from twilio.rest import TwilioRestClient
from twilio.util import TwilioCapability


# create Flask app
app = Flask(__name__)   # create our flask app


# configure pusher 
pusher.app_id = os.environ.get('PUSHER_APP_ID')
pusher.key = os.environ.get('PUSHER_KEY')
pusher.secret = os.environ.get('PUSHER_SECRET')
p = pusher.Pusher()


# --------- Routes ----------
@app.route('/', methods=['GET', 'POST'])
def index():

	templateData = {
		'PUSHER_KEY' : os.environ.get('PUSHER_KEY')
	}

	return render_template('index.html', **templateData)


@app.route("/voice", methods=['GET', 'POST'])
def voice():

	# incoming call

    response = twiml.Response()

    if response:
        p['ghost_demo'].trigger('incoming_call',{'msg':'incoming'}) 


    with response.gather(numDigits=1, action="/gather", timeout=50) as g:
        g.say("Welcome to Ghosts' Village.  Press 1 to hear the story of the Shirtwaist Factory Fire.  Press 2 hear about the Fire Patrol Station Number 2.  Press 3 to learn about the Washignton Square Park as a burial ground.  Press 4 to hear the stories of the New York University Dormitory, Brittany Hall." )
        
    return str(response)


@app.route('/gather', methods=['GET','POST'])
def gather():

	response = twiml.Response()
	digits = request.form['Digits']
	
	if digits == "1":
		#twilio plays audio 1
		response.play("static/audio/factoryfire.mp3")
		app.logger.info("they pressed 1")

		#pusher broadcasts video 1
		p['ghost_demo'].trigger('incoming_digits',{'msg':str(digits)})
		

	if digits == "2":
		#twilio plays audio 2
		response.play("static/audio/firepatrolstation.mp3")
		app.logger.info("they pressed 2")

		#pusher broadcasts video 2
		p['ghost_demo'].trigger('incoming_digits',{'msg':str(digits)})

	if digits == "3":
		#twilio plays audio 3
		response.play("static/audio/washingtonsquarepark.mp3")
		app.logger.info("they pressed 3")

		#pusher broadcasts video 3
		p['ghost_demo'].trigger('incoming_digits',{'msg':str(digits)})

	if digits == "4":
		#twilio plays audio 4
		response.play("static/audio/brittanyhall.mp3")
		app.logger.info("they pressed 4")

		#pusher broadcasts video 4
		p['ghost_demo'].trigger('incoming_digits',{'msg':str(digits)})
		

	else:
        with response.gather(numDigits=1, action="/gather", timeout=50) as g:
        g.say("Welcome to Ghosts' Village.  Press 1 to hear the story of the Shirtwaist Factory Fire.  Press 2 hear about the Fire Patrol Station Number 2.  Press 3 to learn about the Washignton Square Park as a burial ground.  Press 4 to hear the stories of the New York University Dormitory, Brittany Hall." )
        
	return str(response)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


# --------- Server On ----------
# start the webserver
if __name__ == "__main__":
	app.debug = True
	
	port = int(os.environ.get('PORT', 5000)) # locally PORT 5000, Heroku will assign its own port
	app.run(host='0.0.0.0', port=port)



	