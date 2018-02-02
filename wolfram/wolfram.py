#https://medium.com/@salisuwy/build-an-ai-assistant-with-wolfram-alpha-and-wikipedia-in-python-d9bc8ac838fe

from credentials import *
import wolframalpha
import xml.etree.ElementTree as ET

client = wolframalpha.Client(app_id)

#print(app_id)
#question = input("Ask Wolfram Alpha a question ")
question = "who is the us president"
if question:
    result = client.query(question)
else:
    question = input("Please try that again ")

for item in result:
    print(item)
##root = ET.fromstring(result)
##error = root.get("error")
##success = root.get("success")
##numpods = root.get("numpods")
##answer = ""
##
##print(success, numpods)
##if success and int(numpods) > 0:
##    for plaintext in root.iter("plaintext"):
##        answer += plaintext.text
##    print(answer)
##elif error:
##    print("That query threw an error")
##
