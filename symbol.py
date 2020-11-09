#Vournazidis Anastasios A.M. 2413 username: cse32413
#Kyrkopoulos Pantelis A.M. 1697 username: cs091697

import sys

matrix = [
        [1, 2, "plustk", "minustk", "multtk", 3, 7, 8, "equaltk", 9, "commatk", "lpartk", "rpartk", "lbracketstk", "rbracketstk","eoftk", 0, 0, 0, "semicolontk", "othertk"],
        [1, 1, "idtk", "idtk", "idtk", "idtk", "idtk", "idtk", "idtk", "idtk", "idtk", "idtk", "idtk", "idtk", "idtk", "idtk", "idtk", "idtk", "idtk", "idtk", "idtk"],
        ["constanttk", 2, "constanttk", "constanttk", "constanttk", "constanttk", "constanttk", "constanttk", "constanttk", "constanttk", "constanttk", "constanttk", "constanttk", "constanttk", "constanttk", "constanttk", "constanttk", "constanttk", "constanttk", "constanttk", "constanttk"],
        ["divtk", "divtk", "divtk", "divtk", 5, 4, "divtk", "divtk", "divtk", "divtk", "divtk", "divtk", "divtk", "divtk", "divtk", "divtk", "divtk", "divtk", "divtk", "divtk", "divtk"],
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4],
        [5, 5, 5, 5, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, "errortk", 5, 5, 5, 5, 5],
        [5, 5, 5, 5, 6, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, "errortk", 5, 5, 5, 5, 5],
        ["lessthantk", "lessthantk", "lessthantk", "lessthantk", "lessthantk", "lessthantk", "lessthantk", "differenttk", "lessequaltk", "lessthantk", "lessthantk", "lessthantk", "lessthantk", "lessthantk", "lessthantk", "errortk", "lessthantk", "lessthantk", "lessthantk", "lessthantk", "lessthantk"],
        ["morethantk", "morethantk", "morethantk", "morethantk", "morethantk", "morethantk", "morethantk", "morethantk", "moreequaltk", "morethantk", "morethantk", "morethantk", "morethantk", "morethantk", "morethantk", "errortk", "morethantk", "morethantk", "morethantk", "morethantk", "morethantk"],
        ["colontk", "colontk", "colontk", "colontk", "colontk", "colontk", "colontk", "colontk", "assignmenttk", "colontk", "colontk", "colontk", "colontk", "colontk", "colontk", "errortk", "colontk", "colontk", "colontk", "colontk", "colontk"]
    ]
line = 1
quads = []
tempCounter = 0
exitlist = []
programName = ""

returnCounter = 0

scopes = []

def lex(token):
    global line
    word = ""
    state = 0

    while str(state).endswith("tk") == False:
        ch = infile.read(1)
        if len(word) < 30:
            word = word + ch

        if ch.isalpha() == True:
            state = matrix[state][0]
        elif ch.isdigit() == True:
            state = matrix[state][1]
        elif ch == "+":
            state = matrix[state][2]
        elif ch == "-":
            state = matrix[state][3]
        elif ch == "*":
            state = matrix[state][4]
        elif ch == "/":
            state = matrix[state][5]
        elif ch == "<":
            state = matrix[state][6]
        elif ch == ">":
            state = matrix[state][7]
        elif ch == "=":
            state = matrix[state][8]
        elif ch == ":":
            state = matrix[state][9]
        elif ch == ",":
            state = matrix[state][10]
        elif ch == "(":
            state = matrix[state][11]
        elif ch == ")":
            state = matrix[state][12]
        elif ch == "[":
            state = matrix[state][13]
        elif ch == "]":
            state = matrix[state][14]
        elif ch == "":
            state = matrix[state][15]
        elif ch == "\n":
            state = matrix[state][16]
            line = line + 1
        elif ch == "\t":
            state = matrix[state][17]
        elif ch == " ":
            state = matrix[state][18]
        elif ch == ";":
            state = matrix[state][19]
        else:
            state = matrix[state][20]

        if state == 0:
            word = ""

    if state == "errortk":
        print "Grammi",line,": Den kleinoun ta sxolia prin to telos tou arxeiou"
        exit(0)
    if state == "othertk":
        print "Grammi",line,": O xarakthras",ch,"den anagnorizetai"
        exit(0)

    if state == "idtk" or state == "constanttk" or state == "divtk" or state == "lessthantk" or state == "morethantk" or state == "colontk":
        infile.seek(-1,1)
        if ch == "\n":
            infile.read(1)
        if len(word) <= 30:
            word = word[0:len(word) - 1]

    if state == "constanttk":
        if int(word) > 32767:
            print "Grammi",line,": O arithmos einai poly megalos"
            exit(0)

    if state == "idtk":
        if word == "program":
            state = "programtk"
        elif word == "endprogram":
            state = "endprogramtk"
        elif word == "declare":
            state = "declaretk"
        elif word == "enddeclare":
            state = "enddeclaretk"
        elif word == "if":
            state = "iftk"
        elif word == "then":
            state = "thentk"
        elif word == "else":
            state = "elsetk"
        elif word == "endif":
            state = "endiftk"
        elif word == "while":
            state = "whiletk"
        elif word == "endwhile":
            state = "endwhiletk"
        elif word == "repeat":
            state = "repeattk"
        elif word == "endrepeat":
            state = "endrepeattk"
        elif word == "exit":
            state = "exittk"
        elif word == "switch":
            state = "switchtk"
        elif word == "case":
            state = "casetk"
        elif word == "endswitch":
            state = "endswitchtk"
        elif word == "forcase":
            state = "forcasetk"
        elif word == "when":
            state = "whentk"
        elif word == "endforcase":
            state = "endforcasetk"
        elif word == "procedure":
            state = "proceduretk"
        elif word == "endprocedure":
            state = "endproceduretk"
        elif word == "function":
            state = "functiontk"
        elif word == "endfunction":
            state = "endfunctiontk"
        elif word == "call":
            state = "calltk"
        elif word == "return":
            state = "returntk"
        elif word == "in":
            state = "intk"
        elif word == "inout":
            state = "inouttk"
        elif word == "and":
            state = "andtk"
        elif word == "or":
            state = "ortk"
        elif word == "not":
            state = "nottk"
        elif word == "true":
            state = "truetk"
        elif word == "false":
            state = "falsetk"
        elif word == "input":
            state = "inputtk"
        elif word == "print":
            state = "printtk"

    token[0] = word
    token[1] = state


def relationaloper(token):
    if token[1] == "equaltk" or token[1] == "lessequaltk" or token[1] == "moreequaltk" or token[1] == "lessthantk" or token[1] == "morethantk" or token[1] == "differenttk":
        token[2] = token[0]
        lex(token)
    else:
        print "Grammi",line,": Prepei na yparxei telesths sygkrishs"
        exit(0)

def optionalSign(token):
    if token[1] == "plustk" or token[1] == "minustk":
        lex(token)

def actualparitem(token):
    if token[1] == "intk":
        lex(token)
        expression(token)
        genquad("par",token[2],"CV","_")
    elif token[1] == "inouttk":
        lex(token)
        if token[1] == "idtk":
            found = False
            for i in range(len(scopes)-1, -1, -1):
                for entity in scopes[i][2]:
                    if entity[0] == token[0]:
                        found = True
                        if len(entity) == 4:
                            print "Grammi",line,": to",token[0], "den einai metavlhth/parametros"
                            exit(0)
                        break
                if found == True:
                    break

            if found == False:
                print "Grammi",line,": Den exeis dhlwsei thn metavlhth ",token[0]
                exit(0)
            genquad("par",token[0],"REF","_")
            lex(token)
        else:
            print "Grammi",line,": Prepei na exei onoma parametrou"
            exit(0)
    else:
        print "Grammi",line,": Prepei na yparxei in i inout"
        exit(0)

def actualparlist(token):
    actualparitem(token)
    while token[1] == "commatk":
        lex(token)
        actualparitem(token)

def actualpars(token):
    if token[1] == "lpartk":
        lex(token)
        if token[1] != "rpartk":
            actualparlist(token)

        if token[1] == "rpartk":
            lex(token)
        else:
            print "Grammi",line,": Prepei na teleiwnei me )"
            exit(0)
    else:
        print "Grammi",line,": Prepei na exei ("
        exit(0)

def idtail(token):
    if token[1] == "lpartk":
        actualpars(token)

def factor(token):
    if token[1] == "constanttk":
        token[2] = token[0]
        lex(token)

    elif token[1] == "lpartk":
        lex(token)
        expression(token)
        if token[1] == "rpartk":
            lex(token)
        else:
            print "Grammi",line,": Den yparxei )"
            exit(0)
    elif token[1] == "idtk":

        token[2] = token[0]
        callName = token[0]
        lex(token)

        found = False
        for i in range(len(scopes)-1, -1, -1):
            for entity in scopes[i][2]:
                if entity[0] == callName:
                    found = True
                    if len(entity) == 4:
                        if token[1] == 'lpartk':
                            if entity[1] == 'proceduretk':
                                print "Grammi",line,": Den mporeis na kaleseis diadikasia me ayto ton tropo"
                                exit(0)
                        else:
                            print "Grammi",line,": to",callName, "den einai metavlhth/parametros"
                            exit(0)
                    else:
                        if token[1] == 'lpartk':
                            print "Grammi",line,": to",callName, "den einai synarthsh"
                            exit(0)
                    break
            if found == True:
                break

        if found == False:
            print "Grammi",line,": Den exeis dhlwsei thn metavlhth ",callName
            exit(0)

        if token[1] == "lpartk":
            idtail(token)
            temp = newtemp()
            genquad("par", temp, "RET","_")
            genquad("call", callName, "_", "_")
            token[2] = temp
    else:
        print "Grammi",line,": Den yparxei to stathera, id i ("
        exit(0)

def term(token):
    factor(token)
    f1place = token[2]
    while token[1] == "multtk" or token[1] == "divtk":
        operator = token[0]
        lex(token)
        factor(token)

        f2place = token[2]
        w = newtemp()
        genquad(operator,f1place, f2place,w)
        f1place = w

    token[2] = f1place

def expression(token):
    optionalSign(token)
    term(token)
    t1place = token[2]
    while token[1] == "plustk" or token[1] == "minustk":
        operator = token[0]
        lex(token)
        term(token)

        t2place = token[2]
        w = newtemp()
        genquad(operator,t1place, t2place,w)
        t1place = w

    token[2] = t1place

def boolfactor(token):
    if token[1] == "truetk":
        lex(token)
        token[3] = makelist(nextquad())
        genquad("jump", "_", "_", "_")
        token[4] = emptylist()

    elif token[1] == "falsetk":
        lex(token)
        token[3] = emptylist()
        token[4] = makelist(nextquad())
        genquad("jump", "_", "_", "_")

    elif token[1] == "nottk":
        lex(token)
        if token[1] == "lbracketstk":
            lex(token)
            condition(token)
            token[3], token[4] = token[4], token[3]
            if token[1] == "rbracketstk":
                lex(token)
            else:
                print "Grammi",line,": Den yparxei ]"
                exit(0)
        else:
            print "Grammi",line,": Den yparxei ["
            exit(0)
    elif token[1] == "lbracketstk":
        lex(token)
        condition(token)
        if token[1] == "rbracketstk":
            lex(token)
        else:
            print "Grammi",line,": Den yparxei ]"
            exit(0)
    else:
       expression(token)
       e1place = token[2]
       relationaloper(token)
       reloperator = token[2]
       expression(token)
       e2place = token[2]

       token[3] = makelist(nextquad())
       genquad(reloperator, e1place, e2place, "_")
       token[4] = makelist(nextquad())
       genquad("jump", "_", "_", "_")


def boolterm(token):
    boolfactor(token)

    bf1true = token[3]
    bf1false = token[4]

    while token[1] == "andtk":

        backpatch(bf1true, nextquad())
        lex(token)
        boolfactor(token)

        bf2true = token[3]
        bf2false = token[4]

        bf1true = bf2true
        bf1false = merge(bf1false, bf2false)

    token[3] = bf1true
    token[4] = bf1false


def condition(token):
    boolterm(token)

    bt1true = token[3]
    bt1false = token[4]

    while token[1] == "ortk":

        backpatch(bt1false, nextquad())

        lex(token)
        boolterm(token)

        bt2true = token[3]
        bt2false = token[4]

        bt1true = merge(bt1true, bt2true)
        bt1false = bt2false

def inputStat(token):
    if token[1] == "idtk":

        found = False
        for i in range(len(scopes)-1, -1, -1):
            for entity in scopes[i][2]:
                if entity[0] == token[0]:
                    found = True
                    if len(entity) == 4:
                        print "Grammi",line,": to",token[0], "den einai metavlhth/parametros"
                        exit(0)
                    break
            if found == True:
                break

        if found == False:
            print "Grammi",line,": Den exeis dhlwsei thn metavlhth ",token[0]
            exit(0)

        genquad("inp", token[0], "_", "_")
        lex(token)
    else:
        print "Grammi",line,": Prepei na yparxei onoma metavlhths"
        exit(0)


def returnStat(token):
    global returnCounter

    returnCounter = returnCounter + 1

    expression(token)
    genquad("retv", token[2], "_", "_")

def printStat(token):
    expression(token)
    genquad("out", token[2], "_", "_")

def callStat(token):
    if token[1] == "idtk":
        callName = token[0]
        lex(token)
        actualpars(token)

        found = False
        for i in range(len(scopes)-1, -1, -1):
            for entity in scopes[i][2]:
                if entity[0] == callName:
                    found = True
                    if len(entity) == 4:
                        if entity[1] != 'proceduretk':
                                print "Grammi",line,": Den mporeis na kaleseis synarthsh me ayto ton tropo"
                                exit(0)
                    else:
                        print "Grammi",line,": to",callName, "den einai diadikasia"
                        exit(0)

                    break
            if found == True:
                break

        if found == False:
            print "Grammi",line,": Den exeis dhlwsei thn metavlhth ",callName
            exit(0)


        genquad("call", callName, "_", "_")
    else:
        print "Grammi",line,": Prepei na yparxei onoma procedure"
        exit(0)

def forcaseStat(token):
    flag = newtemp()

    start = nextquad()
    genquad(":=","0","_",flag)
    if token[1] != "whentk":
        print "Grammi",line,": Prepei na yparxei toulaxiston ena when"
        exit(0)
    while token[1] == "whentk":
        lex(token)
        condition(token)
        if token[1] == "colontk":

            backpatch(token[3], nextquad())
            genquad("+","1",flag,flag)
            lex(token)
            statements(token)

            backpatch(token[4], nextquad())

        else:
            print "Grammi",line,": Den exei :"
            exit(0)

    if token[1] == "endforcasetk":
        genquad("<>","0",flag,start)
        lex(token)
    else:
        print "Grammi",line,": Den teleiwnei me endforcase"
        exit(0)

def switchStat(token):
    alljump = emptylist()

    expression(token)

    e1place = token[2]

    if token[1] != "casetk":
        print "Grammi",line,": Prepei na yparxei toulaxiston ena case"
        exit(0)
    while token[1] == "casetk":
        lex(token)
        expression(token)

        e2place = token[2]

        jlist = makelist(nextquad())
        genquad("<>", e1place, e2place, "_")

        if token[1] == "colontk":
            lex(token)
            statements(token)
            casejump = makelist(nextquad())
            genquad("jump","_","_","_")
            alljump = merge(alljump, casejump)
            backpatch(jlist, nextquad())

        else:
            print "Grammi",line,": Den exei :"
            exit(0)
    if token[1] == "endswitchtk":
        backpatch(alljump, nextquad())
        lex(token)
    else:
        print "Grammi",line,": Den teleiwnei me endswitch"
        exit(0)

def whileStat(token):
    start = nextquad()

    condition(token)

    backpatch(token[3], nextquad())

    statements(token)

    genquad("jump","_","_",start)

    backpatch(token[4], nextquad())

    if token[1] == "endwhiletk":
        lex(token)
    else:
        print "Grammi",line,": Den teleiwnei me endwhile"
        exit(0)
    return

def exitStat(token):
    global exitlist

    if len(exitlist) == 0:
        print "Grammi",line,": Yparxei exit xwris repeat"
        exit(0)

    elist = makelist(nextquad())
    genquad("jump","_","_","_")
    exitlist[len(exitlist) - 1] = merge(exitlist[len(exitlist) - 1], elist)
    return

def repeatStat(token):
    global exitlist

    exitlist.append(emptylist())
    start = nextquad()

    statements(token)

    genquad("jump", "_", "_", start)
    if token[1] == "endrepeattk":

        backpatch(exitlist[len(exitlist) - 1], nextquad())
        exitlist.pop(len(exitlist) - 1)
        lex(token)
    else:
        print "Grammi",line,": Den teleiwnei me endrepeat"
        exit(0)

def elsepart(token):
    if token[1] == "elsetk":
        lex(token)
        statements(token)

def ifStat(token):
    condition(token)

    if token[1] == "thentk":

        backpatch(token[3], nextquad())

        lex(token)
        statements(token)

        jlist = makelist(nextquad())
        genquad("jump","_","_","_")

        backpatch(token[4], nextquad())

        elsepart(token)

        backpatch(jlist, nextquad())

        if token[1] == "endiftk":
            lex(token)
        else:
            print "Grammi",line,": Den teleiwnei me endif"
            exit(0)
    else:
        print "Grammi",line,": Den exei then"
        exit(0)

def assignmentStat(token, assignmentId):

    global scopes
    found = False

    for i in range(len(scopes)-1, -1, -1):
        for entity in scopes[i][2]:
            if entity[0] == assignmentId:
                found = True
                if len(entity) == 4:
                    if entity[1] == 'functiontk':
                        print "Grammi",line,": Den mporeis na anatheteis timh se synarthsh"
                    else:
                        print "Grammi",line,": Den mporeis na anatheteis timh se diadikasia"
                    exit(0)
                break
        if found == True:
            break

    if found == False:
        print "Grammi",line,": Den exeis dhlwsei thn metavlhth "+assignmentId
        exit(0)

    if token[1] == "assignmenttk":
        lex(token)
        expression(token)
        genquad(":=", token[2], "_", assignmentId)
    else:
        print "Grammi",line,": Den yparxei to :="
        exit(0)

def statement(token):
    if token[1] == "idtk":
        assignmentId = token[0]
        lex(token)
        assignmentStat(token, assignmentId)
    elif token[1] == "iftk":
        lex(token)
        ifStat(token)
    elif token[1] == "whiletk":
        lex(token)
        whileStat(token)
    elif token[1] == "repeattk":
        lex(token)
        repeatStat(token)
    elif token[1] == "exittk":
        lex(token)
        exitStat(token)
    elif token[1] == "switchtk":
        lex(token)
        switchStat(token)
    elif token[1] == "forcasetk":
        lex(token)
        forcaseStat(token)
    elif token[1] == "calltk":
        lex(token)
        callStat(token)
    elif token[1] == "returntk":
        lex(token)
        returnStat(token)
    elif token[1] == "inputtk":
        lex(token)
        inputStat(token)
    elif token[1] == "printtk":
        lex(token)
        printStat(token)

def statements(token):
    statement(token)
    while token[1] == "semicolontk":
        lex(token)
        statement(token)

def formalparitem(token):
    if token[1] == "intk":
        lex(token)
        if token[1] == "idtk":
            offset = 12
            for entity in scopes[len(scopes)-1][2]:
                if entity[0] == token[0]:
                    print "Grammi",line,": Den prepei na exeis idio onoma"
                    exit(0)
                if len(entity) == 2 or len(entity) == 3:
                    offset = offset + 4

            scopes[len(scopes)-1][2].append([token[0], offset, "CV"])
            lex(token)
        else:
            print "Grammi",line,": Prepei na exei onoma parametrou"
            exit(0)
    elif token[1] == "inouttk":
        lex(token)
        if token[1] == "idtk":
            offset = 12
            for entity in scopes[len(scopes)-1][2]:
                if entity[0] == token[0]:
                    print "Grammi",line,": Den prepei na exeis idio onoma"
                    exit(0)
                if len(entity) == 2 or len(entity) == 3:
                    offset = offset + 4

            scopes[len(scopes)-1][2].append([token[0], offset, "REF"])
            lex(token)
        else:
            print "Grammi",line,": Prepei na exei onoma parametrou"
            exit(0)
    else:
        print "Grammi",line,": Prepei na yparxei in i inout"
        exit(0)

def formalparlist(token):
    formalparitem(token)
    while token[1] == "commatk":
        lex(token)
        formalparitem(token)

def formalpars(token):
    if token[1] == "lpartk":
        lex(token)
        if token[1] != "rpartk":
            formalparlist(token)

        if token[1] == "rpartk":
            lex(token)
        else:
            print "Grammi",line,": Prepei na teleiwnei me )"
            exit(0)
    else:
        print "Grammi",line,": Prepei na exei ("
        exit(0)

def procorfuncbody(token, procorfuncName):
    formalpars(token)
    block(token, procorfuncName)

def subprograms(token):
    global returnCounter, scopes

    typeOfSubprogram = ''
    while token[1] == "proceduretk" or token[1] == "functiontk":
        typeOfSubprogram = token[1]
        lex(token)
        if token[1] == "idtk":

            procorfuncName = token[0]


            for entity in scopes[len(scopes)-1][2]:
                if entity[0] == procorfuncName:
                    print "Grammi",line,": Den prepei na exeis idio onoma"
                    exit(0)

            scopes[len(scopes)-1][2].append([procorfuncName, typeOfSubprogram, -1, -1])

            scopes.append([len(scopes), procorfuncName, []])

            lex(token)
            procorfuncbody(token, procorfuncName)
            if typeOfSubprogram == "proceduretk":
                if token[1] == "endproceduretk":
                    if returnCounter != 0:
                        print "Grammi",line,": H procedure den prepei na exei return"
                        exit(0)
                    returnCounter = 0
                    lex(token)
                else:
                    print "Grammi",line,": Prepei na teleiwnei me endprocedure"
                    exit(0)
            elif typeOfSubprogram == "functiontk":
                if token[1] == "endfunctiontk":
                    if returnCounter == 0:
                        print "Grammi",line,": H function prepei na exei return"
                        exit(0)
                    returnCounter = 0
                    lex(token)
                else:
                    print "Grammi",line,": Prepei na teleiwnei me endfunction"
                    exit(0)
        else:
                print "Grammi",line,": Prepei na dwseis onoma procedure/function"
                exit(0)

def varlist(token):
    global scopes

    if token[1] == "idtk":
        offset = 12
        if token[0] == scopes[len(scopes)-1][1]:
            print "Grammi",line,": Den prepei na exeis idio onoma"
            exit(0)
        for entity in scopes[len(scopes)-1][2]:
            if entity[0] == token[0]:
                print "Grammi",line,": Den prepei na exeis idio onoma"
                exit(0)
            if len(entity) == 2 or len(entity) == 3:
                offset = offset + 4

        scopes[len(scopes)-1][2].append([token[0], offset])
        lex(token)
        while token[1] == "commatk":
            lex(token)
            if token[1] == "idtk":
                offset = 12
                if token[0] == scopes[len(scopes)-1][1]:
                    print "Grammi",line,": Den prepei na exeis idio onoma"
                    exit(0)
                for entity in scopes[len(scopes)-1][2]:
                    if entity[0] == token[0]:
                        print "Grammi",line,": Den prepei na exeis idio onoma"
                        exit(0)
                    if len(entity) == 2 or len(entity) == 3:
                        offset = offset + 4

                scopes[len(scopes)-1][2].append([token[0], offset])
                lex(token)
            else:
                print "Grammi",line,": Meta to , prepei na exei metavlhth"
                exit(0)


def declarations(token):
    if token[1] == "declaretk":
        lex(token)
        varlist(token)
        if token[1] == "enddeclaretk":
            lex(token)
        else:
            print "Grammi",line,": Oi dhlwseis teleiwnoun me enddeclare"
            exit(0)

def block(token, blockName):
    global programName, returnCounter, scopes

    declarations(token)
    subprograms(token)

    if len(scopes) >= 2:
        functionEntity = scopes[len(scopes) - 2][2][len(scopes[len(scopes) - 2][2])-1]
        functionEntity[2] = nextquad()

    genquad("begin block",blockName, "_","_")

    returnCounter = 0
    statements(token)
    if blockName == programName:
        genquad("halt","_","_","_")
    else:

        offset = 12

        for entity in scopes[len(scopes)-1][2]:
            if len(entity) == 2 or len(entity) == 3:
                offset = offset + 4
        functionEntity = scopes[len(scopes) - 2][2][len(scopes[len(scopes) - 2][2])-1]
        functionEntity[3] = offset

    print
    for scope in scopes:
        print scope

    scopes.pop(len(scopes)-1)

    genquad("end block",blockName, "_","_")

def program(token):
    global programName, returnCounter
    if token[1] == "programtk":
        lex(token)
        if token[1] == "idtk":
            programName = token[0]

            scopes.append([len(scopes), programName, []])

            lex(token)
            block(token, programName)
            if token[1] == "endprogramtk":
                if returnCounter != 0:
                    print "Grammi",line,": To programma den prepei na exei return"
                    exit(0)
                print "telos metafrashs"
            else:
                print "Grammi",line,": To programa prepei na teleiwnei me endprogram"
                exit(0)
        else:
            print "Grammi",line,": To programa prepei na exei onoma"
            exit(0)
    else:
        print "Grammi",line,": To programa prepei na arxizei me program"
        exit(0)
def synt():
    token = ['',0,'place',[],[]]
    lex(token)
    program(token)



def nextquad():
    global quads

    return len(quads)

def newtemp():
    global tempCounter

    tempCounter = tempCounter + 1

    temp = "T_"+str(tempCounter)
    offset = 12

    for entity in scopes[len(scopes)-1][2]:
        if entity[0] == temp:
            print "Grammi",line,": Den prepei na exeis idio onoma"
            exit(0)
        if len(entity) == 2 or len(entity) == 3:
            offset = offset + 4

    scopes[len(scopes)-1][2].append([temp, offset])
    return temp

def genquad(op, x, y, z):
    quads.append([nextquad(),op,x,y,z])

def emptylist():
    return []

def makelist(x):
    return [x]

def merge(list1, list2):
    return list1 + list2

def backpatch(list1, z):
    global quads

    for label in list1:
        for quad in quads:
            if quad[0] == label:
                quad[4] = z
                break

def writeIntToFile(filename):
    name = filename.split('.')
    if len(name) == 1:
        openName = name[0]+".int"
    else:
        openName = ".".join(name[0:len(name)-1]) + ".int"
    outfile = open(openName, "w")

    for quad in quads:
        outfile.write(str(quad)+"\n")

    outfile.close()

def writeIntToCFile(filename):
    name = filename.split('.')
    if len(name) == 1:
        openName = name[0]+".c"
    else:
        openName = ".".join(name[0:len(name)-1]) + ".c"
    outfile = open(openName, "w")
    outfile.write("#include <stdio.h>\n")
    outfile.write("#include <stdlib.h>\n")
    outfile.write("int main() {\n")

    variables = []
    for quad in quads:
        for i in range(2,5):
            q = str(quad[i])

            if q[0].isalpha() == True:
                if q not in variables:
                    variables.append(q)

    for variable in variables:
        outfile.write("int "+variable+";\n")

    for quad in quads:
        outfile.write("L"+str(quad[0])+":\n\t")

        if quad[1] == "end block":
            outfile.write("\treturn 0;\n")
            outfile.write("}\n")
        elif quad[1] == "out":
            outfile.write("printf(\"%d\","+ str(quad[2])+");")
        elif quad[1] == "inp":
            outfile.write("scanf(\"%d\",&"+ str(quad[2])+");")

        elif quad[1] == "jump":
            outfile.write("goto L"+str(quad[4])+";\n")
        elif quad[1] == ":=":
            outfile.write(quad[4]+"="+str(quad[2])+";\n")
        elif quad[1] == "+":
            outfile.write(quad[4]+"="+str(quad[2])+"+"+str(quad[3])+";\n")
        elif quad[1] == "-":
            outfile.write(quad[4]+"="+str(quad[2])+"+"+str(quad[3])+";\n")
        elif quad[1] == "*":
            outfile.write(quad[4]+"="+str(quad[2])+"+"+str(quad[3])+";\n")
        elif quad[1] == "/":
            outfile.write(quad[4]+"="+str(quad[2])+"+"+str(quad[3])+";\n")
        elif quad[1] == "=":
            outfile.write("if("+str(quad[2])+"=="+str(quad[3])+")\n\t\tgoto L"+str(quad[4])+";\n")
        elif quad[1] == ">":
            outfile.write("if("+str(quad[2])+">"+str(quad[3])+")\n\t\tgoto L"+str(quad[4])+";\n")
        elif quad[1] == "<":
            outfile.write("if("+str(quad[2])+"<"+str(quad[3])+")\n\t\tgoto L"+str(quad[4])+";\n")
        elif quad[1] == ">=":
            outfile.write("if("+str(quad[2])+">="+str(quad[3])+")\n\t\tgoto L"+str(quad[4])+";\n")
        elif quad[1] == "<=":
            outfile.write("if("+str(quad[2])+"<="+str(quad[3])+")\n\t\tgoto L"+str(quad[4])+";\n")
        elif quad[1] == "<>":
            outfile.write("if("+str(quad[2])+"!="+str(quad[3])+")\n\t\tgoto L"+str(quad[4])+";\n")

        else:
            outfile.write("\n")
    outfile.close()

if len(sys.argv) != 2:
    print "Valte to onoma tou arxeiou eisodou"
    exit(0)

infile = open(sys.argv[1],"r")

synt()
writeIntToFile(sys.argv[1])
writeIntToCFile(sys.argv[1])

for quad in quads:
    print quad
