# -*- coding: utf-8 -*-
import os, datetime
import re

from flask import Flask, request, render_template, redirect, abort, jsonify
import requests

# Twilio

from twilio import twiml
from twilio.rest import TwilioRestClient
from twilio.util import TwilioCapability


# create Flask app
app = Flask(__name__)   # create our flask app


# --------- Routes ----------
@app.route('/')
def ghost_demo():
	# account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
	# auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
	# application_sid = os.environ.get('TWILIO_APP_SID')

	# capability = TwilioCapability(account_sid, auth_token)
	# capability.allow_client_outgoing(application_sid)
	# token = capability.generate()

	return render_template('index.html')


@app.route("/voice", methods=['GET', 'POST'])
def voice():

	# incoming call
	# PUSHER tells browser to show map

    response = twiml.Response()
    with response.gather(numDigits=1, action="/gather") as gather:
        gather.say("Welcome to Ghosts' Village. Press 1 to learn about the Shirtwaist Factory.")
    return str(response)

@app.route('/gather', methods=['GET','POST'])
def gather():

	response = twiml.Response()
	digits = request.form['Digits']
	
	if digits == "1":
		response.say("You are correct.  The Ramones are the best.")
		response.play("static/audio/01TriangleShirtwaistFire.mp3")
		app.logger.info("they pressed 1")
		#pusher broadcasts 1

	else:
		response.say("You are wrong.  Never call me again.")
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



	