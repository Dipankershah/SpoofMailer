# name="Dipanker shah"
import requests

def send():
    r = requests.post("http://gourl.gq/email.php", data={'fake_email': 'info@gourl.gq', 'subject': 'Test', 'txt': 'Boday','sender_email':'dipankarshah143@gmail.com','name':'name'})
    # print(r.status_code, r.reason)
    return r.status_code

# s= send()
# print(s)