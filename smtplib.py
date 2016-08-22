#!/usr/bin/python

import smtplib

sender = 'alexander.voronin@macys.com'
receivers = ['alexander.voronin@macys.com']

message = """From: Alexander Voronin <alexander.voronin@macys.com>
To: Alexander Voronin <alexander.voronin@macys.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print "Successfully sent email"
except smtplib.SMTPException:
   print "Error: unable to send email"
