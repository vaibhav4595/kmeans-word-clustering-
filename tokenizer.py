import re
import sys
import json
from collections import OrderedDict
reload(sys)
sys.setdefaultencoding('UTF-8')

regex_check = '^[\w]+[-?(\w)+]*$'
regdate = '\d{2}[-/.]\d{2}[-/.]\d{4}'
regtime = '\d{2}:\d{2}(:\d{2})?'
regex1 = '^\w+[-?\w]*$'
regex2 = '^\w+[-?\w]+(\\,|\\.)$'
regex3 = '^\(\w+[-?\w]+\)$'
regex4 = '^(\(|")"?[\w]+[-?[\w]+]*"?(\)|")$'
regex6 = '^(\(|\)|"|,|\.|;)*\w+(\(|\)|"|,|\.|;)*$'
regex5 = '^[\w]+\'[\w]$'
regex7 = '^[\*|.|,|-|=|+|{|}|"|\'|#|!]+$'
regex8 = '^<\w+>\w]+</\w+>$'
regex9 = '^[\w]+:[\w]+$'
regex10 = '^\w+='
regex11 = '^\w+-?\w+:\w+'
regex12 = '^\(.*\)$'

tokendict = {}
tokendict2 = {}
tokendict3 = {}
tokenarr = []

arraylist = ["Co.", "Corp.", "vs.", "e.g.", "etc.", "ex.", "cf.",
            "eg.", "Jan.", "Feb.", "Mar.", "Apr.", "Jun.", "Jul.", "Aug.",
            "Sept.", "Oct.", "Nov.", "Dec.", "jan.", "feb.", "mar.",
            "apr.", "jun.", "jul.", "aug.", "sept.", "oct.", "nov.",
            "dec.", "ed.", "eds.", "repr.", "trans.", "vol.", "vols.",
            "rev.", "est.", "b.", "m.", "bur.", "d.", "r.", "M.", "Dept.",
            "MM.", "U.", "Mr.", "Jr.", "Ms.", "Mme.", "Mrs.", "Dr.",
            "Ph.D."]

def biaddtodict(string):
    if tokendict2.has_key(string):
        tokendict2[string] += 1
    else:
        tokendict2[string] = 1

def triaddtodict(string):
    if tokendict3.has_key(string):
        tokendict3[string] += 1
    else:
        tokendict3[string] = 1

def tokenize(string):
    tokenarr.append(string)
    if tokendict.has_key(string):
        tokendict[string] += 1
    else:
        tokendict[string] = 1

def stringify(string, start, end):
    if type(string) == int:
        tokenize(string)
        return

    for each in xrange(0, start):
        tokenize(each)
    tokenize(string[start:end])
    for each in xrange(end, len(string)):
        tokenize(each)


def token_it(filename):
    fp = open(filename)
    lines = fp.read()
    splitBySpaces = lines.split()

    for each in splitBySpaces:

        if each in arraylist:
            if ',' in each:
                ind = each.index(',')
                if ind == 0:
                    tokenize(',')
                    tokenize(each[1:])
                else:
                    tokenize(each[:-1])
                    tokenize(each[-1])
            else:
                tokenize(each)

        result = re.search(regdate, each, flags = re.UNICODE)
        if result:
            for indexes in xrange(0, result.start()):
                tokenize(each[indexes])
            tokenize(each[result.start():result.end()])
            for indexes in xrange(result.end(), len(each)):
                tokenize(each[indexes])
            continue

        result = re.search(regtime, each, flags = re.UNICODE)
        if result:
            for indexes in xrange(0, result.start()):
                tokenize(each[indexes])
            tokenize(each[result.start():result.end()])
            for indexes in xrange(result.end(), len(each)):
                tokenize(each[indexes])
            continue

        result = re.search(regex1, each, flags = re.UNICODE)
        if result:
            tokenize(each)
            continue

        result = re.search(regex2, each)
        if result:
            tokenize(each[:-1])
            tokenize(each[-1])
            continue

        result = re.search(regex3, each)
        if result:
            tokenize(each[0])
            tokenize(each[1:-1])
            tokenize(each[-1])
            continue

        result = re.search(regex4, each)
        if result:
            if each[0] == '(' or each[-1] == ')':
                if each[0] == '(' and each[-1] == ')':
                    if each[1] == '"' and each[-2] == '"':
                        tokenize(each[0])
                        tokenize(each[1])
                        tokenize(each[2:-2])
                        tokenize(each[-2])
                        tokenize(each[-1])
                    elif each[1] == '"':
                        tokenize(each[0])
                        tokenize(each[1])
                        tokenize(each[2:-1])
                        tokenize(each[-1])
                    elif each[-2] == '"':
                        tokenize(each[0])
                        tokenize(each[1:-2])
                        tokenize(each[-2])
                        tokenize(each[-1])
                elif each[0] == '(':
                    if each[1] == '"' and each[-1] == '"':
                        tokenize(each[0])
                        tokenize(each[1])
                        tokenize(each[2:-1])
                        tokenize(each[-1])
                    elif each[1] == '"':
                        tokenize(each[0])
                        tokenize(each[1])
                        tokenize(each[2:])
                    elif each[-1] == '"':
                        tokenize(each[0])
                        tokenize(each[1:-1])
                        tokenize(each[-1])
                elif each[-1] == ')':
                    if each[0] == '"' and each[-2] == '"':
                        tokenize(each[0])
                        tokenize(each[1:-2])
                        tokenize(each[-2])
                        tokenize(each[-1])
                    elif each[0] == '"':
                        tokenize(each[0])
                        tokenize(each[1:-1])
                        tokenize(each[-1])
                    elif each[-2] == '"':
                        tokenize(each[0:-2])
                        tokenize(each[-2])
                        tokenize(each[-1])

            elif each[0] == '"' or each[-1] == '"':
                if each[0] == '"' and each[-1] == '"':
                    tokenize(each[0])
                    tokenize(each[1:-1])
                    tokenize(each[-1])
                elif each[0] == '"':
                    tokenize(each[0])
                    tokenize(each[1:])
                elif each[-1] == '"':
                    tokenize(each[0:-1])
                    tokenize(each[-1])

            continue

        result = re.search(regex6, each, flags = re.UNICODE)
        if result:
            result = re.search('[\w]+', each)
            if result:
                for indexes in xrange(0, result.start()):
                    tokenize(each[indexes])
                tokenize(each[result.start():result.end()])
                for indexes in xrange(result.end(), len(each)):
                    tokenize(each[indexes])
                continue
            else:
                tokenize(each)

        result = re.search(regex8, each, flags = re.UNICODE)
        if result:
            result = re.search('<\w+>', each, flags = re.UNICODE)
            tokenize(each[result.start():result.end()])
            result = re.search('</\w+>', each, flags = re.UNICODE)
            tokenize(each[result.start():result.end()])
            result = re.search('>\w+<', each, flags = re.UNICODE)
            tokenize(each[result.start() + 1:result.end() - 1])
            continue

        result = re.search(regex9, each, flags = re.UNICODE)
        if result:
            pos = each.find(':')
            tokenize(each[0:pos])
            tokenize(each[pos])
            tokenize(each[pos + 1:])
            continue

        result = re.search(regex10, each, flags = re.UNICODE)
        if result:
            tokenize(each[result.start():result.end()])
            temp = each[result.end():]
            temp = temp.split('|')
            for eg in xrange(0, len(temp)):
                if temp[eg] == '':
                    tokenize('|')
                else:
                    result2 = re.search('\w+-\w+:\w+', temp[eg])
                    if result2:
                        for indexes in xrange(0, result2.start()):
                            tokenize(temp[eg][indexes])
                        tokenize(temp[eg][result2.start():result2.end()])
                        for indexes in xrange(result2.end(), len(temp[eg])):
                            tokenize(temp[eg][indexes])
                    else:
                        tokenize(temp[eg])
                    if eg != len(temp) - 1:
                        tokenize('|')
            continue

        result = re.search(regex11, each, flags = re.UNICODE)
        if result:
            tokenize(each[result.start():result.end()])
            newstr = each[result.end():]
            result2 = re.search('\w+', newstr)
            if result2:
                for indexes in xrange(0, result2.start()):
                    tokenize(newstr[indexes])
                tokenize(newstr[result2.start():result2.end()])
                for indexes in xrange(result2.end(), len(newstr)):
                    tokenize(newstr[indexes])
            else:
                for checks in newstr:
                    tokenize(checks)
            continue

        result = re.search(regex12, each, flags = re.UNICODE)
        if result:
            tokenize('(')
            tokenize(each[1:-1])
            tokenize(')')
            continue

        if 1:
            tokenize(each)

    oneGram = OrderedDict(sorted(tokendict.items(), key = lambda x : x[1], reverse = True))
    return oneGram, tokenarr
