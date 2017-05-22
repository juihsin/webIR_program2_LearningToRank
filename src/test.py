import os
from random import randint

import bigfloat
import sqlite3
from bigfloat import BigFloat, sub, precision


def no_newline_print():
    for num in range(1, 2001):
        if num == 2000:
            print("?", end='', flush=True)
        else:
            print("?" + ',', end='', flush=True)
    return None


def renew_value_of_list(test_list):
    new_list = []
    for t in test_list:
        t = int(t) + 10
        new_list.append(t)
    test_list = new_list
    return test_list


def while_else():
    qid = []
    for random_count in range(0, 3):
        random_number = randint(2, 8001)
        while random_number in qid:
            random_number = randint(2, 8001)
        else:
            qid.append(random_number)
    print(qid)
    return None


def why_number_nan():
    """
    If you do any of the following without horsing around with the floating-point environment, 
    you should get a NaN where you didn't have one before:

    1. 0/0 (either sign on top and bottom)
    2. inf/inf (either sign on top and bottom)
    3. inf - inf or (-inf) + inf or inf + (-inf) or (-inf) - (-inf)
    4. 0 * inf and inf * 0 (either sign on both factors)
    5. sqrt(x) when x < 0
    6. fmod(x, y) when y = 0 or x is infinite; here fmod is floating-point remainder.
    
    http://stackoverflow.com/questions/25506281/what-are-all-the-possible-calculations-that-could-cause-a-nan-in-python
    
    """

    print(0.1)
    print(BigFloat(0.1))
    print(BigFloat.exact(0.1) * 0.5)
    n0 = BigFloat.exact(
        0.0000000000000000000000000000000000000000000000000000000000000000000000000007678767867868983840900000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)
    test_list = [n0]

    n1 = sub(test_list[0], bigfloat.mul(0.1, 5))
    with precision(2000):
        print(sub(10 ** (-160), 0.5))
    test_list.append(n1)

    # n2 = bigfloat.add(bigfloat.div(test_list[1], 5), 0.1)
    n2 = BigFloat(n1 / 5 + 0.1, context=precision(2000))
    with precision(2000):
        print(test_list[1] / 5 + 0.1)
    # print(BigFloat.exact(test_list[1] / 5 + 0.1))
    test_list.append(n2)

    n3 = BigFloat.exact(test_list[1] / test_list[2])
    n4 = test_list[0] / test_list[2]
    test_list.extend([n3, n4])

    n5 = test_list[3] / test_list[4]
    test_list.append(n5)

    n6 = bigfloat.exp(test_list[4])
    test_list.append(n6)

    n7 = test_list[2] / test_list[4]
    test_list.append(n7)

    n8 = bigfloat.exp(test_list[5])
    test_list.append(n8)

    print(test_list)
    for t in test_list:
        print(str(t))
    return None


def transfer_text_to_list(filepath, delim):
    with open(filepath, 'r') as f:
        lines = f.read().split(delim)
        print(str(lines) + ',', end='', flush=True)
    return None


def main():
    # script_dir = os.path.dirname(os.path.realpath(__file__))
    # rel_path = "../data/t1_weight"
    # abs_file_path = os.path.join(script_dir, rel_path)
    # transfer_text_to_list(abs_file_path, ',')

    no_newline_print()
    # test_list = ['1', '3', '5']
    # print(renew_value_of_list(test_list))
    # while_else()
    # why_number_nan()

    return None


main()
