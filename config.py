import os

# Basic Auth Username and Password
BASIC_AUTH_USERNAME = os.environ.get('BASIC_AUTH_USERNAME')
BASIC_AUTH_PASSWORD = os.environ.get('BASIC_AUTH_PASSWORD')

# Plivo Auth ID and Auth Token
PLIVO_AUTH_ID = os.environ.get('PLIVO_AUTH_ID')
PLIVO_AUTH_TOKEN = os.environ.get('PLIVO_AUTH_TOKEN')

# Plivo Caller ID
PLIVO_CALLER_ID = os.environ.get('PLIVO_CALLER_ID', '')

# Wait announcement music when there is only 1 participant in the conference
HOLD_MUSIC = 'https://s3.amazonaws.com/plivocloud/music.mp3'

# Wait announcement message when there is only 1 participant in the conference
CONFERENCE_WAIT_ANNOUNCEMENT = "Please wait for our agent to join. Thank you."

# Announcement message before entering the conference
CONFERENCE_ANNOUNCEMENT = 'Welcome to tendigit support.'

# Enable this to have the ability to add people to a conference by calling a
# PSTN number. 
ALLOW_OUTBOUND_PSTN = True

# Enable this to attach an incoming number to every ad-hoc conference created.
# Be careful with this flag. Turning this to True will result in renting a new number
# with every conference created from this app.
ALLOW_INBOUND_DID = False

# Expire a conference in 24 hours when this flag is enabled.
EXPIRE_CONFERENCE = not ALLOW_INBOUND_DID
