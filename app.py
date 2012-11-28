# -*- coding: utf-8 -*-
import os, datetime
import re
from unidecode import unidecode

from flask import Flask, request, render_template, redirect, abort, jsonify
import requests

# Twilio
from twilio.rest import TwilioRestClient
import twilio.twiml

# create Flask app
app = Flask(__name__)   # create our flask app


# --------- Routes ----------
@app.route('/', methods=['GET'])
def ghost_demo():
	
	account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

    # This is a special Quickstart application sid - or configure your own
    # at twilio.com/user/account/apps
    application_sid = os.environ.get('TWILIO_APP_SID')

    capability = TwilioCapability(account_sid, auth_token)
    capability.allow_client_outgoing(application_sid)
    token = capability.generate()

	return render_template('index.html', token=token)


@app.route("/voice", methods=['GET', 'POST'])
def voice():
    """Respond to incoming requests."""
    resp = twilio.twiml.Response()
    resp.say("Hello Monkey")
 
    return str(resp)


@app.route('/twilio', methods=['GET','POST'])
def twilio():
	
	if request.method == "GET":
		return render_template('twilio.html')

	elif request.method == "POST":

		telephone = request.form.get('telephone')
		sms_text = request.form.get('sms_text')

		# prepare telephone number. regex, only numbers
		telephone_num = re.sub("\D", "", telephone)
		if len(telephone_num) != 11:
			return "your target phone number must be 11 digits. go back and try again."
		else:
			to_number = "+" + str(telephone_num) #US country only now


		# trim message to 120
		if len(sms_text) > 120:
			sms_text = sms_text[0:119]

		account = os.environ.get('TWILIO_ACCOUNT_SID')
		token = os.environ.get('TWILIO_AUTH_TOKEN')

		client = TwilioRestClient(account, token)

		from_telephone = os.environ.get('TWILIO_PHONE_NUMBER') # format +19171234567

		message = client.sms.messages.create(to=to_number, from_=from_telephone,
	                                     body="DWD DEMO: " + sms_text)

		return "message '%s' sent" % sms_text

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


# --------- Server On ----------
# start the webserver
if __name__ == "__main__":
	app.debug = True
	
	port = int(os.environ.get('PORT', 5000)) # locally PORT 5000, Heroku will assign its own port
	app.run(host='0.0.0.0', port=port)



	