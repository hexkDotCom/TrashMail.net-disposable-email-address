# based on the work of Laszlo Szthmary
# https://github.com/jabbalaci/TrashMail.net-disposable-email-address

import re
import json
import requests

USERNAME = ""
PASSWORD = ""
DOMAIN = ""
#
DEBUG = True


def get_session_id_and_real_email():
    """
    Login and get a session ID and your real email.
    """
    payload = {
        "api": 1,
        "cmd": "login",
        "fe-login-user": USERNAME,
        "fe-login-pass": PASSWORD
    }
    r = requests.post('https://trashmail.com/', data=payload)
    if DEBUG:
        print r.headers
    # Holy shit: you need the SECOND session ID, not the first one!
    session_id = re.findall(r"trashmail_session=(.*?);", r.headers['set-cookie'])[-1]
    if DEBUG:
        print session_id
    real_email = r.json()['msg']['real_email_list'].keys()[0]

    return session_id, real_email


def create_temp_email(session_id, real_email, disposable_name):
    """
    Create a new disposable email address.
    For this, we need to provide the session ID.
    The real email address must be given too where
    emails will be redirected to.
    """
    payload = {
        "data": {
            "id": -1,
            "uid": None,
            "ctime": 0,
            "ctime_text": "",
            "disposable_name": disposable_name,
            "disposable_domain": DOMAIN,
            "destination": real_email,
            "forwards": -1,      # that's the maximum number of forwards for the free service
            "expire": -1,        # max. value: 31 (one month)
            "website": "",
            "cs": 0,
            "notify": True,
            "desc": ""
        }
    }
    cookie = {'trashmail_session': session_id}
    headers = {'content-type': 'text/plain'}

    r = requests.post('https://trashmail.com/?api=1&cmd=update_dea',
        cookies=cookie, data=json.dumps(payload), headers=headers
    )
    if DEBUG:
        print r.text
    data = r.json()['data'][0]
    temp_email = "{0}@{1}".format(data['disposable_name'], data['disposable_domain'])

    return temp_email


def main():
    with open("import.csv", 'r') as f:
        lines = f.readlines()
    if DEBUG:
        print(lines)
        print("\n")

    session_id, real_email = get_session_id_and_real_email()
    if DEBUG:
        print(session_id)
        print(real_email)

    for l in lines:
        line = l.strip()
        email = create_temp_email(session_id, real_email, line)
        print email
#############################################################################


if __name__ == "__main__":
    if USERNAME and PASSWORD:
        main()
    else:
        print """Create a TrashMail.net disposable email address
You must provide the username and password that you use
on trashmail.net to access the address manager"""
        if not USERNAME:
            USERNAME = raw_input("Username: ")
        else:
            print "Username:", USERNAME
        if not PASSWORD:
            PASSWORD = raw_input("Password: ")
        else:
            print "Password:", '*' * len(PASSWORD)
        main()
