import requests
from bs4 import BeautifulSoup
import re

def pullFactoring():
    line = "http://webspace.ship.edu/deensley/m100/ws5.html"

    problemSet = []
    text = requests.get(line)
    bs = BeautifulSoup(text.text, "lxml")
    for ol  in bs.findAll("ol"):
        lis = ol.findAll("li")
        for li in lis:
            problemSet.append(li.text)

    # sheet also contained answers, had to remove those
    problemSet[13:len(problemSet)] = []
    return problemSet

def formatProblemSet(problemSet):
    # Ran into some issues with regex, need to learn more and come back
    # x2 + 3 x - 10 -> x*+ 3 x - 10 because of below
    # item = re.sub("x(\d)+", "x*\1",  str(item))
    print("Will Return")

problemSet = pullFactoring()
formatProblemSet(problemSet)