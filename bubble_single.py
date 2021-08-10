import time
import random




def bubble(x_l):
    #リスト
    x_len = len(x_l)
    flag = 1

    #バブルソート 
    while(flag):
        flag = 0
        for i in range(x_len - 1):
            if(x_l[i] < x_l[i+1]):
                tmp = x_l[i]
                x_l[i] = x_l[i+1]
                x_l[i+1] = tmp

                flag = 1
    #降順に
    x_l.reverse()

    return x_l





if __name__ == "__main__":
    start = time.time()
    
    #リストサイズ
    size = 100000

    x = [random.randint(0, 100) for i in range(size)]
    bubble(x)

    end = time.time()
    print("Finished in {} seconds.".format(end - start))