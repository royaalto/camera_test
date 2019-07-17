import hashlib
import os
import base64
from datetime import datetime
import subprocess

with open('GetRelayOutputs.xml', 'r') as myfile:
    data = myfile.read()
username = "service"
password = "iPilot!19"
# created = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z")
created = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z")
#created = "2019-01-31T09:29:20.000Z"

raw_nonce = os.urandom(20)

nonce = base64.b64encode(raw_nonce)
#nonce = "/kvdBcs9absreIW0ydzrg9fsgqE="
# raw_nonce=base64.b64decode(nonce)
sha1 = hashlib.sha1()
sha1.update(raw_nonce + created.encode('utf8') + password.encode('utf8'))
raw_digest = sha1.digest()
digest = base64.b64encode(raw_digest)
req_body = data.format(username=username, nonce=nonce.decode(
    'utf8'), created=created, digest=digest.decode('utf8'))
print(req_body)
text_file = open("test.xml", "w")
text_file.write(req_body)
text_file.close()
os.system("curl --silent -X POST --header 'Content-Type: text/xml; charset=utf-8;; action=\"http: // www.onvif.org/ver20/ptz/wsdl/Stop\"' --header 'SOAPAction: \"http: // www.onvif.org/ver20/ptz/wsdl/Stop\"' -d @test.xml 'http://192.168.10.241/onvif/device_service' | xmllint --format -")
