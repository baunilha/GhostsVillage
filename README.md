## Ghosts' Village - Using Remote APIs

Ghosts' Village is an application that uses your phone to influence the behavior of the website where its hosted.

The user calls a Twilio number that gives him options through '/gather'. The user chooses one option, Twilio send the audio to the user's phone and Pusher updates the website with the new information. 

The website is online at: ghostsvillage.herokuapp.com

To try, go ahead!
Download code. Open code directory in Terminal.

#### #1 Create virtualenv

	virtualenv venv


#### #2 Install requirements

In your code directory run the command below to install new requirements.

	. runpip

or

	. venv/bin/activate
	pip install -r requirements.txt


3 libraries we're using in this example, Twilio, Pusher and Requests


#### #3 Start server

Start server

	. start

or 

	. venv/bin/activate
	foreman start


* If successful you can navigate to <a href='http://localhost:5000'>http://localhost:5000</a>.

-----------


## Twilio

### Getting Twilio Account

* Register [https://www.twilio.com/try-twilio](https://www.twilio.com/try-twilio).
* Verify phone number with access code.
* Pick a phone number.
* Poke around all their API endpoints, make and receive calls, make and receive SMS.

When you are registered locate your your Account SID and Auth Token here,[https://www.twilio.com/user/account](https://www.twilio.com/user/account) and add them to your .env file

**.env**	

	TWILIO_ACCOUNT_SID=xxxxxxxxxxxxxx
	TWILIO_AUTH_TOKEN=xxxxxxxxx
	TWILIO_PHONE_NUMBER=+XXXXXXXXX

Now let's add the Twilio account variables to Heroku.

**In your code directory in Terminal run,**

	heroku config:add TWILIO_ACCOUNT_SID=xxxxxxxxxxxxxx
	heroku config:add TWILIO_AUTH_TOKEN=xxxxxxxxxxxxxx
	heroku config:add TWILIO_PHONE_NUMBER=+XXXXXXXXX


-----------


## jQuery/Pusher

jQuery is a very popular and useful Javascript library that is used to minimize the amount of Javascript you need to write to manipulate HTML DOM elements, add click events and AJAX functions. We will use AJAX in all the demos on this site.

## PUSHER - Realtime Web Service

[Pusher.com](http://www.pusher.com) is a great way to add realtime events to your webapp.

Register for an account at [http://pusher.com/](http://pusher.com/). You will need to create a .env file that includes the following information about your Pusher account.

**.env**

	PUSHER_APP_ID=XXXXXX
	PUSHER_KEY=XXXXXXXXXXXXX
	PUSHER_SECRET=XXXXXXXXXXXXXX

Save your .env file.

You will have to push your new .env variables to Heroku config so their servers have your credientals.

In your code directory in Terminal run the following command.

	heroku config:add PUSHER_APP_ID=XXXXXX
	heroku config:add PUSHER_KEY=XXXXXXXXXXXXXXX
	heroku config:add PUSHER_SECRET=XXXXXXXXXXXXX

