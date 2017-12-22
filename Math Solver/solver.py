"""
Thanks to reddit's /u/henrebotha and /u/ka-splam for
reviewing and improving this code
"""

import requests
from bs4 import BeautifulSoup
import re
import sympy as sym


def pullFactoring():
    problems = "http://webspace.ship.edu/deensley/m100/ws5.html"

    problemSet = []
    text = requests.get(problems)
    bs = BeautifulSoup(text.text, "lxml")

    problemSet = [li.text for ol in bs.findAll("ol") for li in
                  ol.findAll("li")]

    #for ol in bs.findAll("ol"):
    #    lis = ol.findAll("li")
    #    for li in lis:
    #        problemSet.append(li.text)

    # sheet also contained answers, had to remove those
    return problemSet[0:13]


def formatProblemSet(problemSet):
    problemSet = ''.join(problemSet)

    problemSet = problemSet.replace(" ", "")
    problemSet = re.sub(r"(\d)x", r"\1*x", problemSet)
    problemSet = re.sub(r"x(\d+)", r"x**\1", problemSet)

    problemSet = problemSet.split()
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
    print(key, "\n", value, "\n")
