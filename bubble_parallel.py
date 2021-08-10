from multiprocessing import Pool, cpu_count, current_process
from multiprocessing import Pool, Process
from multiprocessing import Manager
import random
import time




def bubble(param):
    # x はリスト, iはリストの番地
    l = param

    len_l = len(l)
    # flag を0に
    flag = 1


    #print(current_process().name, ': This started at %s.' % time.ctime().split()[3])


    while(flag):
        flag = 0
        for i in range(len_l - 1):
            a = l[i]
            b = l[i + 1]
            if a > b:
                l[i] = b
                l[i + 1] = a
                flag = 1

    return l


def bubble_single(param_s):
    ls = param_s
    len_ls = len(l)

    flag = 1

    while(flag):
        flag = 0
        for i in range(len_ls - 1):
            a = ls[i]
            b = ls[i + 1]
            if a > b:
                ls[i] = b
                ls[i + 1] = a
                flag = 1

    return ls






if __name__ == '__main__':
    start = time.time()

    # プロセス数
    p = Pool()

    size = 100000
    batch = 10000


    l = [random.randint(0, 100) for i in range(size)]
    l_20 = []



    for i in range(0, size, batch):

        l_20.append(l[i : i+batch])






    params = [(l_20[l]) for l in range(size//batch)]
    return_l = p.map(bubble, params)


    list_new = []
    for i in range(len(return_l)):
        list_new += return_l[i]

    print("通過")

    bubblist = bubble_single(list_new)
    #print(bubblist)







    elapsed_time = time.time() - start
    print("elapsed_time:{0}".format(elapsed_time) + "[sec]")

