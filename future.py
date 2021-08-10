from multiprocessing import Pool, cpu_count, current_process
from multiprocessing import Pool, Process
from multiprocessing import Manager
import random
import time




def bubble(param):
    # x はリスト, iはリストの番地
    l, i = param
    # flag を0に
    flag_0 = 0

    a = l[i]
    b = l[i + 1]
    print(current_process().name, ': This started at %s.' % time.ctime().split()[3])

    # 交換する場合
    if a > b:

        l[i] = b
        l[i + 1] = a
        flag_0 = 1

        #time.sleep(1)
        return flag_0

    # 交換しない場合
    else:
        flag_0 = 0

        #time.sleep(1)
        return flag_0





if __name__ == '__main__':


    # プロセス数

    # 共有メモリ
    m = Manager()

    #l = Array('i', [random.randint(0, 100) for i in range(10)], lock = False)

    l = m.list([random.randint(0, 100) for i in range(1000)])

    ml = len(l)

    flag = 1



    start = time.time()


    while (flag):

        # フラグを設定
        flag = 0

        flag_0 = 0
        flag_1 = 0



        # (偶数,奇数)ペア

        p = Pool(4)
        # リストの長さが偶数の場合
        if ml % 2 == 0:
            params = [(l, i) for i in range(0, ml - 1, 2)]
            data_0 = p.map(bubble, params)

        # リストの長さが奇数の場合
        if ml % 2 == 1:
            params = [(l, i) for i in range(0, ml - 2, 2)]
            data_0 = p.map(bubble, params)



        for i in range(len(data_0)):
            if data_0[i] == 1:
                flag_0 = 1



        # (奇数,偶数)ペア

        params = [(l, i) for i in range(1, ml - 1, 2)]
        data_1 = p.map(bubble, params)




        p.close()
        p.join()

        for i in range(len(data_1)):
            if data_1[i] == 1:
                flag_0 = 1



        if flag_0 or flag_1:
            flag = 1

    print(l)

    elapsed_time = time.time() - start
    print("elapsed_time:{0}".format(elapsed_time) + "[sec]")