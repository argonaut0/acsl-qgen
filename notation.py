from random import choice as ch
from random import randint as ri

MAX_EQN_DEPTH = 6
QUESTIONS_PER_CATEGORY = 10

f = open("notation_questions.rtf", "a")

def gen_problems(header, fn, count):
    f.write(header)
    for i in range(count):
        f.write("\n")
        f.write(" " + str(i + 1) + ". ")
        f.write(fn())
    f.write("\n")


def gen_pre_eqn(depth = 0):
    ops = ["+", "-", "*", "/"]
    if depth >= MAX_EQN_DEPTH:
        return " " + ch(ops) + " " + str(ri(1,9)) + " " + str(ri(1,9))
    return " " + ch(ops) + gen_pre_eqn(depth + 1) + " " + str(ri(1,9)) if ri(0,1) else " " + ch(ops) + " " + str(ri(1,9)) + gen_pre_eqn(depth + 1)

def gen_post_eqn(depth = 0):
    ops = ["+", "-", "*", "/"]
    if depth >= MAX_EQN_DEPTH:
        return " " + str(ri(1,9)) + " " + str(ri(1,9)) + " " + ch(ops)
    return gen_post_eqn(depth + 1) + " " + str(ri(1,9)) + " " + ch(ops) if ri(0,1) else " " + str(ri(1,9)) + gen_post_eqn(depth + 1) + " " + ch(ops)

def gen_in_eqn(depth = 0):
    ops = ["+", "-", "*", "/"]
    if depth >= MAX_EQN_DEPTH:
        return "( " + str(ri(1,9)) + " " + ch(ops) + " " + str(ri(1,9)) + " )"
    return "(" + gen_in_eqn(depth + 1) + " " + ch(ops) + " " + str(ri(1,9)) + " )" if ri(0,1) else "( " + str(ri(1,9)) + " " + ch(ops) + gen_in_eqn(depth + 1) + " )"


gen_problems("Evaluate these prefix notation equations:", gen_pre_eqn, 10)
gen_problems("Evaluate these postfix notation equations:", gen_post_eqn, 10)
gen_problems("Convert from prefix notation to postfix", gen_pre_eqn, 10)
gen_problems("Convert from postfix notation to prefix", gen_post_eqn, 10)
gen_problems("Convert from prefix notation to infix", gen_pre_eqn, 10)
gen_problems("Convert from postfix notation to infix", gen_post_eqn, 10)
gen_problems("Convert from infix notation to postfix", gen_in_eqn, 10)
gen_problems("Convert from infix notation to prefix", gen_in_eqn, 10)

f.close()
