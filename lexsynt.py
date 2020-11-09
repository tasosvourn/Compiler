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
    elif token[1] == "inouttk":
        lex(token)
        if token[1] == "idtk":
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
        lex(token)
        idtail(token)
    else:
        print "Grammi",line,": Den yparxei to stathera, id i ("
        exit(0)

def term(token):
    factor(token)
    while token[1] == "multtk" or token[1] == "divtk":
        lex(token)
        factor(token)

def expression(token):
    optionalSign(token)
    term(token)
    while token[1] == "plustk" or token[1] == "minustk":
        lex(token)
        term(token)


def boolfactor(token):
    if token[1] == "truetk":
        lex(token)
    elif token[1] == "falsetk":
        lex(token)
    elif token[1] == "nottk":
        lex(token)
        if token[1] == "lbracketstk":
            lex(token)
            condition(token)
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
       relationaloper(token)
       expression(token)

def boolterm(token):
    boolfactor(token)
    while token[1] == "and":
        lex(token)
        boolfactor(token)

def condition(token):
    boolterm(token)
    while token[1] == "ortk":
        lex(token)
        boolterm(token)


def inputStat(token):
    if token[1] == "idtk":
        lex(token)
    else:
        print "Grammi",line,": Prepei na yparxei onoma metavlhths"
        exit(0)


def returnStat(token):
    expression(token)

def printStat(token):
    expression(token)

def callStat(token):
    if token[1] == "idtk":
        lex(token)
        actualpars(token)
    else:
        print "Grammi",line,": Prepei na yparxei onoma procedure"
        exit(0)

def forcaseStat(token):

    if token[1] != "whentk":
        print "Grammi",line,": Prepei na yparxei toulaxiston ena when"
        exit(0)
    while token[1] == "whentk":
        lex(token)
        condition(token)
        if token[1] == "colontk":
            lex(token)
            statements(token)
        else:
            print "Grammi",line,": Den exei :"
            exit(0)

    if token[1] == "endforcasetk":
        lex(token)
    else:
        print "Grammi",line,": Den teleiwnei me endforcase"
        exit(0)

def switchStat(token):
    expression(token)
    if token[1] != "casetk":
        print "Grammi",line,": Prepei na yparxei toulaxiston ena case"
        exit(0)
    while token[1] == "casetk":
        lex(token)
        expression(token)
        if token[1] == "colontk":
            lex(token)
            statements(token)
        else:
            print "Grammi",line,": Den exei :"
            exit(0)
    if token[1] == "endswitchtk":
        lex(token)
    else:
        print "Grammi",line,": Den teleiwnei me endswitch"
        exit(0)

def whileStat(token):
    condition(token)
    statements(token)
    if token[1] == "endwhiletk":
        lex(token)
    else:
        print "Grammi",line,": Den teleiwnei me endwhile"
        exit(0)
    return

def exitStat(token):
    return

def repeatStat(token):
    statements(token)
    if token[1] == "endrepeattk":
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
        lex(token)
        statements(token)
        elsepart(token)
        if token[1] == "endiftk":
            lex(token)
        else:
            print "Grammi",line,": Den teleiwnei me endif"
            exit(0)
    else:
        print "Grammi",line,": Den exei then"
        exit(0)

def assignmentStat(token):

    if token[1] == "assignmenttk":
        lex(token)
        expression(token)
    else:
        print "Grammi",line,": Den yparxei to :="
        exit(0)

def statement(token):
    if token[1] == "idtk":
        lex(token)
        assignmentStat(token)
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
            lex(token)
        else:
            print "Grammi",line,": Prepei na exei onoma parametrou"
            exit(0)
    elif token[1] == "inouttk":
        lex(token)
        if token[1] == "idtk":
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

def procorfuncbody(token):
    formalpars(token)
    block(token)

def subprograms(token):
    typeOfSubprogram = ''
    while token[1] == "proceduretk" or token[1] == "functiontk":
        typeOfSubprogram = token[1]
        lex(token)
        if token[1] == "idtk":
            lex(token)
            procorfuncbody(token)
            if typeOfSubprogram == "proceduretk":
                if token[1] == "endproceduretk":
                    lex(token)
                else:
                    print "Grammi",line,": Prepei na teleiwnei me endprocedure"
                    exit(0)
            elif typeOfSubprogram == "functiontk":
                if token[1] == "endfunctiontk":
                    lex(token)
                else:
                    print "Grammi",line,": Prepei na teleiwnei me endfunction"
                    exit(0)
        else:
                print "Grammi",line,": Prepei na dwseis onoma procedure/function"
                exit(0)

def varlist(token):
    if token[1] == "idtk":
        lex(token)
        while token[1] == "commatk":
            lex(token)
            if token[1] == "idtk":
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

def block(token):
    declarations(token)
    subprograms(token)
    statements(token)


def program(token):
    if token[1] == "programtk":
        lex(token)
        if token[1] == "idtk":
            lex(token)
            block(token)
            if token[1] == "endprogramtk":
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
    token = ['',0]
    lex(token)
    program(token)

if len(sys.argv) != 2:
    print "Valte to onoma tou arxeiou eisodou"
    exit(0)

infile = open(sys.argv[1],"r")

synt()
