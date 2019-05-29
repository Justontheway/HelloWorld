# -*- coding:utf-8 -*-

import os
import sys
from math import ceil
import time
import signal
os.environ['OMP_NUM_THREADS'] = '1'
import numpy as np
import multiprocessing as mp

MATRIX_SIZE = (20000, 20000)
#MATRIX_SIZE = (2000, 2000)
pool = None
EXIT_FLAG = False

def worker(*args, **kwargs):
    mat1 = np.random.random(MATRIX_SIZE)
    mat2 = np.random.random(MATRIX_SIZE)
    return mat1.dot(mat2).sum()

def forever(worker, *args, **kwargs):
    while True:
        worker(*args, *kwargs)

def sigint(signum, stack):
    global EXIT_FLAG
    EXIT_FLAG = True

def main(size=None):
    global pool, EXIT_FLAG
    signal.signal(signal.SIGINT, sigint)
    ts = time.perf_counter()
    worker()
    te = time.perf_counter()
    t = te - ts
    pool = mp.Pool(size)
    import tracemalloc
    tracemalloc.start()
    while True and not EXIT_FLAG:
        ss1 = tracemalloc.take_snapshot()
        pool.apply_async(worker)
        ss2 = tracemalloc.take_snapshot()
        print(ss2.compare_to(ss1, 'lineno'))
        #pool.apply(worker)
        #pool.map_async(worker, range(int(ceil(t))))
        #pool.map(worker, range(size))
        #time.sleep(t)
    pool.terminate()
    pool.join()

def main1(size=None):
    ps = [mp.Process(target=forever, args=(worker, )) for i in range(size)]
    signal.signal(signal.SIGINT, sigint)
    for p in ps:
        p.start()
    while not EXIT_FLAG:
        time.sleep(1)
    for p in ps:
        p.terminate()
    for p in ps:
        p.join()

if __name__ == "__main__":
    size = max(1, int(ceil(mp.cpu_count() * int(sys.argv[1]) / 100.0)))
    print(size)
    main(size)
    #main1(size)

