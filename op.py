#
# File: op.py
# Description: basic arithmetic exercises for children
#


import time
import datetime
import random


ops = {0: '-',
       1: '+',
       2: '*'}


def get_exp():
    op1 = str(random.choice(range(0, 9)))
    op2 = str(random.choice(range(0, 9)))
    op  = ops[random.choice(range(0, len(ops)))]
    if op1 < op2: op1, op2 = op2, op1
    return "%s %s %s " % (op1, op, op2)


def check_op(exp, result):
    return eval(exp) == result 


def go():
    start = time.time()
    count = 0
    n = 100
    for i in range(n):
        exp = get_exp()
        result = input(exp + "= ")
        b = check_op(exp, result)
        print(b)
        if b: count += 1
    ttime = time.time() - start
    print("score: %s/%s" % (count, n))
    print("time: %s" % ttime)

    f = open('log/' + str(datetime.datetime.now().date()), 'w+') 
    f.write('score: %s/%s\n' % (count, n))
    f.write('time: %s\n' % ttime)
    f.close()


go()
