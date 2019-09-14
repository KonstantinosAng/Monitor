#! /usr/bin/python3

try:
	from urllib.request import urlopen
except ImportError:
	from urllib2 import urlopen

import re
import smtplib
import os

# setup login credentials

# Settings

# from_address = Write the email address you want the email to be sent from ( example@gmail.com inside the quotes )

# to_address = Write the email address you want the email to be sent to (example@gmail.com inside the quotes)

# If you want to be sent to the same address you can put the same address to from_address and to_address

# Subject = Write the Subject you want the email to have

# Username = Write the username to be used as login at the gmail. For example for GMAIL the username is the same email address as the own you wrote at from_address 

# Password = Write the password that you have to login at the email


from_address = 'Your Email Address' 
to_address = 'Your Email Address'
subject = 'Subject of Email'
username = 'Username or Email to login'
password = 'Password for login at email'

# Function to send email
def send_email(ourIP):
	#Body of email
	body_text =  ourIP # the body of the email
	msg = '\r\n'.join(['To: %s' % to_address,
			   'From: %s' % from_address,
			   'Subject: %s' % subject,
			   '', body_text]) # Initialize the message
	#Send email
	server = smtplib.SMTP('smtp.gmail.com:587') # Open server
	server.ehlo() # Send identification to server
	server.starttls() # Our security for transmission of credentials
	server.ehlo() # Send identification to server
	server.login(username,password) # Login to server
	server.sendmail(from_address, to_address, msg) # Send email 
	server.quit() # Log out and quit the session

# Function for measuring and storing temperature value
def measure_temp():
        temp = os.popen("vcgencmd measure_temp").readline() # Measure Temp of CPU
        return (temp.replace("temp=","").replace("'C\n","")) # Return value of temperature as string

#Check Temp
temp = float( measure_temp()) # Call first functio to measure temp

# Check if Temp is above 65'C
if (temp > 65):
	#send_email
	send_email('Temperature is High ' + str(temp)+ " 'C") # If temperature is above 65 'C notify via email

