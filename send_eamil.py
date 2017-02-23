#__*__coding:utf-8__*__
from setting import Mail
import multiprocessing,time


def proxy():
    m = Mail()
    f = getattr(m,"integration")
    f()

def send_all():
    pool = multiprocessing.Pool(processes=4)
    print "hello"
    # pool.map(m.integration())
    try:
        print "where am i "
        pool.apply_async(proxy)
    except Exception as e:
        print "The exceptionis :",e
    pool.close()
    pool.join()
    print "all processes in the pool are over!"

if __name__ == "__main__":
    start_time = time.time()
    send_all()
    end_time = time.time()
    print end_time - start_time