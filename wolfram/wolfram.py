#https://medium.com/@salisuwy/build-an-ai-assistant-with-wolfram-alpha-and-wikipedia-in-python-d9bc8ac838fe

from credentials import *
import wolframalpha
import xml.etree.ElementTree as ET

client = wolframalpha.Client(app_id)

def resolveListOrDict(variable):
  if isinstance(variable, list):
    return variable[0]["plaintext"]
  else:
    return variable["plaintext"]

def removeBrackets(variable):
  return variable.split("(")[0]

question = "who is the world's fastest man"
if question:
    result = client.query(question)
else:
    question = input("Please try that again ")

if not result["@success"]:
    print("Please try again")
else:
    try:
        pod0 = result['pod'][0]['subpod']['plaintext']
        pod1 = result['pod'][1]['subpod']['plaintext']
        print(pod0, pod1)
    except:
        print("Something went wrong")
