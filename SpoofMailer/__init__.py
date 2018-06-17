# name="Dipanker shah"
import requests

sender_email=""
sender_name=""
receiver_email=""
body=""
subject=""

def set_sender_name(s):
    sender_name=s

def set_sender_email(s):
    sender_email=s


def set_receiver_email(s):
    receiver_email=s

def set_subject(s):
    subject=s

def set_body(s):
    body=s

def send():
    if (sender_email!=""&sender_name!=""&receiver_email!=""&subject!=""&body!=""):
        r = requests.post("http://gourl.gq/email.php", data={'fake_email': sender_email, 'subject': subject, 'txt': body,'sender_email':receiver_email,'name':sender_name})
        print "Mail sent!"
        return r.status_code
    else:
        print "Please set all arguments"
        return "Insufficient arguments set"