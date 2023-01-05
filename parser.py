import math
import ply.lex as lex
from tkinter import Tk, Canvas, Frame, BOTH
import ply.yacc as yacc

reserved = {
    'if': 'IF',
    # 'then': 'THEN',
    'forward': 'FORWARD',
    'backward': 'BACKWARD',
    'left': 'LEFT',
    'right': 'RIGHT',
    'clearscreen': 'CLEARSCREEN',
    'home': 'HOME',
    'penup': 'PENUP',
    'pendown': 'PENDOWN',
    'background': 'BACKGROUND',
    'pencolor': 'PENCOLOR',
    'while': 'WHILE',
    'do': 'DO',
    'end': 'END',
    'then': 'THEN'
}

# tokens = ['PLUS',  'MINUS',  'TIMES',  'DIVIDE',  'LPAREN',  'RPAREN',  'NUMBER', 'ID', 'LBRACE',
#           'RBRACE', 'PLACE', 'NOTSMALLER', 'NOTBIGGER', 'EQUAL', 'SMALLER', 'BIGGER'] + list(reserved.values())
tokens = ['PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'NUMBER', 'ID',
          'PLACE', 'NOTSMALLER', 'NOTBIGGER', 'EQUAL', 'SMALLER', 'BIGGER'] + list(reserved.values())
coord = [300, 300]
# angle = 90

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
# t_LPAREN  = r'\('
# t_RPAREN  = r'\)'
# t_LBRACE = r'\{'
# t_RBRACE = r'\}'
t_PLACE = r'\:='
t_EQUAL = r'\='
t_SMALLER = r'\<'
t_NOTSMALLER = r'\>='
t_NOTBIGGER = r'\<='
t_BIGGER = r'\>'

t_ignore = ' \t'


def t_ID(t):
    r"[a-zA-Z_]\w*"
    return t


# def t_FORWARD(dist, angle, canvas):
#     radians = math.radians(angle)
#     x = math.sin(radians) * dist
#     y = math.cos(radians) * dist
#     # print(math.sin(radians))
#     # print(math.cos(radians))
#     canvas.create_line(coord, coord[0] + x, coord[1] - y)
#     coord[0] += x
#     coord[1] -= y
#     canvas.pack(fill=BOTH, expand=1)
#
# def t_BACKWARD(dist, angle, canvas):
#     x = math.sin(math.radians(angle)) * dist
#     y = math.cos(math.radians(angle)) * dist
#     canvas.create_line(coord, coord[0] - x, coord[1] + y)
#     coord[0] -= x
#     coord[1] += y
#     canvas.pack(fill=BOTH, expand=1)
#
#
# def t_LEFT(val):
#     angle = math.abs()
#
# def t_RIGHT(angle, val):
#     angle = ((angle + val) % 360)
#     return angle

# def FOR()
# def init():
#     root = Tk()
#     root.geometry("300x150")
#     canvas = Canvas(root)
#     canvas.pack()
#     root.mainloop()
def t_NUMBER(t):
    r'\d+'
    # t.value = int(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("line %d: illegal character '%s'" % (t.lineno, t.value[0]))
    t.lexer.skip(1)

def p_S(p):
    """S : ciag_instr """

def p_ciag_instr(p):
    """ciag_instr : instrukcja ciag_instr
                    | empty"""
    # if len(p) == 2:
    #     p[0] = [p[1]]
    # else:
    #     p[0] = [p[1]] + p[2]


def p_empty(p):
    'empty :'
    # pass


def p_instrukcja(p):
    """instrukcja : instr_podst
                    | instr_spec
                    | instr_assign"""
    # p[0] = p[1]


def p_instr_podst(p):
    """instr_podst : instr_zmienna
                    | instr_zwykla"""
    # p[0] = p[1]

def p_instr_zmienna(p):
    """instr_zmienna : FORWARD exp
                    | BACKWARD exp
                    | LEFT exp
                    | RIGHT exp
                    | BACKGROUND color
                    | PENCOLOR color"""
    # p[0] = [p[1], p[2]]


def p_color(p):
    """color : NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER"""
    # p[0] = [p[1], p[2], p[3], p[4], p[5], p[6]]


def p_exp(p):  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!! def t_IDENT(t):
    """exp : numexp
            | ID """
    # if len(p) == 2:
    #     p[0]=p[1]
    # elif len(p) == 3:
    #     p[0] = [p[1],p[2]]

def p_numexp(p):
    """numexp : NUMBER
                | NUMBER numexp"""

def p_instr_zwykla(p):
    """instr_zwykla : CLEARSCREEN
                    | HOME
                    | PENUP
                    | PENDOWN"""
    # p[0] = p[1]


def p_instr_assign(p):
    """instr_assign : ID PLACE exp
                    | ID PLACE instr_mat"""
    # p[0] = p[3]

    # if p[2] == 'exp':
    #     p[0] = p[3]
    # elif p[2] == 'instr_mat':
    #     p[0] = p[3]


def p_instr_mat(p):
    """instr_mat : exp PLUS exp
            | exp MINUS exp
            | exp TIMES exp
            | exp DIVIDE exp"""
    # if p[2] == 'PLUS':
    #     p[0] = p[1] + p[3]
    # elif p[2] == 'MINUS':
    #     p[0] = p[1] - p[3]
    # elif p[2] == 'TIMES':
    #     p[0] = p[1] * p[2]
    # elif p[2] == 'DIVIDE':
    #     p[0] = p[1] / p[3]


def p_instr_war(p):
    """instr_war : exp SMALLER exp
            | exp NOTSMALLER exp
            | exp BIGGER exp
            | exp NOTBIGGER exp
            | exp EQUAL exp"""
    # if p[2] == 'SMALLER':
    #     p[0] = p[1] < p[3]
    # elif p[2] == 'NOTSMALLER':
    #     p[0] = p[1] >= p[3]
    # elif p[2] == 'BIGGER':
    #     p[0] = p[1] > p[2]
    # elif p[2] == 'NOTBIGGER':
    #     p[0] = p[1] <= p[3]
    # elif p[2] == 'EQUAL':
    #     p[0] = p[1] == p[3]


def p_instr_spec(p):
    """instr_spec : instr_while
                | instr_if"""
    # if p[1] == 'instr_while' :
    #     p[0] = 'instr_while'
    # elif p[1] == 'instr_if':
    #     p[0] = 'instr_if'

    # p[0] = [1]


def p_instr_while(p):
    """instr_while : WHILE instr_war DO ciag_instr END """
    # if p[2] == 'instr_war' and p[4] == 'ciag_instr':
    #     while p[2]: p[4]

    # p[0] = [p[1], p[2], p[3], p[4], p[5]]


def p_instr_if(p):
    """instr_if : IF instr_war THEN ciag_instr END """
    # if p[2] == 'instr_war' and p[4] == 'ciag_instr':
    #     if p[2]: p[4]

    # p[0] = [p[1], p[2], p[3], p[4], p[5]]


# def p_error(p):
#     print("parsing error\n")

if __name__ == '__main__':
    # root = Tk()
    # root.geometry("600x600")
    # canvas = Canvas(root)
    # angle = 60
    # t_FORAWRD(200, angle, canvas)
    # angle = RIGHT(angle,200)
    # t_FORAWRD(angle, 200, canvas)
    # root.mainloop()
    # print(math.cos(math.radians(90)))
    lexer = lex.lex()
    parser = yacc.yacc()
    # text = 'forward 1'
    # text = 'a:=1'
    text = 'forward 2'
    parser.parse(text, lexer=lexer)


# 1. wystarczą same te """komentarze""" żeby był język, reszta to były juz akcje wiec je zakomentowałem żeby nie mąciły
# 2. w pliku parser.out który się sam generuje w folderze projektu jak odpalisz parser,
# wypisuje sie gramatyka i latwiej tam patrzeć jak to wygląda
# Ogólnie tam sie wypisuje wszystko, jakieś stany i w ogóle i się spoko to analizuje
# 3. dodałem p_S bo na stacku ktoś pisał że pierwsze produkcja musi być taka prostrza żeby nie było błędów
# 4. w tych co ma być rekurencja dodałem produkcję pustą, tak też pisali na staku że można zrobić

