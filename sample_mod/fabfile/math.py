from fabric.api import *

@task
def calc_add(x, y):
    '''
    add two integer
    '''
    print '%d + %d = %d' % (int(x), int(y), int(x) + int(y))

@task
def calc_mul(x, y):
    '''
    mul two integer
    '''
    print '%d * %d = %d' % (int(x), int(y), int(x) * int(y))
