import requests
from bs4 import BeautifulSoup
import re
import sympy as sym


def pullFactoring():
    line = "http://webspace.ship.edu/deensley/m100/ws5.html"

    problemSet = []
    text = requests.get(line)
    bs = BeautifulSoup(text.text, "lxml")
    for ol in bs.findAll("ol"):
        lis = ol.findAll("li")
        for li in lis:
            problemSet.append(li.text)

    # sheet also contained answers, had to remove those
    problemSet[13:len(problemSet)] = []
    return problemSet


def formatProblemSet(problemSet):
    # The formatting here could use some cleaning up
    problemSet = ''.join(problemSet)
    problemSet = problemSet.replace(" ", "")

    problemSet = re.sub("(\d+)(x)", lambda x: \
        str(x.group(1)) + "*x", problemSet)

    problemSet = re.sub("(x)(\d+)", lambda x: \
        "x**" + str(x.group(2)), problemSet)

    problemSet = problemSet.split()
    problemSet = list(problemSet)
    return problemSet

def solveProblems(problemSet):
    solved = {}
    x = sym.symbols("x")

    for item in problemSet:
        solvedLocal = sym.factor(item)
        solved[item] = {solvedLocal}
    return solved

problemSet = pullFactoring()
problemSet = formatProblemSet(problemSet)
solved = solveProblems(problemSet)
for key, value in solved.items():
    print(key, value)