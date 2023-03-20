from flask_mail import Mail, Message
from flask import render_template, redirect, url_for
from .extensions import mail
    

def foo():
  return render_template('mail.html')

def email():
  msg = Message('Session Scheduled', sender =   'noreply@csschool.io', recipients = ['paul@mailtrap.io'])
  msg.body = "Hey Paul, your session has been scheduled!"
  mail.send(msg)
  return "Message sent!"