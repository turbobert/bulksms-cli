#!/usr/bin/env python3

import os
home = os.getenv("HOME", None)
pwfile = "%s/.bulksms" % home
with open(pwfile, "r") as f:
    data = f.read().strip().split("\n")
(u, pw) = [x.strip() for x in data]



import requests
url = "https://bulksms.vsms.net/eapi/submission/send_sms/2/2.0"

import sys
if len(sys.argv) == 1 or len(sys.argv) != 3:
    lines = sys.stdin.read().strip().split("\n")
    recipient = lines[0].strip()
    text = lines[1].strip().encode("iso-8859-1")
else:
    recipient = sys.argv[1]
    text = sys.argv[2].encode("iso-8859-1")

print("[%s][%s]" % (recipient, text))

r = requests.post(url, data = { "username": u, "password": pw, "message": text, "msisdn": recipient})
print(r.text)
